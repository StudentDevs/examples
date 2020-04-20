# APIs

# Consuming JSON APIs

Use the python `requests` library.

https://requests.readthedocs.io/en/master/user/quickstart/#json-response-content

Most APIs you use will require having an account at a service you're trying
to interact with, but there are a few public APIs with fun data.

Big list of public APIs:

https://github.com/public-apis/public-apis

A few examples:

http://open-notify.org/Open-Notify-API/

https://developer.github.com/v3/


# Providing JSON APIs

Using `bottle`, returning a `dict` from a request handler will automatically
cause a JSON object to be sent to the client. That is, rather than an HTML
response which is what is sent to the client (browser) when you return a string
from request handler.

