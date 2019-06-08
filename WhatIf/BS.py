from bs4 import BeautifulSoup
import requests

from requests.auth import HTTPBasicAuth

# with open('whatfi.GBL') as f:
#     # k = f.read()
#     soup = BeautifulSoup(f)
#     print(soup)

# s = soup.find_all('tr')
# print(len(s))
# # input()
# # print(soup)

class MyAuth(requests.auth.AuthBase):
    def __call__(self, r):
        print(type(r))
        
        input()
        return r
session = requests.Session()


url = "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s1"
payload = {"j_username": "zz8qc",
           "j_password": "Pw?QS40R2019",
           "_eventId_proceed": "Log In",
           }
AUTH = {"factor": "Phone Call"}
r = session.post(url, data=payload, auth=HTTPBasicAuth('user','pass'))
soup = BeautifulSoup(r.text)
print(soup)
