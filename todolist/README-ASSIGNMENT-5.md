# **Tugas 5 (todolist)**

-- [Deployment Link](https://assignment-2-aidahnovallia.herokuapp.com/) --

## **Perbedaan Inline, Internal, dan External CSS**
---
- **Internal CSS** merupakan kode CSS yang ditulis di dalam tag `<style>` dan kode HTML dituliskan di bagian atas (header) file HTML. Internal CSS dapat digunakan untuk membuat tampilan pada satu halaman situs web dan tidak digunakan pada halaman situs web yang lain. Internal CSS ini akan sangat cocok dipakai untuk menciptakan halaman web dengan tampilan yang berbeda. Dengan kata lain, Internal CSS ini bisa dipakai untuk menciptakan tampilan yang unik pada setiap halaman situs web. Beberapa kekurangan internal CSS antara lain tidak efisien apabila ingin menggunakan CSS yang sama dalam beberapa file. Selain itu, performa situs web lebih lambat sebab CSS yang berbeda-beda akan mengakibatkan loading ulang setiap kali  mengganti halaman situs web. 

- **Eksternal CSS** adalah kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi .css. File eksternal CSS biasanya diletakkan setelah bagian `<head>` pada halaman. Cara ini lebih sederhana dan simpel daripada menambahkan kode CSS di setiap elemen HTML yang ingin Anda atur tampilannya. Salah satu kekurangan eksternal CSS adalah halama dapat menjadi berantakan ketika file CSS gagal dipanggil oleh file HTML. Hal tersebut disebabkan oleh koneksi internet yang lambat.

- **Inline CSS** merupakan kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style, di situ lah inline CSS ditulis. Cara ini kurang efisien karena setiap tag HTML yang diberikan harus memiliki style masing-masing. Akan lebih sulit dalam mengatur situs web apabila hanya menggunakan inline style CSS. Sebab, Inline CSS digunakan hanya untuk mengubah satu elemen saja.

## **Tag HTML5 yang diketahui**
- `<p>` merupakan tag untuk membuat sebuah paragraf
- `<form>` merupakan tag untuk membuat sebuah form HTML untuk input pengguna
- `<input>` merupakan tag untuk membuat sebuah kontrol input
-  `<a>` merupakan tag untuk membuat hyperlink
- `<li>` merupakan tag untuk membuat item daftar

##  **Iipe-tipe CSS selector**
1. <u>Elemen selector</u> <br>
Jenis selector ini menggunakan nama-nama tag HTML. Pada dasarnya seluruh element tag visual HTML dapat digunakan sebagai selector. Artinya, pada setiap halaman HTML, terbuat dari konten yang ditempatkan di dalam tag HTML dan setiap set tag tersebut mewakili elemen pada halaman.

2. <u>Class selector</u> <br>
Dalam HTML nantinya akan ada tag-tag html pada umurnya memiliki atribut class. Saat memilih elemen dengan class tertentu, maka kita bisa menuliskan karakter titik (.) kemudian diikuti dengan nama class.

3. <u>ID selector</u> <br>
Salah satu atribut dalam HTML yang dapat digunakan sebagai selector adalah atribut 'id'. Nantinya, id dari elemen tersebut memiliki sifat yang unik dalam suatu laman, jadi jenis penyeleksi ini sering digunakan untuk memilih satu elemen unik. 
Biasanya, saat memilih elemen dengan id tertentu, maka ditulis dengan karakter hash (#), kemudian diikuti dengan id elemen.

## **Implementasi checklist**
