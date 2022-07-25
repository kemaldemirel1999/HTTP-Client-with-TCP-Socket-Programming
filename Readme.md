run server.py HTTP Client, then send request

--------------------------------

GET/isPrime

parameter name must be "number" 

number must be prime number

must be integer

example request: http://localhost:8080/isPrime?number=11

when the number is a prime number and parameter name is "number", then response: {"number": 5, "isPrime": "True"}



---------------------------------
GET/download

Allows to client to download the file from the server

example:  http://localhost:8080/download?fileName=kemaldemirel.png

kemaldemirel.png will be download

After the file is downloaded: HTTP 200 OK and related message

If there is no fileName parameter: HTTP 404 NOT FOUND and related message

If there is no file: HTTP 200 OK and related message

---------------------------------
PUT/rename

Allows to filename to be changed

example: http://localhost:8080/rename?oldFileName=demirel.txt&newName=btc.txt

If there is no oldFileName parameter: HTTP 404 NOT FOUND and related message

If there is no newName parameter: HTTP 404 NOT FOUND and related message

If there is no oldFileName and newName parameter: HTTP 404 NOT FOUND and related message

If the file specified by the oldFileName parameter does not exists: HTTP 200 OK and related message

If the filename successfully changed: HTTP 200 OK and related message

---------------------------------

DELETE/remove

Allows to file to be removed

example: http://localhost:8080/remove?fileName=eth.txt

If there is no fileName parameter: HTTP 404 NOT FOUND and related message

If the file that is specified by fileName parameter is not found: HTTP 404 NOT FOUND and related message

If the file is removed: HTTP 200 OK and related message

-------------------------------------

POST/upload

If client wants to upload a file to the server

example:  http://localhost:8080/upload?fileName=metinkemal.txt

If there is no fileName parameter: HTTP 404 NOT FOUND and related message

If the file is not found: HTTP 200 OK and related message

If successful: HTTP 200 OK and related message

---------------------------------------
