Tugas 2 :
Link pws : https://philip-halomoan-tokopakdika77.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawaban :
- Hal pertama yang saya lakukan adalah mebuat repositori lokal dengan nama yang telah saya pikirkan yaitu "tokopakdika." 
- Setelah itu saya mengikuti tahap-tahap dari tutorial 0 dengan membuat virtual environment dan melakukan startproject terhadap "tokopakdika"
- Setelah itu saya menambahkan main dengan startapp
- Setelah itu agar proyek main dapat dimasukan, saya melakuka konfigurasi program dengan menambahkan main pada installed_apps yang ada pada settings
- Setelah itu saya mengubah isi dari models.py yang sudah ada di dalam main dengan atribut-atribut yang wajib ada seperti nama, deskripsi dan stok yang dijadikan dalam satu model bernama product
- Setelah itu saya melakukan konfigurasi routing agar bisa menjalankan main dengan cara membuka urls.py yang berada di direktori terluar/direktori utama, melakukan import lalu memasukan main.urls pada urlpatterns
- Setelah membuat product saya melakukan routing aplikasi main dengan mengubah bagian urls.py yang ada di dalam direktori main agar memiliki pattern atau urlpatterns pada main yaitu show_main.
- Setelah itu saya menambahkan pada bagian views.py yaitu isi dari show_main berupa data-data yaitu nama aplikasi, nama saya dan kelas saya.
- Setelah itu langkah akhir terhadap program yaitu melakukan deploy. Saya membuat project baru pada PWS. Setelah itu saya menghubungkan antara direktori lokal dengan projek di PWS dengan menambahkan remote dengan url link dari projek PWS. 
- Setelah itu saya menambahkan url deployment PWS pada allowed_hosts yang ada di settings.py. Setelah itu saya melakukan push direktori tokopakdika pada github dan PWS
- Sebagai tugas terakhir saya menambahkan file README.md pada direktori utama tokopakdika dan menjawab pertanyaan-pertanyaan.

2.Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Jawaban :

Versi visual : https://drive.google.com/file/d/1Ae5AaFi0FKfPuzXu9SvfTkHpxbJ2TE0l/view?usp=sharing

Client Request --> urls.py --> views.py --> models.py --> Template (HTML) --> Client Response

- Client Request:
Klien mengirimkan permintaan HTTP (seperti GET atau POST) ke server. Permintaan ini dapat berupa permintaan halaman web, data, atau tindakan tertentu pada aplikasi.

- urls.py:
urls.py adalah modul yang memetakan URL yang diminta klien ke fungsi tampilan (view function) tertentu di views.py. Ketika permintaan klien datang, Django mencari pola URL yang sesuai dalam urls.py.

- views.py:
views.py berisi fungsi tampilan yang menangani logika aplikasi. Fungsi ini akan menerima permintaan yang cocok dengan pola URL dari urls.py.
Fungsi tampilan dapat melakukan beberapa hal seperti memproses data yang dikirimkan pengguna, mengakses atau memperbarui data dalam database melalui models.py, dan menyiapkan data yang akan ditampilkan kepada pengguna.

- models.py:
models.py mendefinisikan struktur data dan menyediakan API untuk berinteraksi dengan database. Fungsi tampilan (views.py) dapat menggunakan model untuk mengakses, menyimpan, memperbarui, atau menghapus data dari database.

- Template (HTML):
Setelah logika dalam views.py diproses dan data siap untuk ditampilkan, views.py akan merender template HTML. Template ini menggunakan file HTML dengan variabel dan logika template yang ditulis menggunakan sintaks Django Template Language (DTL).

- Client Response:
Django mengirimkan respons kembali ke klien, yang biasanya berupa halaman HTML yang dirender berdasarkan template. Respons ini kemudian ditampilkan kepada pengguna di browser.

