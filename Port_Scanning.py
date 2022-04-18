import socket
import pyfiglet

ascii_banner = pyfiglet.figlet_format("PORT SCANNER") # Banner for script
print(ascii_banner) # Printing out the banner at the start of the script.

for port in range(1,4000): # Loop to check if a port is open. Looping throughout the designated range.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Open up the socket and a stream.
    results = sock.connect_ex(("Host IP", port)) # Connecting to the particular host to scan.

    #If and else statement to determine if the ports are open or closed.
    if results == 0:
        print("Port " + str(port) + " is open")
    else:
        print("Port " + str(port) + " is closed")
    sock.close()
