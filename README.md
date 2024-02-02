# PythonRPC

Pyhton RPC is a library that lets you define daemons and proxy to interact with the daemons. In this repo I will create a daemon that will act like a server and create a proxy to make RPC calls on behalf of the client and return to it the results. 

## Creating Deamons and registering services

For more information on daemons check out this video:

<a href="https://youtu.be/wOWhfNB_r-0?si=1_9TWXYGcI0YbWa4" target="_blank">
 <img alt="Watch Video on Deamons" width="240" height="180" src="https://i.ytimg.com/an_webp/wOWhfNB_r-0/mqdefault_6s.webp?du=3000&sqp=CNnD9K0G&rs=AOn4CLB8G0D1bguJcRe7RoLffjQiTzL5nQ"/>
</a>

In summary they are instances of programs that run on the background in your machine. They are typically not started manually by the user of the machine and run various background services. 

Pyro4 allows one to create a daemon using the command below:

```python
daemon = Pyro4.Deamon()
```

The daemon can then be set to listen for requests on the background using the following command:

```python
deamon.request_loop()
```

To add a service to be running on the daemon and can respond to requests you create a class that represents the service and its reachable functions. An example of how to do this is below. Registering returns a URI that can be used to uniquely identify the service in the deamon:

```python
service = MyService()

uri = deamon.register(service)
```

Don't forget to expose the service that you want to be callable by adding the decorator @Pyro4.expose to the class.

## Calling services on the daemon

To call a service on a daemon you need a proxy. The proxy will be incharge of taking the request from your client and passing it to the server. It then returns to the clients the results from the server.

To get a proxy for the service you need the services URI. An example is:

```python
proxy = Pyro4.Proxy(uri)
```

You then call methods in the proxy as if it were an object of the service e.g you can do proxy.add(1).
