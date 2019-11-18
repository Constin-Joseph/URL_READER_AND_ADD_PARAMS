from requests.models import PreparedRequest
import urllib.request
import json
def apipara(a):
    req = PreparedRequest()
    url = "any url"
    params = {'ID':a}
    req.prepare_url(url, params)
    content = urllib.request.urlopen(req.url).read()
    data = json.loads(content)
    print(data['success'])#I Extract json content
    print(data['msg'])#I Extract json content
apipara(1)
   


