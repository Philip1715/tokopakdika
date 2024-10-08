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

Tugas 4:
1. Untuk HttpResponseRedirect memrlukan penyediaan URL secara manual yang akan dituju sedangkan untuk redirect() kita dapat menggunakan URL ataupun nama dari view, sehingga bisa dibilang redirect() lebih fleksibel mudah dibaca dan dipahami.

2. Penghubungan antara user dan product diawali dengan adanya ForeignKey, hal ini menjadikan user sebagai kunci dimana dengan itu product dapat dihubungkan dengan user dan membuat user bisa terhubung dengan banyak product. Setelah itu penambahan parameter commit=false membuat produk yang akan disimpan tidak langsung basuk ke database tetapi bisa dimodifikasi terlebih dahulu dan setelah itu objek ditandakan sebagai milik user yang sedang login dengan adanya return value dari request.user

3. Authentication adalah proses yang akan mengecek apakah data login yang dimasukan sesuai dengan apa yang ada di database.
Django mengimplementasikan authentication dengan adanya :
- Model User: Django menyediakan model User yang menyimpan informasi pengguna seperti username, password, email, dan lainnya.
- Form: Django memiliki class dan form siap pakai seperti from django.contrib.auth, UserCreationForm untuk pendaftaran dan AuthenticationForm untuk login.
- View: Django menyediakan view untuk menangani login (login), logout (logout), dan pendaftaran (register).
- Middleware: Django juga menyediakan middleware AuthenticationMiddleware yang mengatur pengguna yang sedang login di setiap permintaan.
- Dekorator: Anda bisa menggunakan dekorator @login_required untuk melindungi view sehingga hanya pengguna yang sudah terautentikasi yang dapat mengaksesnya.
 
Sedangkan authorization adalah proses yang memisah-misahkan data/sumber daya, kemampuan, dan hak dalam program antara para user ataupun antara user dengan admin sehingga setiap orang memiliki data/sumber daya, kemampuan, ataupun hak pada program yang berbeda-beda. 
Django mengimplementasikan authorization dengan adanya :
- Permissions: Django memungkinkan Anda untuk mendefinisikan izin (permissions) di level model. Anda bisa menentukan izin khusus untuk objek tertentu atau menggunakan izin default seperti add, change, dan delete.
- Group: Pengguna dapat dimasukkan ke dalam grup, dan grup ini dapat diberikan izin tertentu. Ini memudahkan pengelolaan izin untuk banyak pengguna.
- Decorator dan Middleware: Django menyediakan dekorator seperti @permission_required untuk membatasi akses ke view berdasarkan izin yang dimiliki pengguna.
- Custom Permissions: Anda juga dapat membuat izin kustom di dalam model Anda dengan menambahkan atribut permissions dalam Meta class.

4. Django mengingat pengguna yang telah login dengan mengunakan session dan cookies, dimmana keduanya adalah semacam ruang penyimpanan sementara yang akan dikirim ke server untuk melakukan request. 

Kegunaan Lain dari Cookies
- Pengaturan Preferensi Pengguna:
Cookies dapat menyimpan preferensi pengguna, seperti tema tampilan, bahasa, dan pengaturan lainnya agar pengalaman pengguna lebih personal.
Tracking dan Analytics:

- Cookies dapat digunakan untuk melacak perilaku pengguna di situs web, membantu dalam analisis data untuk meningkatkan pengalaman pengguna.
Keranjang Belanja:

- Dalam aplikasi e-commerce, cookies dapat menyimpan informasi tentang item yang ditambahkan ke keranjang belanja, sehingga pengguna dapat melanjutkan berbelanja di lain waktu.
Keamanan:

- Cookies dapat digunakan untuk menyimpan token keamanan yang digunakan untuk mengautentikasi permintaan API.

dan apakah semua cookies aman, jawabannya adalah tidak. Cookies dapat menyimpan kode atau token yang dapat dengan mudah diakses oleh orang tidak bertangung jawab melalui Cross-Site Scripting ataupun Cross-site Request Forgery, sehingga pelaku tersebut dapat melakukan request yang bisa menguntungkan pelaku dan merugikan user. Cookies yang tidak di enkripsi juga dapat terkena resiko penyadapan oleh pihak ketiga, misalnya melalui jaringan yang tidak aman seperti wifi publik. Hal ini dapat menimbulkan pencurian data, pelacakan, bahkan resiko kehilangan akses bagi korban.

