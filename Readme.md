server.py isimli HTTP sunucusunu çalıştırınız ve ilgili requestleri gönderiniz.

--------------------------------

GET/isPrime

parametre ismi "number" olmalı

sayı asal olmalı

tam sayı olmalı

ornek request: http://localhost:8080/isPrime?number=11

sayı asal ve parametre ismi "number" olduğunda örnek response: {"number": 5, "isPrime": "True"}



---------------------------------
GET/download

istemcinin sunucudan dosyayı indirmesini sağlar

ornek:  http://localhost:8080/download?fileName=tobbetulogo.png

tobbetulogo.png indirilecek

Dosya indirilise: HTTP 200 OK ve ilgili mesaj

fileName parametresi yoksa: HTTP 404 NOT FOUND ve ilgili mesaj

dosya yoksa: HTTP 200 OK ve ilgili mesaj

---------------------------------
PUT/rename

dosya isminin değiştirilmesini sağlar.

ornek: http://localhost:8080/rename?oldFileName=demirel.txt&newName=btc.txt

oldFileName parametresi yoksa: HTTP 404 NOT FOUND ve ilgili mesaj

newName parametresi yoksa: HTTP 404 NOT FOUND ve ilgili mesaj

oldFileName ve newName parametresi yoksa: HTTP 404 NOT FOUND ve ilgili mesaj

oldFileName parametresinin belirttiği dosya yoksa: HTTP 200 OK ve ilgili mesaj

Dosya ismi başarıyla değişirse: HTTP 200 OK ve ilgili mesaj

---------------------------------

DELETE/remove

dosyanın silinmesini sağlar.

ornek: http://localhost:8080/remove?fileName=eth.txt

fileName parametresi yoksa: HTTP 404 NOT FOUND ve ilgili mesaj

fileName parametresinin belirttiği dosya bulunamadı: HTTP 404 NOT FOUND ve ilgili mesaj

dosya silinirse: HTTP 200 OK ve ilgili mesaj

-------------------------------------

POST/upload

sunucuya dosya upload edilmek istenmekte

ornek:  http://localhost:8080/upload?fileName=metinkemal.txt

fileName parametresi yoksa: HTTP 404 NOT FOUND ve ilgili mesaj

dosya yoksa: HTTP 200 OK ve ilgili mesaj

başarılı olursa: HTTP 200 OK ve ilgili mesaj

---------------------------------------
