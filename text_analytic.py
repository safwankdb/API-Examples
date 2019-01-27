########### Python 2.7 #############
import requests, json

data_file = open("data.txt","r")
data = data_file.read()
url = 'https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/keyPhrases'
payload = {
    # Request parameters
    "documents": [
    {
      "id": "string",
      "text": data    
    }
  ]
}
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '45e41a3a0ca744b9a6c569e40c39b524',
}

try:
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    results = response.json()['documents'][0]['keyPhrases']
    for result in results:
      print(result)
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))