5. - Tahap pertama yang saya lakukan adalah membuat form untuk register agar informasi login dapat ddisimpan. diawalai dengan mengimport class yang memang sudah ada dari django yaitu UserCreationForm(untuk membuat form) dan messages
- Setelah itu saya membuat fungsi register yang nantinya akan memunculkan form dan mendirect program untuk ke halaman login ketika form sudah diisi. Fungsi register disimpan di views.py
- Setelah itu untuk menampilkan form tersebut saya membuat file html baru bernama register.html yang disimpan di templates. setelah itu memasukan halaman register dengan mengimportnya di urls.py dan memasukan pathnya pada urlpatterns
- Setelah itu saya membuat fungsi login dan logout. Saya melakukan import AuthenticationForm dan authenticate, login yang tersedia dari django melalui django.contrib.auth. Dari sumber yang sama saya juga melakukan import logout. 
- Setelah itu saya menambahkann fungsi login dan logout di views.py sesuai dengan template kode. Karena sesi login memiliki halaman tersendiri, tidak seperti logout, maka saya membuat file html baru yaitu login.html untuk menampilkan tampilan login yang akan meminta username dan password. login.html disimpan di direktori templates.
- Untuk menambahkan tombol logout maka saya menempatkan 
    <!-- <a href="{% url 'main:logout' %}">
    <button>Logout</button>
    </a> -->
sebagai hyperlink tag yang akan mengembalikan halaman ke halaman login.
- Setelah itu saya mengimport fungsi login dan fungsi logout ke urls.py dan memasukan pathnya ke urlpattern.
- Untuk memastikan bahwa user harus login maka saya mengimport login_required melalui django.contrib.auth.decorators di views.py dan sebelum function main menu atau show_menu saya menambahkan dekorator @login_required(login_url='/login') sehingga user harus login terlebih dahulu sbeelum masuk ke tampilan main program.
- Setelah itu agar produk yang ditampilkan bisa sesuai dengan tiap-tiap user maka saya membuat 1 akun terlebih dahulu. setelah itu mengimport user dari django.contrib.auht.models pada models.py.
- Pada ProductEntry saya menambahkan user = models.ForeignKey(User, on_delete=models.CASCADE). Dengan menambahkan foreign key nantinya setiap produk akan terhubung dengan usernya dan user bisa terhubunga dengan banyak produk. 
- Setelah itu pada views.py saya menambahkkan :
    mood_entry = form.save(commit=False)
    mood_entry.user = request.user
    mood_entry.save()
form.save(commit=False) dtiambahkan agar setiap data tidak langsung ditambahkan ke database tetapi dapat dimodifikasi terlebih dahulu dan akan disimpan sesuai dengan user yang sedang login dengan adanya return dari request.user.
- Setelah itu agar default value dapat di set, saya melakukan make migrations dan migrate sehingga field user dibuat pada database.
- Setelah itu saya mengisi form pada akun pertama sebanyak 3 data dan setelah itu saya logout, membuat akun baru, login, dan mengisi akun tersebut dengan 3 data/produk.
- Setelah itu agar last login dapat diketahui oleh user saya menambahkan datetime, reverse, dan HttpResponseRedirect.
- Setelah itu saya menambahkan kode berikut :
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
kode berikut ditambahkan pada fungsi login_user ketika form tersebut valid. penambahan kode ini agar program dapat menyimpan waktu tepat ketika pengisian form login valid sehingga nantinya kita bisa mengetahui waktu dan tanggal saat kita terakhir kalo login.
- lalu pada context yang ada pada main agar keterangan login dapat dimunculka pada web, saya menambkan 'last_login': request.COOKIES['last_login'],
- Setelah agar dapat ditampilkan, saya menambahkan
 <!-- <h5>Sesi terakhir login: {{ last_login }}</h5>  -->
pada file main.html. Penempatannya saya letakan dibawah tombol logout.
- Setelah itu agar kedepannya lat_login dapat selalu diperbarui sesuai dengan waktu saat login, kita perlu menghapus data last_login yang sudah ada agar data tidak menumpuk. cara menghapusnya adalah dengan menempatkan response.delete_cookie('last_login') pada fungsi logout sehingga setiap kali user menekan tombol logout, data last_login dihapus dan siap menerima data baru sesuai dengan waktu saat user akan melakukan login lagi.

Tugas 5:

