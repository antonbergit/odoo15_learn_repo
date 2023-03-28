import json
import random
import urllib.request
from datetime import datetime

print('JSON-RPC test started')

HOST = 'localhost'
PORT = 8569
DB   = 'o15-learn'
USER = 'js@com.net'
PASS = 'noadmin'

def json_rpc(url, method, params):
    data = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": random.randint(0, 1000000000),
    }
    req = urllib.request.Request(url=url, data=json.dumps(data).encode(), headers={
        "Content-Type":"application/json",
    })
    reply = json.loads(urllib.request.urlopen(req).read().decode('UTF-8'))
    if reply.get("error"):
        raise Exception(reply["error"])
    return reply["result"]

def call(url, service, method, *args):
    return json_rpc(url, "call", {"service": service, "method": method, "args": args})

url = "http://%s:%s/jsonrpc" % (HOST, PORT)
uid = call(url, "common", "login", DB, USER, PASS)

#p1 - sessions list
xml_sessions = call(url, "object", "execute_kw",DB, uid, PASS,'openacademy2.sessions','search_read', {})

for xml_rec in xml_sessions:
    print("Session named %s claimed for %s seats" % (xml_rec['name'], xml_rec['seats']))

#p2 - courses scan and get
args = {
    'domain' : [[[('title', 'ilike', 'XMLRPC')]]],
    'limit' : 1,
}
xml_course = call(url, "object", "execute_kw",DB, uid, PASS,'openacademy2.courses','search_read', [[('title', 'ilike', 'XMLRPC')]],{'limit':1})[0]
print("Found course %s named %s" % (xml_course['id'],xml_course['title']))

#p3 - link session to course
xml_session_id = call(url, "object", "execute_kw",DB, uid, PASS,'openacademy2.sessions','create',
                    [{'name'  : 'Remote created ' + datetime.now().strftime("%Y.%M.%D.%H.%M.%S"),
                      'course': xml_course['id'],}])

#p4 - completion report
xml_session = call(url, "object", "execute_kw",DB, uid, PASS,'openacademy2.sessions','search_read', [[('id','=',xml_session_id)]],{'limit':1})[0]
xml_course = call(url, "object", "execute_kw",DB, uid, PASS,'openacademy2.courses','search_read', [[('id','=',xml_course['id'])]],{'limit':1})[0]
print("Course %s linked to Session %s" % (xml_course['title'],xml_session['name']))

print('JSON-RPC test finished')
