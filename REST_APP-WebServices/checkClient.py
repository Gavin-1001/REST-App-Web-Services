import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8001/") as proxy:
    print("and our survey says: %s" % str(proxy.temp_resolve(3)))