3.Jelaskan fungsi git dalam pengembangan perangkat lunak!
Jawaban :
- Melihat Riwayat Perubahan: Kita dapat melihat riwayat perubahan yang lengkap dan siapa yang membuat perubahan tersebut. 
- Mengembalikan ke Versi Sebelumnya: Jika terjadi kesalahan atau bug pada kode, kita dapat dengan mudah mengembalikan (revert) ke versi sebelumnya.
- Branching dan Merging: Pengembang dapat membuat cabang baru dari cabang utama sehingga kita dapat mengembangkan fitur baru atau melakukan perbaikan tanpa mengangu bagian-bagian kode yang sudah benar. Setelah selesai, cabang tersebut dapat digabungkan (merged) kembali ke cabang utama. Ini memungkinkan pengembangan paralel dan meminimalkan konflik.
- Resolusi Konflik: Ketika beberapa pengembang mengubah bagian yang sama dari kode secara bersamaan, Git membantu mendeteksi dan menyelesaikan konflik yang mungkin terjadi ketika menggabungkan kode tersebut.
- Komit : Setiap perubahan dapat diberi pesan komit yang mendeskripsikan apa yang diubah dan mengapa. Ini membuat riwayat proyek lebih mudah dipahami.
- Tagging: Git memungkinkan pemberian tag pada versi tertentu, misalnya untuk menandai rilis versi produk. Ini memudahkan untuk mengidentifikasi titik tertentu dalam riwayat proyek.
- Integrasi Berkelanjutan (CI): Banyak alat CI/CD (Continuous Integration/Continuous Deployment) yang terintegrasi dengan Git untuk secara otomatis menguji dan menggabungkan perubahan kode saat komit baru dibuat. 
- Review Kode: Git memungkinkan pengembang untuk membuat pull request atau merge request, yang bisa di-review oleh anggota tim lain sebelum digabungkan ke cabang utama. Ini memastikan bahwa kode yang ditambahkan telah diperiksa untuk kualitas dan kepatuhan terhadap standar kode.
- Repositori Lokal dan Remote: Setiap pengembang memiliki salinan lengkap dari repositori di mesin lokalnya, memungkinkan pengembangan offline. Perubahan dapat di-push atau di-pull ke dan dari repositori remote kapan saja.
- Cloning: Pengembang dapat membuat salinan repositori utama untuk percobaan atau pengembangan lebih lanjut tanpa memengaruhi repositori utama.
- Dokumentasi Bersama: Selain kode, Git dapat digunakan untuk melacak perubahan pada dokumentasi proyek, seperti README, panduan instalasi, atau catatan rilis.
- Manajemen Rilis: Dengan menggunakan cabang dan tag, tim pengembang dapat mengelola rilis perangkat lunak dengan lebih baik, memastikan stabilitas dan kompatibilitas kode.
- Integrasi dengan Tools DevOps: Banyak alat seperti Jenkins, GitHub Actions, GitLab CI/CD, dan lainnya yang secara otomatis dapat memicu build, pengujian, atau penerapan (deployment) berdasarkan perubahan dalam repositori Git.
- Pipeline Build Otomatis: Git memungkinkan otomatisasi proses build, uji, dan deployment, yang meningkatkan efisiensi dan kecepatan pengembangan perangkat lunak.

