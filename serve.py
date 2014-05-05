from flask import Flask, request, render_template, redirect
app = Flask(__name__)
import json
from main import matchDomainToColor

@app.route('/<domain>/')
def reroute(domain):
  return redirect("/%s/color.info" % domain)

@app.route('/<domain>/color.info')
def convertDomain(domain):
  # Stupid UTF-8
  domain = str(domain)
  try:
    color = matchDomainToColor(domain)
    return render_template('index.html',domain=domain,color=color)
  except Warning, e:
    return render_template('index.html',domain=domain,error="doesn't have any certificates!")
  except Exception, e:
    print "Exception -> %s" % e
    return render_template("l33thax0r.html")

@app.route('/<domain>/color.value')
def colorValue(domain):
  domain = str(domain)
  try:
    color = matchDomainToColor(domain)
    return color
  except Warning, e:
    return "ERROR, no certs found :("
  except:
    return render_template("l33thax0r.html")

@app.route('/<domain>/color.json')
def jsonRespond(domain):
  properties = {}
  try:
    color = matchDomainToColor(domain)
    properties['domain'] = domain
    properties['color'] = color
    properties['error'] = None
    return json.dumps(properties)
  except Warning, e:
    properties['domain'] = domain
    properties['error'] = "No certificates found at %s" % domain
    return json.dumps(properties)
  except:
    return render_template("l33thax0r.html")

if __name__ == "__main__":
    app.run(debug=True)
