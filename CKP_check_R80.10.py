import requests, json

json_payload = {"user":"987301598","password":"7242333222"}
ip_addr = "10.57.8.21"
sid = ""
port = "4433"

def api_call(ip_addr, port, command, json_payload, sid):
    url_login = "https://" + ip_addr + ":" + port + "/web_api/" + command
    if sid == "":
        request_headers = {'Content-Type':'application-json'}
    else:
        request_headers = {'Content-Type':'application-json', 'X-chkp-sid' : sid}
    r = requests.post(url_login, data=json.dumps(json_payload), headers=request_headers, verify=False)
    return r.json()
api_call(ip_addr, port, "login", json_payload, sid)

show_domains = {"limit":"500"}
def check_domains(ip_addr, port, command, sid):
    url_domains = 'https://' + ip_addr + ':' + port + '/web_api/' + command
    request_header_domains = {'Content-Type':'appplication-json', 'X-chkp-sid' : sid}
    print(request_header_domains)
    d = requests.post(url_domains, data=json.dumps(show_domains), headers=request_header_domains, verify=False)
    return d.json()

check_domains("192.168.1.1", port, "show-domains", sid)
