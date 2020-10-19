### This is a very simple proxy server

The proxy server forwards any url_path's or headers passed to it to the httpbin website. It also returns the response code / headers / body from upstream.

To do:
* No concurrency, single process, single thread. We can only handle a single request at once.
* No error handling.
* No limits implemented because of above. I could use `aiohttp` or a rate limiting package via a decorator, though.
* The output 'wfile' does not conform to HTTP 1.1 standard and thus impossible to open in a browser window (cURL only).

## Running the server
```
docker build -it webby:latest .
docker run -it -p 8080:8080 webby:latest
```

## Example usage
```
~/git/p/scrhub_devops_task$ curl -H 'Super: Header' 127.0.0.1:8080/headers
Date: Mon, 19 Oct 2020 10:34:06 GMT
Content-Type: application/json
Content-Length: 231
Connection: keep-alive
Server: gunicorn/19.9.0
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
HTTP/1.0 200 OK
Server: BaseHTTP/0.6 Python/3.7.3
Date: Mon, 19 Oct 2020 10:34:06 GMT

{
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "identity",
    "Host": "127.0.0.1",
    "Super": "Header",
    "User-Agent": "curl/7.64.1",
    "X-Amzn-Trace-Id": "Root=1-5f8d6b9e-56546f0d796cf30a66d26ce7"
  }
}
```
Response in server console:
```
127.0.0.1 - - [19/Oct/2020 13:32:56] "GET /headers HTTP/1.1" 200 -
```

A non-existing page:
```
~/git/p/scrhub_devops_task$ curl 127.0.0.1:8080/nothing_here
Date: Mon, 19 Oct 2020 10:34:45 GMT
Content-Type: text/html
Content-Length: 233
Connection: keep-alive
Server: gunicorn/19.9.0
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
HTTP/1.0 404 Not Found
Server: BaseHTTP/0.6 Python/3.7.3
Date: Mon, 19 Oct 2020 10:34:45 GMT

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
```
Response code is forwarded to the client:
```
127.0.0.1 - - [19/Oct/2020 13:34:45] "GET /nothing_here HTTP/1.1" 404 -
```