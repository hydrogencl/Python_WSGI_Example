from wsgiref.simple_server import make_server
import wsgiref as WSGI
import re

html0=\
u"<html><head><title>Hi my test case</title></head>\
<body>\
<p>Hallo die Welt</p>\
<p>Bitte eindruck:</p> \
<form action='/' method='get'>\
Celsius temperature: \
<input type='text' name='cel_temp' value='submit'>\
<input type='submit' value='check'><br>\
Fahrenheit temperature: %s \
</form>\
</body></html>\
".encode('utf8')

html=\
"""<html><head><title>Hi my test case</title></head>
<body>
<p>Hallo Welt</p>
<p>Bitte drucken ein:</p> 
<form action='/' method='get'>
Celsius temperature: 
<input type='text' name='cel_temp' value='%s'>
<input type='submit' value='check'><br>
Fahrenheit temperature: %s 
</form>
</body></html>
"""

html_head=\
"""<html><head><title>Hi my test case</title></head>"""

html_body_1=\
"""
<body>
<p>Hallo Welt</p>
<p>Bitte drucken ein:</p> 
"""

html_body_2=\
"""
<form action='/' method='get'>
Celsius temperature: 
<input type='text' name='cel_temp' value='%s'>
<input type='submit' value='check'><br>
Fahrenheit temperature: %s 
</form>
"""
html_body3=\
    """
    
    """

html_tail="""</body></html>"""

def dict_query(str_in):
    arr_in   = re.split("=",str_in)
    print(arr_in)
    if len(arr_in)==0:
        dict_out = {"":""}
    else:
        dict_out = {arr_in[0] : arr_in[1]}
    return dict_out

def convert(num_in):
    num_out = float(num_in) * 180 / 100.0 + 32
    return str(num_out)

def my_app(environ, start_response):
    """a simple wsgi application"""
    cel_temp = "0"
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    #cel_temp = request.get("cel_temp")
    #fah_temp = convert(cel_temp)
    query      = environ['QUERY_STRING']
    #print(query)
    dict_qin = dict_query(query)
    if "cel_temp" in dict_qin:
        print(dict_qin)
        cel_temp    = dict_qin["cel_temp"]
        print(cel_temp)
    fah_temp = convert(cel_temp)
    body=html % (cel_temp, fah_temp)
    return [body]

httpd = make_server('', 8800, my_app)
print("Serving on port 8800...")
httpd.serve_forever()
