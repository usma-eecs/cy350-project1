## Overview

In this project, you will implement a simple HTTP server at the application layer.

### Generative AI Use Policy

The use of generative AI tools is __prohibited for the written portion__ of this assignment.

The use of chat-based generative AI tools is _authorized_ for the programming portion of this assignment subject to the following restrictions:

- You may only use a generative AI tool that has **study mode*- or the equivelant concept enabled.
    - ChatGPT calls it `Study` mode.
    - Gemini calls it `Guided Learning` mode.
- You must provide a link to your chat in your DAAW and properly inline cite provided assistance.
    - Recommend that you open your link in an incognito window to verify that it is publicly accessible. If you cannot reach it from an incognito window, your instructor will not be able to access it either.
- You must copy and paste the following prompt as the very first message in any chat on any tool you use:

```txt
Following are the authorized Human-AI teaming (HAT) levels

- HAT Level 1: Support learning of concepts - Focus on explaining concepts, theories, or background knowledge without giving direct solutions.
- HAT Level 2: Collaborate in thinking/reasoning/design - Brainstorm, evaluate, or suggest ideas and options, but do not provide a fully formed solution.

This conversation is for an assignment where you serve as a tutor for me and all responses should be limited to HAT level 1 and HAT level 2. Do not produce parts of the solution.
```

> [!IMPORTANT]
> VS Code Copilot does not meet the DAAW requirement and must be disabled within VSCode before you start writing any code for this project. [Features > Chat > Disable AI Features](vscode://settings/chat.disableAIFeatures)

_Failure to follow any of the above restrictions will be considered unauthorized collaboration will result in a significant deduction of points._

### Learning Objectives

- Implement a functioning HTTP server that can parse HTTP requests, generate appropriate responses, and handle conditional GET requests.
- Analyze and understand protocol behavior using Wireshark.
- Reflect on trade-offs between protocol complexity and performance.

### Submission Instructions

1. You will submit your code to Gradescope. Autograder will give you feedback on the correctness of your implementation.

1. Once you have a working implementation, you will answer several questions on Canvas that explain your thought process. Majority of your grade will be based on your understanding and explanation of your implementation, which requires you to have a working implementation. These must be answered in your own words without any assistance from generative AI tools. You may discuss these questions with your instructor and verbally assist others to develop understanding of the material, but you may not share your written responses with anyone else.

### Points Breakdown

- Develop the HTTP Server = 30 points
- Testing = 10 points
- Explanation of your work = 10 points

> [!NOTE]
> Bonus Points: __`n` extra points__ if you submit the project in its entirety `n` days before the deadline, up to a maximum of 5 points.

## HTTP Server

This project introduces you to the client-server programming paradigm and the basics of HTTP. Using your code from Lab 3, implement a HTTP server that supports [GET](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/GET) method of the HTTP/1.1 protocol. You are only expected to handle one request per connection.

- Correctly initialize a TCP listening socket.
- Accept incoming connections from clients.
- Receive and reassemble a segmented GET or POST request from a client.
- Handle [GET](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/GET) request and parse the method, resource, and headers.
- Look up the requested resource, check the cache, and determine the correct response.
- Generate the HTTP response, properly segment it, and send it back to the client.
- Close the TCP connection after each response and start over.

### Key Tasks

- Implement segmentation and reassembly of messages. This means you will need to handle cases where a single HTTP request or response is split across multiple TCP segments.
- Parse HTTP requests to extract the method, resource, and headers. See [HTTP Message Format](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Messages) for exactly how HTTP messages are structured.
- Handle GET requests. Parse the [If-None-Match](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/If-None-Match) header and conditionally return [304 Not Modified](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/304) if the content cache entry is valid.
- Generate appropriate HTTP responses with correct status codes, headers, and body content.

### Testing

You must test your program yourself. Gradescope will only test certain cases. You will be graded on how thoroughly you test your work. Provide screenshots as evidence of your work.

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

> [!IMPORTANT]
From your browser, you must capture at least one [200 OK](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/200) response and one cached [304 Not Modified](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/304) response. To skip the cache and force a [200 OK](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/200) response, either use the "Disable Cache" checkbox in your browser network monitor, or press `Ctrl-Shift-R` to hard reload. If your server returned the [If-None-Match](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/If-None-Match) correctly, your browser will display the [304 Not Modified](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/304) response the second time you load the page.

### Hints

- Most autograder test results are hidden. Come up with your own test cases and test your code locally.
- Test your work incrementally. Don't try to implement everything at once. Test each piece as you go.
- Use Wireshark to analyze the packets being sent and received by your server.
- Add lots of print statements to your code to understand the flow of execution and produce useful debug information. You can comment out some of these print statements as you progress.
- Check CRLF termination `\r\n\r\n` carefully.
- Ensure `Content-Length` matches body length.
- Use your browser's Network Monitor to analyze [If-None-Match](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/If-None-Match) header and expected [304 Not Modified](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/304) response.
