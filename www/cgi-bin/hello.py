#!/usr/bin/env python
import os

headers = ["Content-type: text/html"]
qs = os.environ['QUERY_STRING']

def sendHeaders():
    for h in headers:
        print h
    print "\n"

def sendForm():
    print '''
    <html>
      <body>
          <form action='hello.py' method='get'>
              <label for="myname">Enter Your Name</label>
              <input id="myname" type="text" name="firstname" value="Nada" />
              <input type="submit">
              <label for="myname1">Enter Your Name</label>
              <input id="myname1" type="text" name="firstname1" value="Nada" />
              <input type="submit">
          </form>
      </body>
    </html>
    '''

def sendPage(name):
    print '''
    <html>
      <body>
        <h1>Hello {0}</h1>
      </body>
    </html>
    '''.format(name)

if not qs:
    sendHeaders()
    sendForm()
else:
    if 'firstname' in qs:
        name = qs.split('=')[1]
    else:
        name = 'No Name Provided'
    sendHeaders()
    sendPage(name)