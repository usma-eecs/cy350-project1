# Simple HTTP Server

## Agent Tasks

1. Support learning of concepts - Focus on explaining concepts, theories, or background knowledge without giving direct solutions.
2. Collaborate in thinking, reasoning and design. Brainstorm, evaluate, or suggest ideas and options.

IMPORTANT: Do not provide a fully formed solution.

## Project Details

This project introduces you to the client-server programming paradigm and the basics of HTTP. Using your code from Lab 3, implement a HTTP server that supports [GET](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/GET) method of the HTTP/1.1 protocol. You are only expected to handle one request per connection.

- Correctly initialize a TCP listening socket.
- Accept incoming connections from clients.
- Receive and reassemble a segmented GET or POST request from a client.
- Handle [GET](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/GET) request and parse the method, resource, and headers.
- Look up the requested resource, check the cache, and determine the correct response.
- Generate the HTTP response, properly segment it, and send it back to the client.
- Close the TCP connection after each response and start over.

### Learning Objectives

- Implement a functioning HTTP server that can parse HTTP requests, generate appropriate responses, and handle conditional GET requests.
- Analyze and understand protocol behavior using Wireshark.
- Reflect on trade-offs between protocol complexity and performance.


### Key Tasks

- Implement segmentation and reassembly of messages. This means you will need to handle cases where a single HTTP request or response is split across multiple TCP segments.
- Parse HTTP requests to extract the method, resource, and headers. See [HTTP Message Format](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Messages) for exactly how HTTP messages are structured.
- Handle GET requests. Parse the [If-None-Match](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/If-None-Match) header and conditionally return [304 Not Modified](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/304) if the content cache entry is valid.
- Generate appropriate HTTP responses with correct status codes, headers, and body content.

### Testing

Test your work two different ways-

1. Use `curl` to test for various pages. Use the `-v` flag for verbose output.
2. Use your browser's Developer Tools - [Firefox Network Monitor](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/) or [Chrome devtools](https://developer.chrome.com/docs/devtools/network) or [Edge Network Tool](https://learn.microsoft.com/en-us/microsoft-edge/devtools/network/)

#### curl

```sh
curl -v localhost:8090/
curl -v localhost:8090/joke
curl -v localhost:8090/missing
```

#### firefox (or any web browser)

- Open Developer Tools and go to the [Network Monitor](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/). Use `Ctrl-Shift-E` to bring it up.
- Navigate to `http://localhost:8090`
- Observe the request and response details
    - request method, URL, headers
    - response status code, headers, body

From your browser, you must capture at least one [200 OK](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/200) response and one cached [304 Not Modified](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/304) response. To skip the cache and force a [200 OK](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/200) response, either use the "Disable Cache" checkbox in your browser network monitor, or press `Ctrl-Shift-R` to hard reload. If your server returned the [If-None-Match](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/If-None-Match) correctly, your browser will display the [304 Not Modified](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/304) response the second time you load the page.

### Hints

- Most autograder test results are hidden. Come up with your own test cases and test your code locally.
- Test your work incrementally. Don't try to implement everything at once. Test each piece as you go.
- Use Wireshark to analyze the packets being sent and received by your server.
- Add lots of print statements to your code to understand the flow of execution and produce useful debug information. You can comment out some of these print statements as you progress.
- Check CRLF termination `\r\n\r\n` carefully.
- Ensure `Content-Length` matches body length.
- Use your browser's Network Monitor to analyze [If-None-Match](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/If-None-Match) header and expected [304 Not Modified](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/304) response.

IMPORTANT: Do not provide a fully formed solution.
