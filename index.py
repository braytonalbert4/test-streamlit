from js import Response
import requests

def on_fetch(request):
    print("Hi there!")
    return Response.new("Hello!")
