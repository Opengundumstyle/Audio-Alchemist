import os,requests

def token(request):
    if not "Authorization" in request.headers:
          return None,("missing credentials",401)
    
    token = request.headers["Authorization"]

    if not token:
          return None,("missing credentials",401)
    
     # Disable SSL verification globally
    requests.packages.urllib3.disable_warnings()

    response = requests.post(
           f"http://{os.environ.get('AUTH_SVC_ADDRESS')}/validate",
           headers={"Authorization":token},
           verify=False
    )
    if response.status_code == 200:
        return response.text,None
    else:
        return None,(response.text,response.status_code)

