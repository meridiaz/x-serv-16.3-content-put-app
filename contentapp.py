#!/usr/bin/python3

"""
 contentApp class
 Simple web application for managing content

 Copyright Jesus M. Gonzalez-Barahona, Gregorio Robles 2009-2015
 jgb, grex @ gsyc.es
 TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
 October 2009 - March 2015
"""

import webapp

formulario = """
    <p>Hola mundo</p>
    <form action="/" method="PUT">
      <input name="resource" type="text" />
      <input name="content" type="text" />
    <input type="submit" value="Submit" />
    </form>
"""
class contentApp (webapp.webApp):
    """Simple web application for managing content.

    Content is stored in a dictionary, which is intialized
    with the web content."""

    # Declare and initialize content
    content = {'/': formulario,
               '/page': 'A page'
               }

    def parse(self, request):
        """Return the resource name (including /)"""
        method = request.split(' ', 1)[0]
        resource = request.split(' ', 2)[1]
        print("RECURSO")
        print(resource)
        if method == "PUT":
            body = request.splitlines()[-1]
        else:
            body = None
        return (method, resource, body)

    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Finds the HTML text corresponding to the resource name,
        ignoring requests for resources not in the dictionary.
        """
        method, resource, body = parsedRequest

        if method == 'PUT':
            page, content = body.split('&')
            resource_request = page.split('=')[1]
            content = content.split('=')[1]
            self.content["/"+resource_request] = content

        if resource in self.content:
            httpCode = "200 OK"
            htmlBody = "<html><body>" + self.content[resource]+ "</body></html>"
        else:
            httpCode = "404 Not Found"
            htmlBody = "Not Found"
        return (httpCode, htmlBody)


if __name__ == "__main__":
    testWebApp = contentApp("localhost", 1234)
