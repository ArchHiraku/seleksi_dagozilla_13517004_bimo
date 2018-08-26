# Take Home Test Seleksi Calon Kru Programming Dagozilla 2018

Mengandung hasil pengerjaan Take Home Test Seleksi Calon Kru Programming Dagozilla 2018 oleh Bimo Adityarahman Wiraputra, 13517004/16517346.  
Folder _source_ mengandung _file_ [minesweeper.cpp][mi] dan [sudoku.py][su].

### Problem 1 : Obstacle Avoidance

Menurut saya, pertama-tama robot memasukkan data posisi rintangan di lapangan berdasarkan gambar yang didapat, lalu robot menentukan rute dari posisi dia berada ke posisi yang diinginkan dengan beberapa parameter, seperti jarak terdekat dan cukup jauh dari rintangan yang ada. Sambil berjalan, robot terus memasukkan/mengupdate data posisi rintangan di lapangan dari gambar yang dia dapat. Jika ternyata rute yang dimiliki sudah menjadi tidak valid, seperti muncul rintangan di rute, maka robot akan menghitung ulang rute baru yang memenuhi. Hal ini dilakukan sampai robot mencapai posisi yang diinginkan.

Beberapa ide yang dapat memperbagus algoritma di atas adalah apabila robot dapat memprediksi posisi rintangan yang bergerak, atau menggunakan gabungan data dari robot-robot lain apabila ada.

### Problem 2 : Algoritma program [sudoku.py][su]

Saat dijalankan sebagai program utama, dengan menuliskan di _command line_ "sudoku.py problx solnx", progam sudoku akan membaca kondisi _board_ mula-mula di _file_ problx, menyelesaikannya dengan menjalankan fungsi _solve_sudoku_, dan mengoutputkan jawaban yang valid, apabila ditemukan, ke layar dan ke _file_ solnx

Algoritma di dalam _solve_sudoku_ bekerja dengan cara _bruteforce_, pertama mencari suatu kotak yang belum diisi, lalu mencoba mengisikannya dengan kemungkinan bilangan yang valid, yaitu bilangan yang belum pernah muncul sebelumnya di baris, kolom, atau blok yang sama dengan kotak kosong tersebut. Hasil _board_ nya akan dimasukan kembali ke dalam fungsi _solve_sudoku_, dimana fungsi akan berhenti apabila ditemukan solusi _board_ yang valid, atau mencoba kemungkinan bilangan lain yang dimasukkan ke kotak tersebut, sampai pada akhirnya solusi yang valid ditemukan atau semua kemungkinan pengisian _board_ sudah dicoba dan tidak ditemukan solusi yang memenuhi.

Remark : saya rasa akan lebih baik apabila program pertama mengecek bahwa input _board_ di probx valid terlebih dahulu.

### Problem 3 : Alur program [minesweeper.cpp][mi]

Pertama, program minesweeper menerima inputan nilai N dan B dari pemain, yaitu dimensi _board_ dan banyak bom yang ada berturut-turut. Lalu program menginisialisasikan _board_ dengan memilih secara acak B buah kotak untuk sebagai kotak yang mengandung bom (hal ini dilakukan dengan mempermutasikan array bilangan dari 0 sampai banyak kotak - 1, masing-masing menandakan satu kotak di _board_, lalu memilih B bilangan pertama di array dimana kotaknya akan diberikan bom. Kotak-kotak yang tidak mengandung bom akan menyimpan nilai yang menandakan banyak bom di sekitarnya.

Program akan terus mengoutput keadaan _board_ dimana kotak yang belum dibuka/tereksplor bertanda '*', yang sudah dibuka dan mengandung bom bertanda 'x', dan sisanya bertanda angka yang menandakan banyak bom di sekitarnya. Pada awalnya semua kotak belum dibuka. Lalu pemain diminta untuk memilih untuk memilih kotak untuk dibuka. Kotak yang dipilih dan kotak yang bersebelahan dengan kotak bernilai 0 yang dibuka akan dibuka. Permainan akan terus berlanjut sampai pemain membuka semua kotak selain kotak yang mengandung bom dimana pemain menang, atau pemain membuka bom dimana pemain kalah.

Remark : Agak aneh bahwa program mengoutput kotak lokasi bom disimpan saat inisialisasi board.


[mi]: https://github.com/ArchHiraku/seleksi_dagozilla_13517004_bimo/blob/master/source/minesweeper.cpp
[su]: https://github.com/ArchHiraku/seleksi_dagozilla_13517004_bimo/blob/master/source/sudoku.py
