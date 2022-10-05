# **Tugas 4 (todolist)**

-- [Deployment Link](https://assignment-2-aidahnovallia.herokuapp.com/) --

## **Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?**
---
CSFR(Cross Site Request Forgery) yang juga dikenal sebagai “Session Riding” atau “One-Click Attack” merupakan jenis serangan berbahaya terhadap penggunaan aplikasi web. Salah satu metode terbaik untuk menghindari CSFR adalah dengan menggunakan token (CSFR token) yang sering berubah alih-alih bergantung pada *session cookies* untuk menjalankan perubahan status pada server. Tanpa `{% csrf_token %}`, input akan gagal diverifikasi sehinggal menyebabkan error setelah meng-*submit* form.

<br>

## **Bagaimana membuat form secara manual**
---
Form dapat kita buat secara manual tanpa menggunakan generator, yaitu dengan menambahkan elemen `<form>`. Elemen `<form>` dapat kita isi dengan elemen `<input>` sesuai dengan kebutuhan. Terakhir, jangan lupa menambahkan `<input type='submit>` untuk meng-*submit* isi dari form tersebut.

<br>

## **Implementasi *checklist***
---
1. Membuat aplikasi `todolist` dengan menjalankan perintah `python manage.py startapp todolist`.
2. Menambahkan path `path('todolist/', include('todolist.urls'))` pada urls.py pada `project_django` untuk mengubungkan `urlpatterns` `urls.py` pada `project_django` dengan `urls.py` pada `todolist`.
3. Membuat model data `Task` pada `todolist/models.py` dengan fields `user`, `date`, `title`, `description`, dan `is_finished`.
4. Membuat file template `login.html` dan `register.html` yang akan ditampilkan saat user login dan register. Setelah itu, tambahkan function `register`, `login_user`, dan `logout_user` pada `todolist/views.py` untuk mengatur *logic* register, login, dan logout.
5. Membuat template `todolist_home.html` yang akan ditampilkan saat user sudah login.Setelah itu, menambahkan function `show_todolist` pada `todolist/views.py` untuk mengatur *logic* data yang akan ditampilkan sesuai dengan user yang login.
6. Membuat template `create_task.html` yang akan ditampilkan saat user membuat Task baru. Setelah itu, menambahkan function `create_task` pada `todolist/views.py` untuk mengatur *logic* pembuatan Task baru.
7. Menambahkan pattern path-path pada `todolist/urls.py` untuk menghubungkan dengan seluruh function pada `todolist/views.py`.
8. Proses deployment ke Heroku berjalan secara otomatis dengan meng-*push* pekerjaan kita ke repository Github yang terhubung dengan aplikasi di Heroku.
9. Pada deployment Heroku, register 2 akun dan menambahkan 3 Task pada masing-masing akun.
