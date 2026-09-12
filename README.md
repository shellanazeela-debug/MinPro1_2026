
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
Bagan ini mengartikan jika nomor yang dimasukkan pengguna diubah menjadi integer. Kemudian dikurangi 1 karena indeks list Python dimulai dari 0. <br>

7. <img width="419" height="62" alt="image" src="https://github.com/user-attachments/assets/c37471d0-d89f-4ce3-86ec-a1bc6c685d11" /> <br>
Sebelum dihapus, nama tugas disimpan ke variabel tugas_dihapus agar dapat ditampilkan dalam pesan konfirmasi. Lalu tugas akan dihapus dengan `tugas.pop(index)`. Dan setelah selesai,sistem akan menampilkan jika tugas telah dihapus. <br>

8.Output <br>
<img width="518" height="163" alt="Screenshot 2026-09-12 140117" src="https://github.com/user-attachments/assets/86ec5c9e-d295-430a-9cde-358c60d1592e" /> <br>


======== PEMBAHASAN MENU KEEMPAT: UBAH HAPUS TUGAS ========<br>
1.<img width="281" height="37" alt="Screenshot 2026-09-12 144707" src="https://github.com/user-attachments/assets/db396be8-c7ee-43a9-943d-fe12b3994376" /> <br>
Pada bagian ini, akan berjalan Jika pengguna memilih menu nomor 4, program menjalankan proses untuk mengubah data tugas yang sudah tersimpan. <br>

2. <img width="342" height="35" alt="image" src="https://github.com/user-attachments/assets/92e0f0c9-8838-4c13-8059-61188909bec7" /> <br>
Pada bagian ini, Program memeriksa apakah terdapat tugas yang dapat diubah. Jika list kosong, program memberikan informasi kepada pengguna yaitu "belum ada tugas yang diubah." <br>

3. <img width="332" height="41" alt="image" src="https://github.com/user-attachments/assets/ddf9b2c8-9808-4eb7-bd50-07373761b540" /> <br>
Untuk bagian ini,Jika terdapat tugas, program menampilkan daftar tugas beserta nomor urutnya. Pengguna kemudian dapat menentukan tugas mana yang ingin diubah.<br>

4. <img width="545" height="77" alt="Screenshot 2026-09-12 145450" src="https://github.com/user-attachments/assets/1970a668-df92-4bc1-8cbd-ecadadaeee80" /> <br>
Bagian ini, Program meminta pengguna memasukkan nomor tugas yang ingin diedit. Setelah itu program akan melakukan validasi yang digunakan untuk memastikan nomor yang dimasukkan merupakan angka dan berada dalam daftar tugas yang tersedia. Dan ketika pengguna memasukkan nilai yang tidak tersedia, program akan menampilkan pesan "nomor tugas tidak tersedia!".<br>

5.<img width="230" height="35" alt="Screenshot 2026-09-12 150605" src="https://github.com/user-attachments/assets/cd1ffb39-dd36-463f-b1b9-586c82592252" /> <br>
Pada bagian ini, Nomor tugas diubah menjadi integer kemudian dikurangi satu untuk menyesuaikan dengan indeks list Python.<br>

6.<img width="452" height="323" alt="Screenshot 2026-09-12 150751" src="https://github.com/user-attachments/assets/becfcd73-daf5-4d50-9b84-325c301166f7" /> <br>
Pertama program akan meminta user untuk melakukan penginputan nama tugas baru sebagai pengganti dari tugas sebelumnya. Setelah itu program akan melakukan validasi nama tugas. Program akan memeriksa apakah pengguna memasukkan nama kosong.
Jika nama_baru == "", program menampilkan pesan bahwa nama tugas tidak boleh kosong dan meminta pengguna memasukkan nama kembali. Setelahnya, Program meminta pengguna memasukkan jumlah hari yang tersisa sebelum deadline yang baru. Nilai tersebut disimpan dalam variabel sisa_hari_baru. Dan akan melakukan sistem validasi apakah kode yang digunakan merupakan huruf atau angka. Dan harus angka. Setelah input dipastikan berupa angka, nilai tersebut diubah dari string menjadi integer menggunakan int().Setelah itu, bagian ini menampilkan pilihan tingkat kesulitan tugas dari skala 1 sampai 5. Pengguna dapat menentukan tingkat kesulitan tugas yang baru berdasarkan pilihan tersebut.<br>.

