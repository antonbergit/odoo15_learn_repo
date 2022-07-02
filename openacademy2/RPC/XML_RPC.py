import xmlrpc.client
from datetime import datetime

print('XML-RPC test started')

HOST = 'localhost'
PORT = 8569
DB   = 'o15-learn'
USER = 'js@com.net'
PASS = 'noadmin'

url = 'http://%s:%d/xmlrpc/' % (HOST, PORT)
uid = xmlrpc.client.ServerProxy(url + 'common').login(DB, USER, PASS)
print("Logged in as %s (uid: %d)" % (USER, uid))

#p0 - connection node
cnode = xmlrpc.client.ServerProxy(url + 'object')

#p1 - sessions list
xml_sessions = cnode.execute_kw(DB, uid, PASS,'openacademy2.sessions','search_read', '', '')

for xml_rec in xml_sessions:
    print("Session named %s claimed for %s seats" % (xml_rec['name'], xml_rec['seats']))

#p2 - courses scan and get
xml_course = cnode.execute_kw(DB, uid, PASS,'openacademy2.courses','search_read', [[('title', 'ilike', 'XMLRPC')]],{'limit':1})[0]
print("Found course %s named %s" % (xml_course['id'],xml_course['title']))

#p3 - link session to course
xml_session_id = cnode.execute_kw(DB, uid, PASS,'openacademy2.sessions','create',
                    [{'name'  : 'Remote created ' + datetime.now().strftime("%Y.%M.%D.%H.%M.%S"),
                      'course': xml_course['id'],}])

#p4 - completion report
xml_session = cnode.execute_kw(DB, uid, PASS,'openacademy2.sessions','search_read', [[('id','=',xml_session_id)]],{'limit':1})[0]
xml_course = cnode.execute_kw(DB, uid, PASS,'openacademy2.courses','search_read', [[('id','=',xml_course['id'])]],{'limit':1})[0]
print("Course %s linked to Session %s" % (xml_course['title'],xml_session['name']))

print('XML-RPC test finished')
