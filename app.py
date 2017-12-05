from flask import Flask, render_template, request
import urllib2
import json

app = Flask(__name__)

@app.route('/')
def root():
    resp = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=DLYQ8B0goiFYveZzE6IR8mJvpnxH25jfmexgIDNy")
    string = rep.read()
    dictionary = json.loads(string)
    resp2 = urllib2.urlopen("https://content.guardianapis.com/search?api-key=a136031c-da93-4bea-912a-cfdc669d03c2")
    string2 = resp2.read()
    dictionary2 = json.loads(string2)
    return render_template('base.html', pic = dictionary['url'], info = dictionary["explanation"], guardianlink = dictionary2["response"]["results"][0]["webUrl"])

if __name__ == '__main__':
    app.run(debug = True)
