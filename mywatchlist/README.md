# **Tugas 3 (mywatchlist)**

-- [Deployment Link](https://assignment-2-aidahnovallia.herokuapp.com/) --

## **Perbedaan JSON, XML, dan HTML**
---
**HTML (Hypertext Transfer Protocol)** merupakan *markup language* yang menyajikan data dalam bentuk element tree. Data yang direpresentasikan oleh HTML akan ditampilkan dalam bentuk web dan dapat dikustomisasi bentuk dari penyajiannya.

**JSON (JavaScript Object Notation)** menyajikan data dalam bentuk notasi objek Javascript. Data yang direpresentasikan oleh JSON terdiri dari key dan value.

**XML (eXtensible Markup Language)** merupakan *markup language* seperti HTML. Serupa dengan HTML, XML merepresentasikan data menggunakan element tree. Namun, data yang disajikan oleh HTML lebih diperuntukan untuk web browser. 

<br>

## **Mengapa kita memerlukan *data delivery* dalam pengimplementasian sebuah platform?**
---
Data delivery berarti terjadi pertukaran data user dengan data pada server. Pertukaran data pasti sering terjadi dalam proses membangun suatu platform. Penggunaan data delivery akan mempermudah proses pertukaran data. Data delivery sendiri biasanya menggunakan HTML, XML, atau JSON karena mudah dibaca oleh manusia sehingga mempermudah pekerjaan developer.

<br>

## **Implementasi *checklist***
---
1. Membuat aplikasi `mywatchlist` dengan menjalankan perintah `python manage.py startapp mywatchlist`.
2. Menambahkan path `path('mywatchlist/', include('mywatchlist.urls'))` pada urls.py pada `project_django` untuk mengubungkan `urlpatterns` `urls.py` pada `project_django` dengan `urls.py` pada `mywatchlist`.
3. Menambahkan `mywatchlist` pada `INSTALLED_APPS` di `project_django/settings.py` dan menambahkan pattern path-path pada `mywatchilst/urls.py` untuk menghubungkan dengan seluruh function pada `mywatchilst/views.py`.
4. Membuat model data pada `mywatchlist/models.py` dengan fields `watched`, `title`, `rating`, `release_date`, dan `review`.
5. Setelah model dibuat, dilakukan migrasi agar model tersebut dapat digunakan oleh *database* dengan menjalankan perintah `python manage.py makemigrations` dan `python manage.py migrate`.

<br>

## **Postman**
---
### HTML
![html_postman](../static/html_postman.png?raw=true)

<br>

### JSON
![json_postman](../static/json_postman.png?raw=true)

<br>

### XML
![xml_postman](../static/xml_postman.png?raw=true)
