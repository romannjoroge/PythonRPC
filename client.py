import Pyro4 # use to create proxy

# Get URI of MyServer in daemon
uri = input("Enter Server URI: ")

# Create Proxy to communicate with server
myServerProxy = Pyro4.Proxy(uri=uri)

# Call functions using proxy
numberToIncrement = 10
floatToSquare = 1.0
numberToAddToSquare = 2
stringToReverse = "Hello"


increment_result = myServerProxy.increment(numberToIncrement)
squareAndAddResult = myServerProxy.squareAndAdd(floatToSquare, numberToAddToSquare)
reverseStringResult = myServerProxy.reverseString(stringToReverse)

# Show results
print(f"Result of incrementing {numberToIncrement} is: {increment_result}")
print(f"Result of squaring {floatToSquare} and adding {numberToAddToSquare} is: {squareAndAddResult}")
print(f"Result of reversing {stringToReverse} is {reverseStringResult}")

