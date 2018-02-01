# Issue with sending large-ish CSV files to Flask

I am trying to send a csv file as a base64 encoded string in the body of a post request to a flask server. It works find for small files. But when I try to post a file above ~150k the server does not respond and there is no error message. It seems to get hung up on `body = request.get_json()`. This non-responsiveness happens through postman and node. To throw a wrench into the problem, I can submit the file fine using pythons requests library. I am not sure what is causing this or what the difference between the three requests. The headers all look really similar and are included below. I have included the minimal server (server.py), working python request (test.py), the not working node request (jstest.js) and the not working postman collection. Thanks for any help.

## Install
```
git clone https://github.com/mdemin914/flask-largeish-csv-file-error-reproduction.git
cd flask-largeish-csv-file-error-reproduction/
pip install flask requests
```
### Steps to Reproduce
- Run the server 
```
python server.py
```
- Submit a request using python
```
python test.py
```
- You will get "hello world" from the response
- Submit the request with node, it will not return anything and just hangs.
```
node jstest.js
```
- Restart the python server
- Submit with postman
- Import the validation.postman_collection and run it
- It will hang with no errors and no response


## Request Headers on the server
### Postman
```
Content-Length: 189486
User-Agent: PostmanRuntime/7.1.1
Connection: keep-alive
Postman-Token: c6efbbe7-c802-4e8d-be29-acff1efe10ba
Host: localhost:5000
Cache-Control: no-cache
Accept: application/json
Content-Type: application/json
Accept-Encoding: gzip, deflate
```

### Python
```
Content-Length: 189486
User-Agent: python-requests/2.18.4
Connection: keep-alive
Postman-Token: 39421b2e-391e-5228-12dc-feed487fc668
Host: localhost:5000
Cache-Control: no-cache
Accept: application/json
Content-Type: application/json
Accept-Encoding: gzip, deflate
```

### Node
```
Connection: keep-alive
Postman-Token: 41b041b3-75d0-e8c9-7367-42303b303a8b
Host: localhost:5000
Cache-Control: no-cache
Accept: application/json
Content-Type: application/json
Accept-Encoding: gzip, deflate
```

## Versions
```
python 2.7.13
macOS high-sierra 10.12.6
node v7.7.1
postman Version 5.5.2
```