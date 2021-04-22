from xmlrpc.server import SimpleXMLRPCServer

def checkTheWeather(temp):
    if temp < 12:
        return 'cold'
    elif temp > 12:
        return 'hot'


server = SimpleXMLRPCServer(("localhost", 8001))
server.register_function(checkTheWeather,'ctw')
print('listen')
server.serve_forever()
