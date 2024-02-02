


import Pyro4 # Help in making daemon
import typing 
# Defining the server
@Pyro4.expose
class MyServer:
    # Process to increment an integer
    def increment(self, x: int) -> int:
        return x + 1
    
    # Accepts a float and an int. Squares the float and adds the int to it
    def squareAndAdd(self, f: float, x: int) -> float:
        fsquared = f ** 2
        return fsquared + x
    
    # Reverses a string
    def reverseString(self, s: str) -> str:
        return s[::-1]
    
# Register MyServer as a Pyro4 object
myserver = MyServer()

# Create the daemon
daemon = Pyro4.Daemon()

# Register the server in the daemon
uri = daemon.register(myserver)

print(f"Server can be reached on {uri}")

daemon.requestLoop()