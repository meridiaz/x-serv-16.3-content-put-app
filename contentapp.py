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
<!DOCTYPE html>
<html lang="en">
  <body>
    <p>Hola mundo</p>
    <form action="/" method="PUT">
      <input name="content" type="text" />
      <input name="texto" type="text" />
    <input type="submit" value="Submit" />
    </form>
  </body>
</html>
"""
class contentApp (webapp.webApp):
    """Simple web application for managing content.

    Content is stored in a dictionary, which is intialized
    with the web content."""

    # Declare and initialize content
    content = {'/': 'Root page',
               '/page': 'A page'
               }

    def parse(self, request):
        """Return the resource name (including /)"""
        print(request, flush = True)
        method = request.split(' ', 1)[0]
        resource = request.split(' ', 2)[1]
        if method == "PUT":
            body = request.split('/r/n')[-1]
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
            resource = page.split('=')[1]
            content = content.split('=')[1]
            self.content["/"+resource] = content

        if resource in self.content:
            httpCode = "200 OK"
            htmlBody = formulario
        else:
            httpCode = "404 Not Found"
            htmlBody = "Not Found"
        return (httpCode, htmlBody)


if __name__ == "__main__":
    testWebApp = contentApp("localhost", 1234)
