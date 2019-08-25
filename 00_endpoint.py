from bottle import route, run, static_file, debug, request, template 
import operator 

# Serve a static homepage on load
@route('/')
def homepage():
    link = "index.html"
    return static_file(link, root='')

# Function to return user keyword
@route('/', method = 'GET')
@route('/', method = 'POST')
def getUsername():
    postdata = request.body.read()
    print(postdata) 

    if postdata:
        # Try to extract form variables
        try:
            username = request.forms.get("username")
            password = request.forms.get("password")
            filename = request.forms.get("filename")
        except:
            link = "error.html"
            return static_file(link, root='')
        
        # Execute script here
        execute_script(username, password, filename)

    link = "index.html"
    return static_file(link, root='')

def execute_script(username, password, filename):
    print("user: ", username)
    print("pass: ", password)
    print("file: ", filename)
    # Run your script here

# To see page, go to localhost:8000
run(host='localhost', port=8000, reloader=True, debug=True)