1. Urutan Prioritas CSS Selector
Urutan prioritas CSS selector diatur berdasarkan spesifisitas berikut ini:
- Inline styles: CSS yang ditulis langsung pada elemen HTML memiliki prioritas tertinggi (contoh: style="color: red;").
- ID selector: Selector yang merujuk pada ID elemen (contoh: #my-id) memiliki tingkat prioritas lebih tinggi daripada class atau tag.
- Class selector, pseudo-class, attribute selector: Selector seperti .my-class, :hover, dan [type="text"] memiliki prioritas yang lebih rendah daripada ID tapi lebih tinggi daripada selector elemen.
- Element selector: Selector yang menggunakan tag HTML (contoh: p, div, h1) memiliki prioritas terendah.
- Universal selector (*) dan kombinator (+, ~, >, ): memiliki prioritas paling rendah.
Jika ada conflict antara beberapa selector dengan spesifisitas yang sama, CSS akan menerapkan selector yang berada paling akhir dalam file.

2. Pentingnya Responsive Design dalam Pengembangan Web.
Dengan menerapkan Responsive Design, web dapat nmenyesuaikan designnya pada berbagai macam layout device, seperti smartphone, tablet, dan desktop, yang memiliki ukuran layar dan resolusi yang berbeda. Hal ini dapat membuat pengguna akan merasa nyaman ketika tampilan website dapat menyesuaikan dengan layar yang mereka gunakan.
Responsive design memastikan semua pengguna, termasuk pengguna dengan layar kecil atau besar, dapat mengakses konten dengan mudah.

Contoh aplikasi yang sudah menerapkan responsive design:
Google: Website Google memiliki layout sederhana namun responsif di berbagai perangkat.
Contoh aplikasi yang belum menerapkan responsive design:

Aplikasi website lama atau yang tidak di-update mungkin masih menggunakan layout fixed-width yang tidak beradaptasi dengan baik pada ukuran layar mobile, menyebabkan pengguna harus melakukan zoom dan scroll secara horizontal.

3. Perbedaan Margin, Border, dan Padding dalam CSS

- Margin: Jarak antara elemen dan elemen lainnya di luar border. Ini mengontrol ruang di luar elemen.
Contoh : 
div {
  margin: 20px;
}

- Border: Garis yang mengelilingi elemen dan berada di antara padding dan margin. Border ini terlihat secara visual.
Contoh :
div {
  border: 2px solid black;
}

- Padding: Ruang antara konten elemen dan border. Ini mengontrol ruang di dalam elemen
Contoh :
div {
  padding: 10px;
}

4. Flexbox
Flexbox (Flexible Box Layout) adalah model tata letak yang dirancang untuk mendistribusikan elemen dalam sebuah container secara fleksibel dalam satu dimensi (baik baris atau kolom).

Kegunaan: Flexbox sangat berguna untuk tata letak horizontal atau vertikal yang responsif, seperti menu navigasi, galeri gambar, atau card layout.

Grid Layout
CSS Grid adalah sistem tata letak dua dimensi yang memungkinkan kita untuk menyusun elemen dalam baris dan kolom. Ini jauh lebih kuat untuk tata letak kompleks dibandingkan Flexbox, karena Grid bekerja di dua dimensi (baik baris maupun kolom).

Kegunaan: Grid Layout digunakan untuk layout kompleks seperti desain halaman yang melibatkan beberapa kolom dan baris, seperti template halaman blog, galeri foto, atau halaman dashboard.

5. - Hal pertama yang saya lakukan pada tugas ini adalah mengimplementasi Tailwind ke dalam program ini. Selain itu saya juga memasukan global.css untuk kebutuhan desain yang lebih detail untuk kedepannya.
- Untuk mencapai fitur menghapus dan mengedit, saya membuat fungsi edit_product dan delete_product di views.py. Nantinya fungsi edit_product akan mengarahkan halaman ke halaman edit_product dan menampilkan form sehingga kita bisa mengubah data product. Untuk delete_product akan menghapus akan melakukan get terhadap product id lalu melakukan operasi delete.
- Setelah itu pada urls.py, saya mengimport kedua fungsi tersebut dan memasukannya ke urlpatterns.
- Supaya bisa menampilkan halaman edit_product, saya menambahkan edit_product.html yang nantinya akan memunculkan form, lalu akan return ke main ketika sudah di submit. 
- Masuk ke bagian navbar saya melakukan penambahan file yaitu navbar.html. Lalu saya melakukan desain dengan menempatkan nama toko, beberapa elemen navbar dan juga tombol logout yang akan mereturn program ke halaman login.
- Setelah itu masuk ke kostumasasi desain template html. template pertama yang saya ubah adalah login page. Saya membuat gambar dengan tema promo diskon 10.10. Setelah itu pada template saya membuat sebuah box yang di dalamnya terdapat bar untuk mengisi username, bar untuk menngisi password, tombol login, dan dibawahnya link yang mengarahkan ke register page.
- Setelah itu saya tempatkan gambar 1010sale sejajar dengan box tersebut.
- Template yang saya ubah selanjutnya adalah register page. Kurang lebih isi dari register pae dan login page sama. yang membedakan adalah adanya bar untuk confirmation page dan juga link yang akan mengarahkan pengguna ke login page jikda sudah memiliki akun.
- Setelah itu agar nantinya penampilan dari setiap product lebih terstruktur saya membuat file baru bernama card_prduct. Pada card product saya menampilkan semua data product lalu membuat dua tombol di dalamnya yang nantinya akan berguna untuk mengedit dan menghapus product.
- Pada bagian main.html saya menghapus semua isi yang ada sebelumnya, menyisakan tombol product_entry dan keterangan last login yang saya berikan box dan memberi warna hijau. Pada bagian yang sama saya melakukan penambahan yang memangil card_product, menempatkannya sejajar. Kemudian saya membuat conditional yang dimana jika product_entries kosong maka akan menampilkan keterangan dan gambar bahwa belum ada product di Tokopakdika. 
- Untuk mencapai checklist tereakhir saya menambahkan navbar.html pada setiap html yang ada.
- Untuk mencegah tertimpanya card_product dengan navbar pada main.html, saya membuat sebuah page abu sehingga membuat jarak antara card_product dengan bagian teratasdari halaman atau page.
- Sebagai hal terakhir dari checklist, saya mengisi readme ini.

Tugas 6 :
1. Manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web:

- Interaktivitas: JavaScript memungkinkan pengembang membuat halaman web yang interaktif. Misalnya, form validasi langsung, animasi, dan respons terhadap input pengguna tanpa perlu memuat ulang halaman.
- Pengalaman Pengguna yang Lebih Baik: Dengan JavaScript, halaman web bisa di-update secara dinamis menggunakan AJAX tanpa memuat ulang seluruh halaman, sehingga memberikan pengalaman yang lebih cepat dan responsif.
- Pengelolaan DOM: JavaScript dapat digunakan untuk memanipulasi dan memperbarui elemen-elemen DOM secara langsung, memungkinkan konten halaman berubah berdasarkan tindakan pengguna.
- Pengembangan Aplikasi Web Modern: JavaScript mendukung pengembangan aplikasi web modern seperti SPA (Single Page Applications) menggunakan framework seperti React, Angular, dan Vue, yang memungkinkan navigasi cepat tanpa memuat ulang halaman.
- Kompatibilitas Cross-platform: JavaScript berjalan di browser pengguna, artinya aplikasi web berbasis JavaScript dapat berjalan di berbagai perangkat dan platform tanpa perlu pengaturan tambahan.

2. Fungsi await ketika menggunakan fetch(): await digunakan untuk menunggu penyelesaian Promise yang dikembalikan oleh fetch(). fetch() adalah fungsi asinkron yang melakukan permintaan HTTP, dan hasilnya tidak segera tersedia karena membutuhkan waktu untuk mendapatkan respons dari server. Dengan await, kode berhenti sejenak dan menunggu hasil permintaan HTTP sebelum melanjutkan eksekusi.

Jika kita tidak menggunakan await, maka fetch() akan mengembalikan Promise yang belum terselesaikan, dan kode akan terus berjalan tanpa menunggu respons. Hal ini bisa menyebabkan error atau data yang belum tersedia, karena operasi yang bergantung pada hasil fetch() akan dieksekusi sebelum hasil tersebut diterima.

Contoh perbedaannya:
// Dengan await
const response = await fetch(url);
const data = await response.json();
console.log(data); // Mencetak data setelah respons diterima

// Tanpa await
const response = fetch(url);
console.log(response); // Mencetak Promise yang belum diselesaikan

3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang digunakan untuk AJAX POST: CSRF (Cross-Site Request Forgery) adalah serangan yang memanfaatkan kepercayaan antara pengguna dan server. Django secara default mengaktifkan perlindungan CSRF untuk semua permintaan POST agar permintaan dari domain yang tidak diizinkan tidak dapat dilakukan tanpa izin pengguna.

Jika kita melakukan permintaan AJAX POST tanpa melampirkan token CSRF yang valid, Django akan menolak permintaan tersebut. Decorator csrf_exempt digunakan untuk menonaktifkan pemeriksaan CSRF pada view tertentu, terutama ketika:
- Kita tahu bahwa permintaan berasal dari sumber yang tepercaya.
- Kita belum menambahkan mekanisme untuk mengirim token CSRF bersama dengan permintaan AJAX.
Namun, meskipun menggunakan csrf_exempt memberikan kemudahan, penting untuk memastikan keamanan lain tetap terjaga untuk menghindari potensi serangan.

4. Mengapa pembersihan data input pengguna dilakukan di backend juga, tidak hanya di frontend: Meskipun pembersihan input dapat dilakukan di frontend untuk memberikan pengalaman pengguna yang lebih baik (misalnya, validasi langsung dan pesan error), melakukan pembersihan hanya di frontend tidak cukup aman. Alasannya adalah:

- Frontend Dapat Dimodifikasi: Kode JavaScript di frontend dapat diubah atau dilewati oleh pengguna menggunakan alat debugging browser. Hal ini memungkinkan pengguna mengirimkan data yang tidak valid atau berbahaya (misalnya, script injeksi).
- Keamanan Server: Backend merupakan lapisan terakhir dari keamanan aplikasi. Jika input hanya dibersihkan di frontend, ada risiko server menerima input yang tidak aman, yang bisa menyebabkan serangan seperti SQL injection atau XSS (Cross-Site Scripting).
- Konsistensi: Backend perlu memastikan semua data yang diterima dari berbagai sumber (termasuk API atau integrasi lainnya) selalu bersih dan valid, sehingga pembersihan di backend menjaga konsistensi dan integritas data.

Oleh karena itu, walaupun validasi dan pembersihan input di frontend berguna untuk pengalaman pengguna, validasi dan pembersihan di backend adalah keharusan demi keamanan dan integritas aplikasi.

5. - Step pertama yang saya lakukan adalah melakukan import untuk mendukung pembuatan add_product_entry_ajax. 
- Saya membuat function baru bernama add_product_entry_ajax yang memiliki fungsi yang sama dengan productEntry.
- Saya memastikan bahwa pemetaan isi yang di get sesuai dengan variabel pada ProductEntry
- Setelah itu pada urls.py, add_product_entry_ajax di import dan ditambahkan pathnya di urlpatterns
- Setelah itu saya menghapus product_entries yang ada di views.py karena untuk nantinya data akan langsung di filter di json/xml
- saya menambahkan line yang akan mamasukan nilai berupa objek-objek product yang sudah di filter bedasarkan usernya. Line ini ditambahkan di show_json dan show_xml
- Tak lupa saya menghapus line pengambilan data yang lama agar setiap data hanya muncul sesuai dengan user yang sedang login.
- Pada main.html bagian yang berguna untuk menampilkan produk di halaman utama di hapus dan digantikan dengan penaruan product_entry_cards sebagai penanda.
- Setalah itu pada main.html saya membuat sebuah function di script yang akan mendefinisikan bagian yang sudah di tag id product_entry_cards. Isi dari function kurang lebih sama dengan bagian yang di hapus sebelumya, hanya saja terdapat penambahan kode berupa tampilan card dari product yang sudah saya buat sebelumnya, yang dimanya sebelumnya kode tersebut hanya berada di card_product.html.
- Setelah itu saya membuat function di script yang akan melakukan get terhadap product entries, mengambilnya melalui json.
- Agar dapat menambahkan product dengan ajax, saya menambahkan sebuah function yang mengambil id melalui productForm dan merespon terhadap click. Setelah itu menambahkan menambahkan kode yang akan menerima respon submit
- Setelah itu saya menambahkan implementasi modal pada program sesuai dengan ketentuan. Untuk implementasi modal ini, saya menyesuaikannya dengan kebutuhan program saya yang memrlukan 4 data yaitu name, description, price, dan stock. 
- Setelah itu saya menambahkan function showModal dan hideModal yang dibutuhkan karena tidak adanya class modal yang sudah built in di Tailwind CSS.
- Step terakhir yaitu agar web aman dari XSS atau Cross Site Scripting, saya mengimport strip_tags dan menempatkannnya di variabel data yang bisa menerima input tulisan seperti name dan description.
- Setelah itu pada forms saya menambahkan method clean_product dan clean_feelings agar jika ada upaya untuk melakukan XSS, input yang dimasukan dapat langsung ditolak dan dibersihkan
- Dan terakhir saya mengisi readme.md ini.