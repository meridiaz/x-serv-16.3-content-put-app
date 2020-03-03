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
        method = request.split()[0]
        resource = request.split()[1]
        body = request.split('\r\n\r\n', 1)[-1]
        return request.split(' ', 2)[1]

    def process(self, resourceName):
        """Process the relevant elements of the request.

        Finds the HTML text corresponding to the resource name,
        ignoring requests for resources not in the dictionary.
        """
        method, resource, value = resourceName

        if method == 'PUT':
            self.content[resource] = value

        #self.content equivalente a self.content.keys()
        if resourceName in self.content:
            httpCode = "200 OK"
            htmlBody = "<html><body>" + self.content[resourceName] \
                + "</body></html>"
        else:
            httpCode = "404 Not Found"
            htmlBody = "Not Found"
        return (httpCode, htmlBody)


if __name__ == "__main__":
    testWebApp = contentApp("localhost", 1234)
