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

        # Parse filename from URL and removes '/'
        filename = request.split()[1][1:]

        with open(filename) as f:
            data = f.read()

        http_response = """\
        HTTP/1.1 200 OK
        Content-Type: text/plain
        {0}
        """.format(data)
        client_connection.sendall(http_response)

    except IOError:
        # Put your codes here
        # Send HTTP response message for file not found
        http_response = """\
        HTTP/1.1 404 Not Found
        """
        client_connection.sendall(http_response)

# Put your code here to close the socket
client_connection.close()
