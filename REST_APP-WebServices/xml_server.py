from xmlrpc.server import SimpleXMLRPCServer

def temp_resolve(temp):

    if temp > -1 and temp < 12:
        return 'cold'

    elif temp > 11 and temp < 21:
        return 'warm'

    else:
        return

server = SimpleXMLRPCServer(("localhost", 8001))
print("Listening on port 8001...")
server.register_function(temp_resolve, "temp_resolve")
server.serve_forever()
