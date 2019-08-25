from bottle import route, run, static_file, debug, request, template 
import operator

# Serve a static homepage on load
@route('/')
def homepage():
    link = "index.html"
    return static_file(link, root='')

# Function to return user keyword
@route('/', method = 'GET')
def getUsername():
    q = request.query_string # 'GET' the query string from form
    if q:
        print("Q : ", q)
    else:
        link = "index.html"
        return static_file(link, root='')

# To see page, go to localhost:8000
run(host='localhost', port=8000, reloader=True, debug=True)