4.Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Jawaban :
Menurut saya pribadi ada beberapa alasan mengapa framework Django dipilih sebagai framework permulaan seperti:
- Django memiliki banyak fitur bawaan yang dapat memudahkan tugas kita seperti fitur admin interface yang memudahkan pengelolaan data, ORM yang memungkinkan kita bisa mengaskses databse mengunakan python tanpa harus menulis SQL, dan Routing URL yang sangat mudah untuk mendefinisikan URL. Diatas ini adalah beberapa fitur yang saya sudah tau kegunaanya.
- Django sudah memiliki dokumentasi yang lengkap seperti langkah-langkah, referensi, dan juga contoh kode, sehingga kita sebagai pemula dapat mudah memahami dan mengunakannya.
- Django sudah menjadi framework yang populer, sehingga untuk mengetahui dan memperdalam mengenai Django sudah sangat mudah menemukan tutorial, forum, atau artikel yang membahasnya.
- Django sangat mudah untuk di deploy, seperti dengan adanya manage.py yang mempermudah manajemen aplikasi.
- Django menerapkan best practices untuk pengembangan aplikasi web, seperti menggunakan pola arsitektur MVC (Model-View-Controller) yang dikenal sebagai MTV (Model-Template-View) dalam konteks Django.
- Django dibangun dengan fokus kuat pada keamanan. Framework ini membantu pemula untuk menghindari kesalahan keamanan umum, seperti serangan XSS (Cross-Site Scripting), CSRF (Cross-Site Request Forgery), SQL Injection, dan lainnya. Dengan perlindungan ini, kita sebagai pemula dapat lebih percaya diri dalam membuat aplikasi yang aman.

5.Mengapa model pada Django disebut sebagai ORM?
Jawaban :
Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena menggunakan teknik pemetaan objek untuk berinteraksi dengan basis data yang berelasi. ORM memungkinkan developer untuk bekerja dengan database menggunakan konsep-konsep pemrograman berorientasi objek, daripada menggunakan bahasa SQL langsung untuk manipulasi data.

Tugas 3 :
1. Data delivery adalah proses pengiriman dan penerimaan data antara berbagai komponen di dalam sebuah platform, misalnya antara server dengan client, atau antar layanan mikro. Dalam pengimplementasian sebuah platform, data delivery diperlukan karena beberapa alasan:

- Interoperabilitas: Aplikasi atau platform umumnya terdiri dari berbagai komponen yang mungkin berjalan di server yang berbeda, ditulis dalam bahasa pemrograman yang berbeda, atau dijalankan di perangkat yang berbeda. Data delivery memastikan komunikasi yang efektif antara komponen-komponen ini.

- Konsistensi Data: Data delivery memastikan bahwa data yang diterima oleh semua komponen platform adalah sama dan terkini. Hal ini penting agar aplikasi atau platform berjalan dengan baik tanpa adanya konflik data.

- Efisiensi dan Skalabilitas: Sistem yang mendukung data delivery memungkinkan komunikasi yang efisien, baik secara sinkron maupun asinkron. Ini penting untuk aplikasi berskala besar yang melibatkan banyak pengguna atau memiliki alur data yang kompleks.

2. JSON umumnya lebih baik dan populer dalam pengembangan web modern karena beberapa alasan:

- Sintaks yang Lebih Ringkas: JSON memiliki struktur yang lebih sederhana dan lebih mudah dibaca oleh manusia dibandingkan XML. Hal ini membuat JSON lebih ringan dan lebih cepat untuk diproses, baik oleh server maupun klien.

- Pengikatan Lebih Baik dengan JavaScript: JSON adalah format data asli JavaScript. Jadi, pada aplikasi web modern, terutama yang menggunakan JavaScript di frontend, JSON dapat langsung diproses tanpa parsing yang rumit.

- Ukuran Lebih Kecil: JSON cenderung menggunakan lebih sedikit karakter dibandingkan XML, yang berarti pengiriman data melalui jaringan lebih efisien karena ukuran payload lebih kecil.

- Popularitas pada RESTful API: JSON sangat populer digunakan dalam RESTful API karena sifatnya yang ringan dan mudah diproses di berbagai platform dan bahasa pemrograman.

3. Di Django, method is_valid() pada form digunakan untuk memvalidasi data yang dikirimkan ke form. Metode ini melakukan hal-hal berikut:

- Validasi Data: Mengecek apakah data yang dikirimkan ke form memenuhi kriteria validasi yang ditentukan di form (misalnya apakah field tertentu bersifat wajib, atau apakah data mengikuti format yang benar, seperti email yang valid).

