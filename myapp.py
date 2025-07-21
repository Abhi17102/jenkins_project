from flask import Flask
import socket

app=Flask(_name_)


@app.route("/home")
def myhome():
	hostname = socket.gethostname()
	IPaddr = socket.gethostname(hostname)
	return f"Welcome to Abhishek Dhabhai's page....<br> my hostname:{hostname} <br> myIP:{IPAddr}"

app.run(host="0.0.0.0")