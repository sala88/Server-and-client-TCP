
from flask import Flask

app = Flask(__name__)

# 1 - c# SignalR
# 2 - WebSocket


@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Web Server</title>
  </head>
  <body>
    <h1> Questo server sta girando sul local host </h1>
    <p> Benvenuto </p>
    <p>La frequenxza della cpu è" 17 <è/>
  </body>
</html>    '''

if __name__ == 'main':
    app.run(debug=True, host='0.0.0.0')

    #f 1


