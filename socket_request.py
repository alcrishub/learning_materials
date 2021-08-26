#!/usr/bin/env python3

import request
import socket

def check_localhost():
	localhost = socket.gethostbyname("localhost")
	return localhost == "127.0.0.1"

def check_connectivity():
	response = request.get("https://www.google.com")
	return response.status_code == 200