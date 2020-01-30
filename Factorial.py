# Import socket module
import socket

# Put in your codes here to create a TCP sever socket and bind it to your server address and port number
HOST, PORT = '', 8888
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

# Server should be up and running and listening to the incoming connections
while True:
    print('Ready to serve...')

    # Put your codes here
    # Set up a new connection from the client
    client_connection, client_address = listen_socket.accept()

    # If an exception occurs during the execution of try clause
    # the rest of the clause is skipped
    # If the exception type matches the word after except
    # the except clause is executed
    try:
        # Put your codes here
        # Receives the request message from the client
        request = client_connection.recv(1024)

        # Parse value from URL and removes '/'
        value = request.split()[1][1:]

        # Initialize to iterate starting at 1
        fact = 1
        # Calculate factorial
        for i in range(1,int(value)+1):
            fact = fact * i

        http_response = ("HTTP/1.1 200 OK"
                        "Content-Type: text/plain\n\n"
                        "Factorial is: {0}").format(fact)
        client_connection.sendall(http_response)
        client_connection.close()
    except Exception as e:

        # Catches all types exceptions
        http_response = """\
        HTTP/1.1 400 Bad Request
        """
        client_connection.sendall(http_response)
        client_connection.close()
