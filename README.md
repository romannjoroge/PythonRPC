# PythonRPC
Pyhton RPC is a library that lets you define daemons and proxy to interact with the daemons. In this repo I will create a daemon that will act like a server and create a proxy to make RPC calls on behalf of the client and return to it the results. 

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