- Membersihkan Data: Jika form valid, method ini juga membersihkan data, mengonversi tipe data yang diinput agar sesuai dengan tipe yang diharapkan.

Jika is_valid() mengembalikan True, artinya data dalam form valid dan siap untuk diproses (misalnya untuk disimpan ke database). Jika mengembalikan False, artinya ada kesalahan pada input pengguna dan biasanya Django akan memberikan pesan kesalahan yang relevan.

4. Django menggunakan csrf_token untuk mencegah serangan CSRF, di mana penyerang dapat melakukan aksi tidak sah di situs Anda dengan memanfaatkan sesi pengguna yang sedang login tanpa sepengetahuannya.

Fungsi csrf_token: Token ini dimasukkan ke form dan diverifikasi saat form dikirim ke server. Hal ini memastikan bahwa permintaan berasal dari situs Anda, bukan dari pihak luar yang mencoba menyalahgunakan sesi pengguna.

Jika csrf_token tidak ada: Situs Anda rentan terhadap serangan CSRF, di mana penyerang bisa menjalankan aksi seperti mengubah data atau melakukan transaksi tanpa izin.

Cara penyerang memanfaatkannya: Penyerang bisa membuat form tersembunyi di situs lain atau email, dan ketika pengguna mengkliknya, permintaan berbahaya akan dikirim ke server tanpa diketahui pengguna. Tanpa csrf_token, server tidak bisa membedakan apakah permintaan tersebut sah atau berbahaya.

5. - Hal pertama yang saya lakukan adalah adalah menambahkan form.py pada direktori main. Pada forms tersebut saya melakukan import modelform yang sudah ada dari django
- Selanjutnya saja melakukan import ProductEntry yang ada di models.py yang ada di main. ProductEntry di import agar nantinya model dari form dapat disimpan menjadi sebuah objek dari ProductEntry
- Setelah itu saya membuat class ProductEntryForm yang fieds nya terdapat name, description, price dan stock. sesua dengan input field yang akan ada nanti.
- Setelah itu Pada views.py saya mengimport ProductEntry dan MoodEntryForm yang sebelumnya sudah kita definisikan.
- Setelah itu saya membuat function create_product_entry yang nantinya akan menerima input, memvalidasi input dengan form.is_valid(), menyimpan data dengan form.save(), dan menunjukannya.
- Setelah itu saya menambahkan fungsi MoodEntry.objects.all() di views.py untuk mengambil seluruh objek dari ProductEntry.
- Setelah itu pada urls.py saya mengimport create_product_entry dan menambahkan pathnya.
- Setelah itu saya menambahkan berkan html untuk formnya agar dapat mengatur tampilannya. form tersebut saya simpa di direktori templates yang ada di main dengan nama create_product_entry
- Setelh itu saya lanjut untuk checklist selanjutnya. Saya menambahkan function pada views py yaitu show_json, show_xml, show_json_by_id, dan show_xml_by_id yang masing-masing memiliki isi seperti ini :
data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

- Setelah itu saya mengimport HttpResponse dan serializers yang memang sudah ada dari django.
- Setelah itu pada urls.py saya melakukan import dari setiap function diatas dan memasukan pathnya pada urlpatterns

SS Json :https://drive.google.com/file/d/1nsnsZBFQi6v-71V49jBUZEy6IFWvBfCU/view?usp=sharing

SS Xml : https://drive.google.com/file/d/1sxm0bNGZbIZQpQDrXQNCTn5D5fzLIZA0/view?usp=sharing

SS Xml By ID : https://drive.google.com/file/d/1o5aA1nX2_eQTGKp9FbCJ5nXKRClG3Btz/view?usp=sharing

SS Json By ID :https://drive.google.com/file/d/1cMjC_NPOfTFUvzeIt5np0-b05MFAGWin/view?usp=sharing