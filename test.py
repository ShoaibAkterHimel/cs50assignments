import requests
import json
import sys
if len(sys.argv)!=2:
    sys.exit()

response=requests.get("https://itunes.apple.com/search?entity=album&limit=20&term=" + sys.argv[1])
x=response.json()
y=(json.dumps(x,indent="2"))
for i in x["results"]:
    print(i["artistName"])



