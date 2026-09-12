
NAMA : SHELLA NAZEELA SAPUTRA <br>
NIM : 2609116018 <br>
KELAS : A <br>

PENJELASAN MINI PROJECT DENGAN TEMA " 'Sistem untuk Menentukan Prioritas Tugas Mahasiswa' "<br>
<br>
<br>
 <img width="116" height="17" alt="Screenshot 2026-09-12 114728" src="https://github.com/user-attachments/assets/dd3ecd48-e67f-456e-b246-bee9b0e5341b" /> <br>
kode tersebut digunakan untuk membuat sebuah list kosong bernama tugas. List ini berfungsi sebagai tempat penyimpanan sementara seluruh data tugas yang dimasukkan oleh pengguna selama program berjalan.<br>

<img width="398" height="15" alt="image" src="https://github.com/user-attachments/assets/87c16d4b-d3f2-4407-a94f-11da6036f695" /> <br>
Bagian ini menggunakan fungsi input() untuk meminta pengguna memasukkan nama sebelum menggunakan sistem. <br>

<img width="331" height="21" alt="Screenshot 2026-09-12 115838" src="https://github.com/user-attachments/assets/d59e15b6-40bd-4ba6-978c-8476a9558d92" /> <br>
Kode while True digunakan untuk membuat perulangan tanpa batas pada program. yang dimana, menu utama akan terus ditampilkan dan pengguna dapat melakukan berbagai aktivitas seperti menambah, melihat, menghapus, atau mengubah tugas.<br>

<img width="655" height="107" alt="Screenshot 2026-09-12 120047" src="https://github.com/user-attachments/assets/244faad8-c7cb-46bf-9350-0d3636bff248" /> <br>
kode diatas digunakan untuk membuat menu tampilan yang dimana akan mempermudah user untuk menjalankan perintah. Variabel Nama digabungkan dengan teks menggunakan beberapa argumen pada print(). Tujuannya agar program terasa lebih interaktif dan personal.Menu tersebut nantinya akan diproses menggunakan conditional statement if, elif, dan else.<br>

<img width="347" height="16" alt="Screenshot 2026-09-12 120219" src="https://github.com/user-attachments/assets/3c821538-bbcd-4f1c-a103-4c8f692d42dd" /> <br>
Kode ini digunakan untuk menerima pilihan menu dari pengguna berdasar pilihannya diblok atas. Input disimpan dalam variabel pilihan. <br>

======== PEMBAHASAN MENU PERTAMA : MENAMBAH TUGAS ========<br>
1. <img width="273" height="34" alt="Screenshot 2026-09-12 120835" src="https://github.com/user-attachments/assets/237b4d0d-5977-4e6f-9107-5fe91ad6ad56" /> <br>
Conditional statement `if pilihan == "1":` digunakan untuk mengecek apakah pengguna memilih menu nomor 1. Jika nilai pilihan adalah "1", maka seluruh kode di dalam blok tersebut akan dijalankan. Jika tidak, , maka blok ini tidak akan berjalan.Dan juga code print `("--- TAMBAH TUGAS ---")` <br>

2.<img width="359" height="81" alt="Screenshot 2026-09-12 121316" src="https://github.com/user-attachments/assets/1a49d9db-7257-4d31-b6ab-23d56770c3d1" /> <br>
Untuk baris pertama, program meminta pengguna memasukkan nama atau deskripsi tugas dengan menggunakan fungsi input. Di lanjutkan dengan menggunakan while untuk memastikan pengguna tidak memasukkan nama tugas kosong. Jika nama == "", berarti pengguna tidak memasukkan teks apa pun. Program kemudian memberikan pesan kesalahan dan meminta pengguna memasukkan nama tugas kembali. <br>

3. <img width="405" height="104" alt="Screenshot 2026-09-12 121616" src="https://github.com/user-attachments/assets/6e21e364-e74a-4ab1-8f5f-2ba40929bb6c" /> <br>
Baris pertama meminta pengguna memasukkan jumlah hari yang tersisa sebelum tugas memiliki deadline dan akan dimasukkan kedalam variable `sisa_hari` . Baris kedua digunakan untuk memastikan bahwa sisa hari yang dimasukkan benar-benar berupa angka. `isdigit()` digunakan untuk memeriksa apakah isi string hanya terdiri dari angka. Kata not berarti kondisi akan dijalankan jika input bukan angka. Dan untuk baris `sisa_hari = int(sisa_hari)` digunakan ketika Setelah dipastikan bahwa input hanya berisi angka, data tersebut diubah dari string menjadi integer menggunakan int(). <br>

