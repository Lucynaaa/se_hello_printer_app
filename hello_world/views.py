from hello_world import app
from flask import request

moje_imie = "Lucy&Mike"
msg = "Hello: "


@app.route('/')
def index():
   return msg + moje_imie 
