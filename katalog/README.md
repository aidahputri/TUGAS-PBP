# **Tugas 2 (Katalog)**
-- [Deployment Link](https://assignment-2-aidahnovallia.herokuapp.com/) --

## **Bagan**
![Bagan](../static/bagan.png?raw=true)
### Penjelasan Bagan
1. Permintaan atau *request* dari *user* yang masuk akan diproses `URLConf` untuk diteruskan ke `views` yang didefinisikan oleh *developer* untuk memproses permintaan tersebut.
2. Jika terdapat proses yang membutuhkan keterlibatan *database*, maka nantinya `views` akan memanggil *query* ke `models`. Setelah itu, *database* akan mengembalikan hasil *query* kepada `views`. Pada akhirnya, `views` akan mengembalikan *response* kepada *user*. Response yang diberikan dipetakan lewat file HTML yang terdapat pada template.
3. `models` pada dasarnya berfungsi untuk mendefinisikan informasi mengenai data yang dimiliki. `models` berisi bidang (*field*) dan juga menyimpan perilaku bagaimana data itu dikelola. Singkatnya, `models` merupakan jembatan antara *database* dengan `views`. `models` akan menerima permintaan dari `views`, kemudian meneruskan permintaan (*query*) ke *database* dan mengembalikan *response* query ke `views`.
4. Template berisi file HTML yang akan ditampilkan ke *user* sebagai *response* dari `views`.

## **Virtual Environment**
### <u>Mengapa menggunakan virtual environment?</u>
*Virtual environment* sendiri adalah sebuah *tool* yang memungkinkan kita untuk membuat *packages* dan *dependencies* yang digunakan pada project ini terisolasi. Dengan begitu, antar satu *project* dengan *project* lain tidak saling mengganggu. Bila dianalogikan, misalnya, terdapat beberapa gelas dengan isi yang berbeda-beda. Ada yang jus, teh, dan kopi. Isi dari gelas tidak akan tercampur walau saling berdekatan karena terhalang dinding gelas. Gelas tersebut merupakan analogi dari *virtual environment* yang menjadi wadah bagi *project* yang kita buat.

### <u>Apakah kita dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*?</u>
Kita tetap bisa membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*. Namun, seperti yang telah dijelaskan sebelumnya, terdapat risiko satu *project* dengan *project* lainnya saling mengganggu. 

## **Implementasi**
### <u>Poin 1</u>
Pada file `katalog/views.py` dibuat sebuah function bernama `show_catalog(request)` yang menerima parameter berupa `request`. Function `katalog/views.py` mengambil seluruh data dari class `CatalogItem` yang berada di `katalog/models.py`. Kemudian, di dalam function `katalog/views.py` dibuat sebuah `context` yang berisi `catalog_item`, `nama`, dan `npm`. Pada akhirnya, function `katalog/views.py` akan me-*render* file `katalog.html`, `context`, dan parameter `request`.

### <u>Poin 2</u>
Pada file `katalog/urls.py` ditambahkan urlpatterns `path('', show_catalog, name='show_catalog')` untuk menampilkan `show_catalog(request)`, tetapi untuk benar-benar tampil pada web, urlpatterns pada `katalog/urls.py` perlu dihubungkan dengan urlpatterns pada `project_django/urls.py`. Oleh karena itu, pada `project_django/urls.py` ditambahkan `path('katalog/', include('katalog.urls'))` untuk mengalihkan *route* `/katalog/` dan memanggil function `show_catalog(request)`

### <u>Poin 3</u>
Pemetaan data pada file `katalog.html` dilakukan dengan menambahkan `{{nama}}` dan `{{npm}}` untuk menampilkan data nama dan npm. Selain itu, ditambahkan looping `catalog_item` untuk menampilkan isi dari `catalog_item` pada tabel. 

### <u>Poin 4</u>
Pertama buat sebuah app pada Heroku, kemudian tambahkan secrets pada repository github berupa `HEROKU_APP_NAME` dan `HEROKU_APP_KEY` yang berisi nama dari aplikasi kita dan API key yang dapat diakses pada `Account Settings` di Heroku.