4.<img width="449" height="118" alt="Screenshot 2026-09-12 122221" src="https://github.com/user-attachments/assets/efb5fb26-8006-4477-990b-6463a1a0a006" /> <br>
Bagian ini memberikan pengguna sebuah pilihan tingkat kesulitan tugas dari 1 sampai 5. Selain itu untuk blok selain print,Blok ini digunakan untuk mengInput pilihan pengguna yang akan disimpan dalam variabel kesulitan. <br>

5. <img width="543" height="40" alt="Screenshot 2026-09-12 122601" src="https://github.com/user-attachments/assets/8cee3a88-af7b-4e6c-8045-ad68224c4482" /> <br>
Bagian ini melakukan beberapa pemeriksaan sekaligus. Input akan menjadi tidak valid ketika input tersebut bukan angka,angkanya kurang dari 1, dan angkanya lebih dari 5. Operator or digunakan karena cukup satu kondisi saja yang terpenuhi untuk membuat input dianggap tidak valid. Lalu blok `print` dibaris kedua meminta user untuk mengisi ulang beserta dilanjutkannya blok ke-3 untuk user memasukkan ulang dengan yang baru. <br>

6.<img width="297" height="178" alt="Screenshot 2026-09-12 123100" src="https://github.com/user-attachments/assets/b22b3ea2-0526-4c7d-98ae-f138a9d73992" /> <br>
Dibaris pertama, ketika input dinyatakan valid, nilai kesulitan diubah menjadi integer agar dapat digunakan dalam proses perbandingan. Selankjutnya akan menggunakan Conditional statement digunakan agar program dapat menentukan teks berdasarkan angka yang dimasukkan pengguna.<br>

7.<img width="323" height="149" alt="image" src="https://github.com/user-attachments/assets/5fe03f9e-5db2-4914-900d-46e7b52ec3aa" /> <br>
Bagian ini merupakan logika utama sistem prioritas. Program menentukan prioritas berdasarkan dua faktor, yaitu: Sisa hari deadline dan juga tingkat kesulitan tugas. Aturan yang digunakan yaitu ketika sisa hari semakin sedikit dan tingkat kesulitan tugas semakim besar, maka tugas akan menjadi prioritas utama.Operator and digunakan ketika dua kondisi harus terpenuhi secara bersamaan. <br>

8.<img width="230" height="103" alt="Screenshot 2026-09-12 123646" src="https://github.com/user-attachments/assets/e16c8d25-2d1d-4efa-9b42-8ad8499fdbfb" /> <br>
Bagian ini membuat sebuah list baru bernama data_tugas. List ini berisikan data-data yang didapatkan dari code-code diatas yang secara tidak langsung meminta data kepada pengguna untuk membuat list ini.<br>

9.<img width="344" height="148" alt="Screenshot 2026-09-12 123902" src="https://github.com/user-attachments/assets/03e07027-20a4-4598-b5a3-e5016936d8f2" /> <br>
Untuk baris pertama, Fungsi append() digunakan untuk memasukkan data_tugas ke dalam list tugas. Selanjutnya untuk deretan print diatas digunakan untuk menampilkan data yang baru saja dimasukkan dan hasil prioritas yang diberikan sistem.<br>

10. Output : <br>
<img width="380" height="238" alt="Screenshot 2026-09-12 124222" src="https://github.com/user-attachments/assets/78fd547a-c7d8-4437-ba4a-0ed4dd313a89" /> <br>

======== PEMBAHASAN MENU KEDUA : MENAMBAH TUGAS ========<br>
1. <img width="326" height="34" alt="Screenshot 2026-09-12 124525" src="https://github.com/user-attachments/assets/88dead10-ac03-4e83-8785-b9ed57ada136" /> <br>
Jika pengguna memilih menu nomor 2, program menjalankan blok untuk menampilkan seluruh tugas yang tersimpan. Selain itu blok `print("------Daftar semua tugas------")` digunakan sebagai tampilan kepada pengguna agar mereka mengetahui jika mereka sedang membuka menu daftar semua tugas. <br>