7.<img width="647" height="105" alt="Screenshot 2026-09-12 152252" src="https://github.com/user-attachments/assets/9f2f98e0-f485-47d1-9f1c-239dbd3a6e1a" /> <br>
-Program pertama Kode ini digunakan untuk meminta pengguna memasukkan skala kesulitan baru dari tugas yang sedang diubah. Input disimpan dalam variabel kesulitan_baru. 
-Setelah itu, ia akan memvalidasi input. Perulangan akan berjalan jika pengguna memasukkan data yang tidak sesuai, yaitu Input bukan berupa angka, angka yang dimasukkan kurang dari 1 , angka yang dimasukkan lebih dari 5. Jika input tidak valid, program menampilkan pesan kesalahan dan meminta pengguna memasukkan skala kesulitan kembali. Proses ini akan terus berulang sampai pengguna memasukkan angka dari 1 hingga 5.
-Dan terakhir, dalam code `kesulitan_baru = int(kesulitan_baru)` nilai kesulitan_baru diubah dari tipe data string menjadi integer menggunakan int().<br>

8.<img width="437" height="317" alt="Screenshot 2026-09-12 154922" src="https://github.com/user-attachments/assets/c7c93be1-3720-43b9-a033-1b87a03c5c08" /><br>
- pada bagan awal, Bagian ini memiliki fungsi yang sama dengan penentuan tingkat kesulitan pada menu tambah tugas, tetapi menggunakan variabel yang baru diinput pengguna sebagai pengganti tugas. Tujuannya adalah menentukan keterangan tingkat kesulitan berdasarkan skala yang baru dimasukkan pengguna.
- Setelah deadline dan kesulitan diperbarui, program menghitung ulang prioritas tugas. Hal ini penting karena perubahan deadline atau tingkat kesulitan dapat menyebabkan prioritas tugas berubah. Contohnya, tugas yang sebelumnya memiliki prioritas rendah dapat berubah menjadi tinggi apabila deadline-nya diubah menjadi tinggal satu hari. (baikin lagi semua dibawah)

9.<img width="260" height="105" alt="Screenshot 2026-09-12 155706" src="https://github.com/user-attachments/assets/90a97930-16a9-47f5-ba12-b957d09137d1" /> <br>
Bagian ini digunakan untuk mengganti seluruh data tugas lama dengan data baru. Berbeda dengan append(), kode ini tidak menambahkan tugas baru. Data pada posisi indeks tertentu justru diganti dengan informasi terbaru. <br>

10.<img width="426" height="105" alt="Screenshot 2026-09-12 155832" src="https://github.com/user-attachments/assets/f91d97c4-7916-4bbd-8e0e-b7693938f2dd" /> <br>
Bagian ini digunakan untuk mengganti seluruh data tugas lama dengan data baru. Berbeda dengan append(), kode ini tidak menambahkan tugas baru. Data pada posisi indeks tertentu justru diganti dengan informasi terbaru. <br>

11.<img width="474" height="106" alt="Screenshot 2026-09-12 155951" src="https://github.com/user-attachments/assets/9a2b6b65-864e-4eb0-84f1-cf4cb3db1485" /> <br>
Bagian ini memberikan konfirmasi bahwa tugas berhasil diperbarui. Program juga menampilkan seluruh data terbaru agar pengguna dapat memastikan bahwa perubahan telah tersimpan. Perintah break digunakan untuk menghentikan while True. Tanpa break, menu akan terus berjalan tanpa batas.<br>

12<img width="404" height="53" alt="Screenshot 2026-09-12 160106" src="https://github.com/user-attachments/assets/41a9c03c-3c75-4a99-8c7e-d0d7ab318094" /> <br> 
Blok else dijalankan apabila pengguna memasukkan pilihan selain "1", "2", "3", "4", atau "5". Program tidak langsung berhenti, tetapi memberikan pesan kesalahan. Setelah itu, karena masih berada di dalam while True, program kembali menampilkan menu utama dan pengguna dapat mencoba memasukkan pilihan yang benar. <br>





















    






















