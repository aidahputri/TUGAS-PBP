# **Tugas 6**

-- [Deployment Link](https://assignment-2-aidahnovallia.herokuapp.com/todolist) --

## **Perbedaan antara *asynchronous programming* dengan *synchronous programming***
- Asynchronous programming merupakan pendekatan pemrograman tidak terikat pada protokol I/O. Hal tersebut menandakan bahwa pemrograman secara asinkronus tidak melakukan pekerjaannya dengan mengeksekusi program satu persatu secara hirarki. Pemrograman secara asinkronus melakukan pekerjaannya tanpa harus terikat dengan proses dengan proses lain.
- Pada synchronous programming, task dieksekusi satu per satu sesuai dengan urutan dan prioritas dari task. Pemrograman secara sinkronus memiliki kekurangan pada lama waktu eksekusi karena masing-masing task harus menunggu task lain selesai terlebih dahulu.

## **Paradigma Event-Driven Programming dan Penerapannya pada Tugas kali ini**
---
Event-Driven adalah suatu paradigma pemrograman yang alur programnya ditentukan dengan suatu peristiwa (event) yang merupakan keluaran dari user. Event-Driven bergantung pada event, sehingga alur program dijalankan dengan tidak terurut dengan menerapkan pemrograman secara asinkronus. Salah satu conton penerapan Event-Driven Programming pada tugas kali ini adalah saat button add task ditekan, fungsi untuk membuat task akan dijalankan. Fungsi tersebut baru akan dijalankan jika dan hanya jika terdapat event berupa click.


## **Penerapan *asynchronous programming* pada AJAX**
---
Pemrograman secara asinkronus pada AJAX ada saat sebuah event terjadi. Contohnya pada tugas kali ini, ketika button add task ditekan untuk membuat task baru, akan dilakukan AJAX POST untuk mengirim data ke server. Setelahnya, akan dijalankan callback function setelah server selesai mengolah data tersebut. Data yang ditangkap akan dikirimkan ke server tanpa melalui browser reload.

## **Implementasi AJAX**
---
- **AJAX GET**. Pertama, menambahkan path routing `todolist/json` pada `urls.py` untuk menghubungkan dengan function pada `views.py`. Pada `views.py` ditambahkan function `show_todolist_json` untuk mengambil task pengguna yang login dalam bentuk JSON. Saat website selesai direload, AJAX GET terpanggil untuk mendapatkan task dalam bentuk JSON.

- **AJAX POST**. Form `create task` dan  buutton `create task` yang sebelumnya redirect ke `todolist/create-task` akan diubah menjadi bentuk modal. Untuk mengimplementasikannya, pertama, menambahkan path routing `todolist/add` pada `urls.py` untuk menghubungkan function pada `views.py`. Pada `views.py`, ditambahkan function `add_task`, kemudian di function tersebut diterapkan pemrograman secara asinkronus, sehingga task  dapat terupdate tanpa reload website.