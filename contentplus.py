#!/usr/bin/python3
#ejercicio como el anterior pero con put y post juntos
"""
 contentApp class
 Simple web application for managing content

 Copyright Jesus M. Gonzalez-Barahona, Gregorio Robles 2009-2015
 jgb, grex @ gsyc.es
 TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
 October 2009 - March 2015
"""

import contentapp
#el action indica a que recurso se envia el formualrio
#si no se pone nada es la barra
formulario = """
<br/br>
<form action="" method == "POST">
    <input type= "text" name= "name" value ="">
    <input type= "submit" value ="Enviar">
</form>

"""
class contentPlus (contentapp.contentApp):
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
        method, resource, body = resourceName

        if method == 'PUT':
            #el body es directamente el value
            self.content[resource] = body
        elif method == "POST":
            #el body es el nombre de value, name=value
            self.content[resource] = body.split('=')[1]

        #self.content equivalente a self.content.keys()
        #self.content[resourceName] \  idnica a pep8 que esa linea continua
        #debajo
        if resourceName in self.content:
            httpCode = "200 OK"
            htmlBody = "<html><body>" + self.content[resourceName] \
                + formulario   + "</body></html>"
        else:
            httpCode = "404 Not Found"
            htmlBody = "<html><body>" + "Not Found" + formulario + "</body></html>"
        return (httpCode, htmlBody)


if __name__ == "__main__":
    testWebApp = contentPlus("localhost", 1234)
