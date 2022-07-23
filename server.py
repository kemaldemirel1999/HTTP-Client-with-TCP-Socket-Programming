import os
import socket
import json

# HTTP metodu yanlış gelen veya yanlış endpoint ile gelen tüm isteklere sunucu 404 NOT FOUND kodu dönecek.



def getFileNameParameter(data):
    parameters = data.split("&")
    name = ""
    for val in parameters:
        infos = val.split("=")
        if (infos[0].__eq__("fileName")):
            return infos[1], True
        else:
            name = infos[1]
    return name, False

def isPrime(data):
    number, isItNumberName = getNumberParameter(data)
    response = ""
    try:
        if(isItNumberName == False):
            response = 'HTTP/1.1 400 BAD REQUEST\n\n'
            dict = {"number": number, "message": "Parametreler arasinda number yok"}
            temp = json.dumps(dict)
            response += temp
            return response
        number = int(number)
    except:
        response = 'HTTP/1.1 400 BAD REQUEST\n\n'
        dict = {"number": number, "message": "Lutfen Tam Sayi Giriniz"}
        temp = json.dumps(dict)
        response += temp
        return response
    if(isItInteger(number)):
        if(isItNumberName):
            if(not isItPrimeNumber(number)):
                response = 'HTTP/1.1 200 OK\n\n'
                dict = {"number": number, "isPrime":"True"}
                temp = json.dumps(dict)
                response += temp
            else:
                response = 'HTTP/1.1 200 OK\n\n'
                dict = {"number": number,"message":"Lutfen Asal Sayi Giriniz"}
                temp = json.dumps(dict)
                response += temp
        else:
            response = 'HTTP/1.1 400 BAD REQUEST\n\n'
            dict = {"message": "Parametre arasında number yok"}
            temp = json.dumps(dict)
            response += temp
    else:
        response = 'HTTP/1.1 400 BAD REQUEST\n\n'
        dict = {"number": number, "message": "Lutfen Tam Sayi Giriniz"}
        temp = json.dumps(dict)
        response += temp
    return response

def isItInteger(number):
    if( isinstance(number, int) ):
        return True
    else:
        return False
def getNumberParameter(data):
    parameters = data.split("&")
    number = -1
    for val in parameters:
        infos = val.split("=")
        if(infos[0].__eq__("number")):
            return infos[1], True
        else:
            number = infos[1]
    return number, False

def isItPrimeNumber(number):
    flag = False
    if(number > 1):
        for i in range(2, number):
            if (number % i) == 0:
                flag = True
                break
    if (flag == True):
        return True
    else:
        return False

def getRequestType(data):
    if( data.__contains__("GET")):
        return "GET"
    elif( data.__contains__("POST")):
        return "POST"
    elif( data.__contains__("DELETE")):
        return "DELETE"
    elif( data.__contains__("PUT")):
        return "PUT"
    else:
        return ""
def GETRequestParser(data):
    temp = data.split(" ")[1].split("?")[0][1::]
    if temp.__eq__("isPrime"):
        return "isPrime", data.split(" ")[1].split("?")[1]
    elif temp.__eq__("download"):
        return "download", data.split(" ")[1].split("?")[1]
    else:
        return "", ""
def DELETERequestParser(data):
    temp = data.split(" ")[1].split("?")[0][1::]
    if temp.__eq__("remove"):
        return "remove", data.split(" ")[1].split("?")[1]
    else:
        return "", ""
def POSTRequestParser(data):
    if(data.__contains__("POST")):
        return True
def PUTRequestParser(data):
    temp = data.split(" ")[1].split("?")[0][1::]
    if temp.__eq__("rename"):
        return "rename", data.split(" ")[1].split("?")[1]
    else:
        return "", ""

def upload(conn,text):
    response = ""
    try:
        first_index = text.find("boundary=") + len("boundary=")
        last_index = first_index
        while text[last_index] != "\n" :
            last_index += 1
        boundary = text[first_index : last_index]
        boundaryByte = bytearray(boundary, 'utf-8')
        with open("fileName.jpg", 'wb') as f:
            conn.sendall("HTTP/1.0 200 OK\n\n".encode())
            while True:
                data1 = conn.recv(1024)
                if boundaryByte in data1:
                    f.write(data[0:len(data)-len(boundary)-4])
                    break
                f.write(data1)
                if not data1:
                    break
        response = '{"success":True,"message":"Dosya alimi tamamlandi."}\n\n'
    except FileNotFoundError:
        response = 'HTTP/1.1 200 OK\n\n'
        dict = {"message": "Dosya Bulunamadi"}
        temp = json.dumps(dict)
        response += temp

    return response