2.<img width="398" height="33" alt="Screenshot 2026-09-12 124833" src="https://github.com/user-attachments/assets/3138b7b3-7444-4661-841a-101d0ee32ac0" /> <br>
Fungsi len() digunakan untuk menghitung jumlah data di dalam list tugas. Jika hasilnya 0, berarti belum ada tugas yang tersimpan dan sistem akan memperingatkannya melalui code `print("belum ada tugas yang kamu simpan. ayo mulai tambahin!")` <br>

3.<img width="429" height="132" alt="Screenshot 2026-09-12 125056" src="https://github.com/user-attachments/assets/7fbdec26-6371-4bb5-affc-c3a20434a370" /> <br>
Jika list tidak kosong, program menggunakan perulangan for untuk mengakses setiap tugas. range(len(tugas)) digunakan untuk menghasilkan nomor indeks berdasarkan jumlah tugas. Selanjutnya untuk barisan print berfungsi sebagai penggunakan indeks untuk mengambil informasi tertentu dari setiap tugas. <br>.

4.OUTPUT <BR>
    <img width="273" height="196" alt="Screenshot 2026-09-12 125558" src="https://github.com/user-attachments/assets/73c4b684-4a26-481f-a322-2bd5ae62c185" /> <br>.

======== PEMBAHASAN MENU KETIGA : HAPUS TUGAS ========<br>
1. <img width="293" height="30" alt="Screenshot 2026-09-12 132326" src="https://github.com/user-attachments/assets/7da278d8-b731-4491-ace4-4fcace4fa6ed" /> <br>
Jika pengguna memilih menu nomor 3, program menjalankan proses untuk menghapus tugas. Dan sistem akan menampilkan tampilan jika menu menghapus tugas terpilih. <br>

2.<img width="380" height="29" alt="Screenshot 2026-09-12 132736" src="https://github.com/user-attachments/assets/29b3dbb1-31d3-411c-8a6b-506892aea2c3" /> <br>
Program diatas berfungsi memeriksa apakah list tugas kosong. Jika tidak ada tugas, proses penghapusan tidak dapat dilakukan dan akan menampilkam pesan "belum ada tugas yang dapat dihapus." <br>

3.<img width="329" height="52" alt="Screenshot 2026-09-12 133457" src="https://github.com/user-attachments/assets/3e72cb30-777c-457f-8476-db283e703aa4" /> <br>
Dalam bagan ini, Jika terdapat tugas, program menampilkan seluruh nama tugas beserta nomor urutnya. `i + 1` digunakan karena indeks Python dimulai dari 0, sedangkan nomor yang ditampilkan kepada pengguna lebih mudah dimulai dari 1. <br>

4.<img width="562" height="21" alt="Screenshot 2026-09-12 133756" src="https://github.com/user-attachments/assets/dcf41b06-6f0c-4561-b263-53177772abad" /> <br>
Pengguna diminta memasukkan nomor tugas yang ingin dihapus. <br>

5.<img width="526" height="46" alt="Screenshot 2026-09-12 133936" src="https://github.com/user-attachments/assets/3adf756d-1e12-4d40-8134-7cbfe44da981" /> <br>
Program memastikan nomor yang dimasukkan berupa angka yang tidak kurang dari 1 namun tidak lebih besar dari jumlah tugas yang tersedia. AKan tetapi, jika tidak valid, pengguna diminta memasukkan nomor kembali. Setelah itu sistem akan memperingatkan pengguna jika nomor yang dimasukkan tidak ada dengan code print. <br>

6.<img width="239" height="32" alt="Screenshot 2026-09-12 134137" src="https://github.com/user-attachments/assets/d56e28aa-79eb-401e-9d7a-ed01906673f6" /> <br>
Bagan ini mengartikan jika nomor yang dimasukkan pengguna diubah menjadi integer. Kemudian dikurangi 1 karena indeks list Python dimulai dari 0.












    






















