tugas = []
Nama = input("masukkan nama anda sebelum memulai sistem ini: ")
while True:
    print("===================================")
    print(" SISTEM PRIORITAS TUGAS MAHASISWA ")
    print("===================================")

    print("===================================")
    print("halo", Nama, ", selamat datang ke sistem prioritas tugas. sekarang", Nama, "mau ngapain ya?")
    print("1.Tambahin tugas kelist")
    print("2.Lihat semua tugas")
    print("3.hapus tugas ")
    print("4.Ubah list tugas")
    print("5.keluar ")

    pilihan = input("silahkan pilih menu(1-5): ")

    if pilihan == "1":
        print("--- TAMBAH TUGAS ---")

        nama = input("Masukkan tugas yang kamu ingin tambahkan: ")

        while nama == "":
            print("Nama tugas tidak boleh kosong!")
            nama = input("Masukkan nama tugas: ")

        sisa_hari = input("Berapa hari lagi deadline? ")

        while not sisa_hari.isdigit():
            print("input harus berupa angka!")
            sisa_hari = input("Berapa hari lagi deadline? ")

        sisa_hari = int(sisa_hari)

        print("skala kesulitan :")
        print("1. Sangat Mudah")
        print("2. Mudah")
        print("3. sedang")
        print("4. Sulit")
        print("5. sangat sulit")

        kesulitan = input("Masukkan skala kesulitan (1-5): ")

        while not kesulitan.isdigit() or int(kesulitan) < 1 or int(kesulitan) > 5:
            print("Skala Kesulitan harus berupa angka 1 sampai 5!")
            kesulitan = input("Masukkan skala kesulitan (1-5): ")

        kesulitan = int(kesulitan)

        if kesulitan == 1:
            tingkat = "Sangat Mudah"
        elif kesulitan == 2:
            tingkat = "Mudah"
        elif kesulitan == 3:
            tingkat = "sedang"
        elif kesulitan == 4:
            tingkat = "sulit"
        else:
            tingkat = "sangat sulit"

        if sisa_hari <= 2:
            prioritas = "Tinggi"
        elif sisa_hari <= 5 and kesulitan >= 4:
            prioritas = "Tinggi"
        elif sisa_hari <= 5:
            prioritas = "sedang"
        elif kesulitan >= 4:
            prioritas = "sedang"
        else:
            prioritas = "rendah"

        data_tugas = [
            nama,
            sisa_hari,
            kesulitan,
            tingkat,
            prioritas
        ]

        tugas.append(data_tugas)

        print("Tugas berhasil ditambahkan!")
        print("---------------------------")
        print("Nama tugas      :", nama)
        print("Sisa Hari       :", sisa_hari)
        print("Skala kesulitan :", kesulitan)
        print("Tingkat         :", tingkat)
        print("Prioritas       :", prioritas)
        print("---------------------------")

    elif pilihan == "2":
        print("------Daftar semua tugas------")

        if len(tugas) == 0:
            print("belum ada tugas yang kamu simpan. ayo mulai tambahin!")
        else:
            for i in range(len(tugas)):
                print("tugas ke-", i + 1)
                print("===================================")
                print("Nama tugas          :", tugas[i][0])
                print("Sisa hari           :", tugas[i][1])
                print("Skala kesulitan     :", tugas[i][2])
                print("Tingkat             :", tugas[i][3])
                print("Prioritas           :", tugas[i][4])

    elif pilihan == "3":
        print("===== HAPUS TUGAS =====")

        if len(tugas) == 0:
            print("belum ada tugas yang dapat dihapus.")
        else:
            for i in range(len(tugas)):
                print(i + 1, ".", tugas[i][0])

            nomor = input("pilih nomor tugas yang ingin dihapus ya, " + Nama + "! ")

            while not nomor.isdigit() or int(nomor) < 1 or int(nomor) > len(tugas):
                print("Nomor tugas tidak ada!")
                nomor = input("Pilih nomor tugas yang ingin dihapus: ")

            nomor = int(nomor)
            index = nomor - 1

            tugas_dihapus = tugas[index][0]
            tugas.pop(index)

            print("Tugas", tugas_dihapus, "berhasil dihapus!")

    elif pilihan == "4":
        print("===== UBAH TUGAS =====")

        if len(tugas) == 0:
            print("belum ada tugas yang diubah.")
        else:
            for i in range(len(tugas)):
                print(i + 1, ".", tugas[i][0])

            nomor = input("pilih nomor tugas yang ingin diubah: ")

            while not nomor.isdigit() or int(nomor) < 1 or int(nomor) > len(tugas):
                print("nomor tugas tidak tersedia!")
                nomor = input("pilih nomor tugas yang ingin diubah: ")

            nomor = int(nomor)
            index = nomor - 1

            print("====== MASUKKAN DATA BARU YA! ======")

            nama_baru = input("nama tugas baru: ")

            while nama_baru == "":
                print("Nama tugas tidak boleh kosong!")
                nama_baru = input("nama tugas baru: ")

            sisa_hari_baru = input("sisa hari baru: ")

            while not sisa_hari_baru.isdigit():
                print("input harus berupa angka!")
                sisa_hari_baru = input("sisa hari baru: ")

            sisa_hari_baru = int(sisa_hari_baru)

            print("Skala Kesulitan")
            print("1. Sangat Mudah")
            print("2. Mudah")
            print("3. sedang")
            print("4. Sulit")
            print("5. Sangat sulit")

            kesulitan_baru = input("berapa skala kesulitan tugasnya, " + Nama + "? (ketik 1-5): ")

            while not kesulitan_baru.isdigit() or int(kesulitan_baru) < 1 or int(kesulitan_baru) > 5:
                print("skala harus berupa angka 1 sampai 5!")
                kesulitan_baru = input("Skala kesulitan baru (1-5): ")

            kesulitan_baru = int(kesulitan_baru)

            if kesulitan_baru == 1:
                tingkat_baru = "sangat mudah"
            elif kesulitan_baru == 2:
                tingkat_baru = "mudah"
            elif kesulitan_baru == 3:
                tingkat_baru = "sedang"
            elif kesulitan_baru == 4:
                tingkat_baru = "sulit"
            else:
                tingkat_baru = "sangat sulit"

            
            if sisa_hari_baru <= 2:
                prioritas_baru = "Tinggi"
            elif sisa_hari_baru <= 5 and kesulitan_baru >= 4:
                prioritas_baru = "Tinggi"
            elif sisa_hari_baru <= 5:
                prioritas_baru = "Sedang"
            elif kesulitan_baru >= 4:
                prioritas_baru = "sedang"
            else:
                prioritas_baru = "rendah"

            tugas[index] = [
                nama_baru,
                sisa_hari_baru,
                kesulitan_baru,
                tingkat_baru,
                prioritas_baru
            ]

            print("Tugas Berhasil diubah! ^^")
            print("===================================")
            print("Nama Tugas      :", nama_baru)
            print("Sisa hari       :", sisa_hari_baru)
            print("Skala kesulitan :", kesulitan_baru)
            print("Tingkat         :", tingkat_baru)
            print("Prioritas       :", prioritas_baru)

    
    elif pilihan == "5":
        print("=================================================")
        print("Terima kasih", Nama, "telah menggunakan program ini!")
        print("semoga semua tugas dapat diselesaikan tepat waktu")
        print("dan mendapat nilai terbaik", Nama, "ya!")
        print("=================================================")
        break

    else:
        print("Pilihan menu tidak tersedia!")
        print("silahkan masukkan angka 1 sampai 5")