def rename(data):
    oldFileName , newName = getRenameParameterName(data)
    if(oldFileName.__eq__("") and newName.__eq__("")):
        response = 'HTTP/1.1 404 NOT FOUND\n\n'
        dict = {"message": "Parametre isimleri hatali"}
        temp = json.dumps(dict)
        response += temp
        return response
    elif(oldFileName.__eq__("")):
        response = 'HTTP/1.1 404 NOT FOUND\n\n'
        dict = {"message": "oldFileName parametresi yok"}
        temp = json.dumps(dict)
        response += temp
        return response
    elif (newName.__eq__("")):
        response = 'HTTP/1.1 404 NOT FOUND\n\n'
        dict = {"message": "newName parametresi yok"}
        temp = json.dumps(dict)
        response += temp
        return response
    try:
        os.rename(oldFileName, newName)
        response = 'HTTP/1.1 200 OK\n\n'
        dict = {"message": "Dosya ismi basari ile degisti"}
        temp = json.dumps(dict)
        response += temp
    except FileNotFoundError:
        response = 'HTTP/1.1 200 OK\n\n'
        dict = {"message": "Dosya Bulunamadi"}
        temp = json.dumps(dict)
        response += temp
    return response

def getRenameParameterName(data):
    parameters = data.split("&")
    oldFileName = ""
    newName = ""

    for val in parameters:
        infos = val.split("=")
        if (infos[0].__eq__("oldFileName")):
            oldFileName = infos[1]
        elif(infos[0].__eq__("newName")):
            newName = infos[1]
        else:
            name = infos[1]
    return oldFileName, newName

def download(conn, data):
    fileName , isItDownloadName = getRemoveNameParameter(data)
    response = ""
    if(isItDownloadName == False):
        response = 'HTTP/1.1 404 NOT FOUND\n\n'
        dict = {"message": "fileName parametresi eksik"}
        temp = json.dumps(dict)
        response += temp
        return response
    try:
        ctr = 0
        with open(fileName, 'rb') as f:
            conn.sendall("HTTP/1.0 200 OK\n\n".encode())
            while True:
                data1 = f.read(1024)
                if not data1:
                    break
                conn.send(data1)
                ctr += 1
        print("Gönderilen Paket Sayısı: ", ctr)
        response ='{"success":True,"message":"Dosya gonderimi tamamlandi."}\n\n'
    except FileNotFoundError:
        response = 'HTTP/1.1 200 OK\n\n'
        dict = {"message": "Dosya Bulunamadi"}
        temp = json.dumps(dict)
        response += temp
    return response


def remove(data):
    fileName , isItRemoveName = getRemoveNameParameter(data)
    if(isItRemoveName == False):
        response = 'HTTP/1.1 404 NOT FOUND\n\n'
        dict = {"message": "fileName parametresi yok"}
        temp = json.dumps(dict)
        response += temp
        return response
    try:
        os.remove(fileName)
        response = 'HTTP/1.1 200 OK\n\n'
        dict = {"success": "True","message": "Dosya Basarili bir sekilde silindi"}
        temp = json.dumps(dict)
        response += temp
    except FileNotFoundError:
        response = 'HTTP/1.1 200 OK\n\n'
        dict = {"success": "False" , "message": "Dosya Bulunamadi"}
        temp = json.dumps(dict)
        response += temp
    return response
def getRemoveNameParameter(data):
    parameters = data.split("&")
    name = ""
    for val in parameters:
        infos = val.split("=")
        if (infos[0].__eq__("fileName")):
            return infos[1], True
        else:
            name = infos[1]
    return name, False

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))

port = 8080

s.bind(("127.0.0.1", port))
s.listen(5)

while True:
    connection, connected_address = s.accept()

    try:
        data = connection.recv(1024).decode()
    except UnicodeDecodeError:
        data = connection.recv(1024).decode('utf-16')
    #data = connection.recv(1024).decode()
    requestType = getRequestType(data)
    response = ""
    if(requestType.__eq__("GET")):
        endpoint, parameter = GETRequestParser(data)
        if(endpoint.__eq__("isPrime")):
            response = isPrime(parameter)
        elif(endpoint.__eq__("download")):
            response = download(connection,parameter)
        else:
            response = 'HTTP/1.1 404 NOT FOUND\r\nMessage:Request error\r\nContent-Length: 0\r\nContent-Type: text/plain\n\n'
    elif(requestType.__eq__("PUT")):
        endpoint, parameter = PUTRequestParser(data)
        if(endpoint.__eq__("rename")):
            response = rename(parameter)
        else:
            response = 'HTTP/1.1 404 NOT FOUND\r\nMessage:Request error\r\nContent-Length: 0\r\nContent-Type: text/plain\n\n'

    elif(requestType.__eq__("DELETE")):
        endpoint, parameter = DELETERequestParser(data)
        if(endpoint.__eq__("remove")):
            response = remove(parameter)
        else:
            response = 'HTTP/1.1 404 NOT FOUND\r\nMessage:Request error\r\nContent-Length: 0\r\nContent-Type: text/plain\n\n'

    elif(requestType.__eq__("POST")):
        flag = POSTRequestParser(data)
        if (flag == True):
            response = upload(connection, data)
        else:
            response = 'HTTP/1.1 404 NOT FOUND\r\nContent-Length: 0\r\nContent-Type: text/plain\n\nMessage:Request error'
    else:
        response = 'HTTP/1.1 404 NOT FOUND\r\nContent-Length: 0\r\nContent-Type: text/plain\n\nMessage:Request error'
    connection.sendall(response.encode())
    connection.close()

