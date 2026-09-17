import os
import sys
import time
import socket
import random
import json
from pathlib import Path
import hashlib
import base64


class HTTPServer:
    def __init__(self, server_ip='127.0.0.1', server_port=8090, frame_size: int = 64, timeout: float = 2.0):
        """
        Initialize the HTTP-like TCP server configuration and resources.

        Parameters
        - server_ip : str - The IP address to listen on.
        - server_port : int - The TCP port to listen on.
        - frame_size : int - Maximum bytes to read/write per send/recv.
        - timeout : float - Socket timeout (seconds) used after accepting.

        Returns: Nothing at all.
        """

        print("Initializing HTTP Server...")

        self.server_ip = server_ip
        self.server_port = server_port
        self.frame_size = frame_size
        self.timeout = timeout

        base_path = Path(__file__).parent
        resources_path = base_path / "resources.json"
        with open(resources_path, "r") as f:
            self.resources = json.load(f)

        # NOTE: build the cache at runtime as you serve requests and calculate ETags
        # see: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/ETag
        self.cache = {  # resource -> ETag
            '/': 'abc123',
            '/about': 'def456',
        }


        # connection-related attributes
        self.connection = None
        self.client_address = None

        print("HTTP Server initialized. Attempting to bind to socket...")

        # create a TCP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # TODO bind and listen

        # print(...)

        # NOTE: Do not set timeout on the listening socket, but only on the accepted connection socket

    def run(self):
        """
        Setup the server socket, loop to accept incoming connections, and handle requests.

        This function should run indefinitely until the server is manually stopped (e.g., with Ctrl+C).
        """

        while True:
            print("Listening for incoming connections...")

            # TODO: accept a handshake and store the connection and client address somewhere

            return "NOT IMPLEMENTED"  # TODO: REMOVE THIS LINE

            # print(...)

            # set a timeout on the connection socket
            self.connection.settimeout(self.timeout)

            # TODO: read upto `frame_size` bytes at a time until the full request is received

            # TODO: ensure robust error handling for socket timeouts and other exceptions while receiving data

            # TODO: build an appropriate HTTP response

            # TODO: send the response back to the client

            # close the connection
            try:
                self.connection.shutdown(socket.SHUT_WR)
                print(f"Shutting down connection: {self.client_address}")
            except Exception as e:
                print(f"An error occurred while shutting down the connection: {e}")

    def parse_request(self, request: str):
        """
        Parse the HTTP request to extract the protocol, method, resource, headers, body.

        Returns:
        - method: The HTTP method (e.g., GET, POST).
        - resource: The requested resource (e.g., /about).
        - headers: A dictionary of HTTP headers.
        """
        method = ""
        resource = ""
        headers = {}

        # TODO: parse the request string to extract the method, resource, and headers
        # see: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Messages

        return method, resource, headers

    def handle_GET(self, resource: str, requestHeaders: dict = {}) -> str:
        """
        Build an HTTP response for the specified resource.

        Returns: A valid HTTP response string
        """

        # TODO: if the resource is not found, return the appropriate response

        # TODO: if the resource is found, check for "If-None-Match" headers
        # TODO: lookup the resource in self.cache and if an ETag is found, match it against the request header value
        # TODO: If they match, return the appropriate response code without sending the resource data
        # see: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/If-None-Match

        # TODO: otherwise, return a response with the resource data
        # TODO: calculate an ETag for the resource data using the provided `calculate_etag()` function
        # TODO: include appropriate headers - Content-Type, Last-Modified, ETag
        # TODO: add an entry to self.cache for the resource with its ETag

    def build_response(self, responseStatus: str, responseBody: str = "", headers: dict = {}) -> str:
        """
        Build an HTTP response with the specified status code, status message, body, and content type.

        Returns: HTTP response string
        """

        # TODO: set the "Connection" header to "close"

        # TODO: set the "Content-Length" header to the length of the response body

        # TODO: generate a valid HTTP response string

        # TODO: include all headers

        # TODO: return the response string

    def build_304(self) -> str:
        """
        Build a 304 Not Modified HTTP response.

        Returns: HTTP response string
        """
        return "HTTP/1.1 304 Not Modified\r\n\r\n"

    def build_404(self) -> str:
        """
        Build a 404 Not Found HTTP response.

        Returns: HTTP response string
        """
        response = (
            "HTTP/1.1 404 Not Found\r\n" +
            "Connection: close\r\n" +
            "Content-Type: text/plain\r\n" +
            "Content-Length: 13\r\n" +
            "\r\n" +
            "404 Not Found"
        )
        return response

    def build_405(self) -> str:
        """
        Build a 405 Method Not Allowed HTTP response.

        Returns: HTTP response string
        """
        response = (
            "HTTP/1.1 405 Method Not Allowed\r\n" +
            "Connection: close\r\n" +
            "Content-Type: text/plain\r\n" +
            "Content-Length: 22\r\n" +
            "\r\n" +
            "405 Method Not Allowed"
        )
        return response

    def calculate_etag(self, content: str) -> str:
        """
        Calculate an ETag for the given content.
        """
        digest = hashlib.sha256(content.encode()).digest()
        return base64.b64encode(digest).decode()

    def send_response(self, response: str) -> None:
        """
        Send the response in chunks of size `frame_size` until the entire response is sent.
        """
        # TODO: Ensure that you break your response into frames of size `frame_size`.
        # TODO: Send each frame separately until the entire response is sent.

        # NOTE: Here, you must use the `send_chunk()` function to send each chunk of data.
        # NOTE: `send_chunk()` is a helper function that simulates network conditions
        # NOTE: Do not attempt to use `self.connection...` directly from here.

    def send_chunk(self, chunk: bytes) -> None:
        """
        Send a single chunk of data through the connection socket.
        """
        if len(chunk) > self.frame_size:
            raise ValueError(f"Chunk size {len(chunk)} exceeds frame size {self.frame_size}")
        self.connection.sendall(chunk)
        time.sleep(random.uniform(0.02, 0.1))  # Simulate network delay

    def close(self) -> None:
        if self.connection:
            self.connection.close()
            print("Connection closed.")
        self.sock.close()


if __name__ == "__main__":
    if os.name != 'posix':
        print("This program should be run on Linux or WSL or docker. You may remove this check at your own risk.")
        sys.exit(1)

    try:
        server = HTTPServer(frame_size=64, timeout=2.0)
        server.run()
    except KeyboardInterrupt:
        print("Shutting down server...")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Add some try/except blocks in your code to locate the issue and handle the errors gracefully.")
        print("Shutting down server...")
    finally:
        server.close()
        print("Server shutdown complete.")
