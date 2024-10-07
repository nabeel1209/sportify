##### Nabeel Muhammad (2306275166)
Web : http://nabeel-muhammad-sportify.pbp.cs.ui.ac.id/
# Tugas 2: Implementasi *Model-View-Template* (MVT) pada Django
- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Membuat sebuah proyek Django baru.
        1. Membuat folder baru dengan nama `sportify`.
        2. Membuat virtual environment dengan menjalankan `python -m venv env` pada terminal dengan directory `sportify`.
        3. Membuat file dengan nama `requirements.txt` yang berisikan depedencies yang dibutuhkan untuk membuat project Django
            ```
            django
            gunicorn
            whitenoise
            psycopg2-binary
            requests
            urllib3
            ```
        4. Mengaktifkan virtual environment dengan menjalankan `env/Scripts/activate` pada terminal dengan directory `sportify`.
        5. Melakukan instalasi depedencies dengan menjalankan `pip install -r requirements.txt` pada terminal.
        6. Membuat project Django dengan menjalankan `django-admin startproject sportify .` pada terminal.
    -  Membuat aplikasi dengan nama main pada proyek.tersebut.
        1. Menjalankan ```python manage.py startapp main``` pada terminal.
    - Melakukan routing pada proyek agar dapat menjalankan aplikasi main. Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu. Membuat sebuah routing pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`.
        1. Membuat folder `templates` pada folder `main` yang nantinya akan digunakan untuk menyimpan file HTML untuk setiap page yang dibutuhkan.
        2. Membuat file dengan nama `main.html` yang berguna untuk menyimpan tampilan halaman utama untuk *main app*
        3. Mengisi file `views.py` pada folder `main` dengan fungsi yang menerima parameter *request* dan berguna untuk me-*render* `main.html` serta menyertakan *context* yang nantinya akan berupa data dari *database* yang kita inginkan. Dalam Tugas 2 ini saya hanya menggunakan *code* di bawah ini.
            ```
            from django.shortcuts import render

            def show_main(request):
                context = {
                    'app_name' : 'Sportify',
                    'name': 'Nabeel Muhammad',
                    'class': 'PBP A'
                }

                return render(request, "main.html", context)
            ```
        4. Membuat file `urls.py` yang berisikan *code* dibawah ini.
            ```
            from django.urls import path
            from main.views import show_main

            app_name = 'main'

            urlpatterns = [
                path('', show_main, name='show_main'),
            ]
            ```
            *Code* di atas berguna untuk membuat url yang nantinya akan dideteksi oleh Django sebagai `main.urls` untuk menghubungkan *main app* dengan project *Sportify* 
        5. Menambahkan *code* di bawah ini pada file `urls.py` yang berada di dalam folder `sportify` 
            ```
            from django.urls import include
            ....
            urlpatterns = [
                ....
                path('', include("main.urls")),
                ....
            ]
            ```
        6. Menambahkan `main` pada `INSTALLED_APPS` yang berada pada file `settings.py` dalam folder `sportify` 
            ```
            INSTALLED_APPS = [
                ....,
                'main'
            ]
            ```
    - Membuat model pada aplikasi `main` dengan nama `Product` dan memiliki atribut wajib sebagai berikut.
        - `name`
        - `price`
        - `description`
        1. Mengubah isi pada file `models.py` yang berada pada folder `main` dengan class sesuai yang diinginkan. Dalam Tugas 2 ini kita membuat class `Product` dengan *code* di bawah ini.
            ```
            from django.db import models

            class Product(models.Model):
                name = models.CharField(max_length=255)
                price = models.IntegerField()
                description = models.TextField()
                stock = models.IntegerField()
            ```
            Saya menambahkan atribut `stock` yang nantinya akan menjadi atribut untuk setiap object `Product`.
        2. Menjalankan `python manage.py makemigrations` pada terminal untuk mempersiapkan migrasi skema model ke dalam database Django lokal
        3. Menjalankan `python manage.py migrate` pada terminal untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.
<br/>

- Buatlah bagan yang berisi *request client* ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas html.
    <img src="./Tugas2PBP.png"/>
    - `urls.py` : berguna untuk menentukan views yang sesuai dengan request yang diberikan.
    - `views.py` : berguna untuk berinteraksi dengan `models.py` lalu menjalankan logika yang diinginkan.
    - `models.py` : berguna untuk memodelkan data yang ingin disimpan pada database serta digunakan pada HTML melalui `views.py`.
    - `HTML` : berguna untuk menampilkan data sesuai tampilan yang diinginkan.

- Jelaskan fungsi git dalam pengembangan perangkat lunak!
    1. Sebagai penyimpanan *source code* dari project yang ingin kita buat.
    2. Memudahkan kolaborasi karena kita dapat melakukan *pull request* yang membuat *source code* dapat dikerjakan sesuai bagian yang telah dibagikan.
    3. Sebagai *version control* karena mempunyai sistem *commit* yang dapat kita lihat sebagai *control* terhadap perubahan *file* yang dilakukan.
<br/>

- Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    1. **Kemudahan Penggunaan dan Konvensi**: Django didesain dengan prinsip "*batteries included*" yang berarti banyak fitur penting, seperti otentikasi, manajemen database, dan routing, sudah disediakan langsung tanpa perlu konfigurasi tambahan. Ini memudahkan pemula untuk fokus pada logika aplikasi daripada harus membangun semuanya dari nol.
    2. **Dokumentasi Lengkap**: Django dikenal dengan dokumentasinya yang sangat lengkap dan ramah bagi pemula. Dokumentasi yang jelas membantu pengguna baru memahami konsep-konsep dasar *framework* tanpa terlalu banyak kebingungan.
    3. **Community Support**: Django memiliki komunitas yang besar dan aktif, sehingga jika pemula menghadapi masalah, mereka bisa dengan mudah menemukan solusi melalui forum, blog, atau Stack Overflow.
<br/>

- Mengapa model pada Django disebut sebagai ORM?
    Karena Django menggunakan objek dalam Python untuk melakukan interaksi dengan *database*. Object Relational Mapper (ORM) pada Django merupakan *library code* yang berguna untuk otomatisasi *data transfer* yang disimpan pada *relational database tables* menjadi objek yang mudah diimplementasi dalam Python.
___

# Tugas 3: Implementasi Form dan Data Delivery pada Django

- **Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**
    1. **Berguna untuk pertukaran data antar komponen dalam platform:**  Setiap platform pastinya terdiri dari berbagai modul atau layanan yang saling berhubungan. *Data delivery* memungkinkan adanya pertukaran informasi atau data antar layanan sehingga platform dapat berfungsi secara optimal.
    2. **Interaksi Pengguna:** Sebuah platform seringkali bergantung pada interaksi pengguna, seperti saat pengguna mengirimkan permintaan, formulir, atau data lainnya. Data delivery memastikan bahwa data yang dimasukkan oleh pengguna dapat sampai ke sistem dengan aman dan cepat untuk diolah dan dikembalikan dalam bentuk tanggapan atau layanan.
    3. **Ketersediaan dan Konsistensi Data Real-Time:** Banyak platform modern, terutama yang berbasis web atau cloud, memerlukan pengiriman data secara real-time. Misalnya, dalam aplikasi e-commerce, data tentang ketersediaan produk, harga, dan pembaruan stok harus dikirimkan ke pengguna secara tepat waktu untuk menjaga konsistensi informasi.
    4. **Skalabilitas Platform:** Ketika platform berkembang dan harus melayani lebih banyak pengguna atau data, sistem pengiriman data harus mampu menangani peningkatan volume tersebut. Sistem data delivery yang skalabel memastikan bahwa platform dapat melayani pengguna dalam jumlah besar tanpa penurunan performa.
- **Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**
    Untuk mengetahui manakah yang lebih baik natar XML dengan JSON kita perlu mengetahui perbedaan keduanya. Diantaranya yaitu,
    1. **Struktur**
        JSON mempunyai struktur yang lebih sederhana dibandingkan dengan XML. JSON menggunakan struktur berupa *map* / *dictionary* yaitu pasangan "key-value". Hal ini sangat berbeda dengan XMl yang menggunakan tag untuk merepresentasikan key serta inner text untuk merepresentasikan valuenya
    2. **Kompatibilitas**
        JSON sesuai namanya yaitu JavaScript Object Notation dapat diintegrasikan langsung dengan web berbasis javascript. Developer tidak perlu mengonversi data bertipe JSON ini karena dapat digunakan secara langsung oleh javascript. Berbeda halnya dengan XML, XML juga dapat digunakan oleh javascript melalui DOM (Document Object Model) atau parser XML sehingga membutuhkan lebih banyak kode tambahan untuk memprosesnya.
    3. **Ukuran File**
        JSON cenderung menghasilkan file yang lebih kecil karena tidak menggunakan tag penutup yang berlebihan seperti XML. Ukuran yang lebih kecil berarti waktu pengiriman data yang lebih cepat, yang penting untuk aplikasi web yang memerlukan pengiriman data melalui jaringan.
    4. **Fleksibilitas**
        XML menawarkan fleksibilitas yang lebih besar dalam hal penandaan, penyematan skema (*schemas*), dan pemformatan data yang kompleks. Ini cocok untuk aplikasi yang membutuhkan validasi dan aturan yang ketat, seperti di beberapa industri (misalnya, keuangan atau medis). JSON lebih sederhana dan fokus pada kecepatan dan efisiensi, cocok untuk aplikasi modern yang tidak memerlukan fitur-fitur kompleks yang ditawarkan XML.
    
    **Kesimpulan:**
    JSON lebih populer karena kesederhanaannya, kemudahan integrasinya dengan JavaScript dan teknologi web, ukuran yang lebih kecil, serta kecepatan parsing yang lebih baik. Itu membuatnya lebih efisien dan lebih cocok untuk penggunaan dalam web development dan aplikasi API modern. XML masih memiliki tempat di mana struktur data yang lebih kompleks dan validasi dokumen diperlukan, tetapi di luar konteks tersebut, JSON lebih diutamakan.
- **Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?**
    Method `is_valid()` pada saat mengimplementasikan form berguna untuk memvalidasi tipe data yang dimasukkan pada input form. Hal ini dapat mencegah user untuk mengisi form dengan data yang tidak seharusnya kita minta. Kita membutuhkan method `is_valid()` untuk memudahkan kita dalam memvalidasi sehingga kita tidak perlu membuat method validasi sendiri yang pastinya membutuhkan waktu lebih banyak daripada kita langsung menggunakan method `is_valid()` yang disediakan oleh Django.
- **Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**
    Kita membutuhkan `csrf_token` saat membuat form di Django untuk melindungi aplikasi web dari serangan **CSRF (*Cross-Site Request Forgery*)**. Serangan CSRF adalah jenis serangan di mana penyerang menipu pengguna yang sah agar mengirimkan permintaan berbahaya ke aplikasi web di mana mereka telah terotentikasi, tanpa sepengetahuan pengguna. CSRF terjadi ketika penyerang memanfaatkan sesi login aktif pengguna untuk melakukan tindakan yang tidak diinginkan di aplikasi web. Misalnya, jika pengguna login ke situs yang sah, penyerang dapat membuat halaman berbahaya yang mengirimkan permintaan ke situs tersebut dengan menggunakan kredensial pengguna yang telah diautentikasi. 
    **Fungsi `csrf_token`:**
    `csrf_token` adalah token keamanan unik yang dihasilkan oleh server dan dikirim bersama dengan setiap permintaan form POST. Token ini:
    - Hanya dikenal oleh server dan pengguna yang sah.
    - Diverifikasi oleh server setiap kali form dikirim.
    - Tidak dapat ditebak atau direproduksi oleh penyerang.

    Tanpa `csrf_token`, aplikasi web rentan terhadap serangan CSRF, yang dapat memungkinkan penyerang untuk mengirimkan permintaan berbahaya dan menyebabkan kerugian besar bagi pengguna dan aplikasi web itu sendiri. Penyerang dapat memanfaatkan ketidakadaan csrf_token dengan membuat permintaan POST berbahaya ke server menggunakan kredensial pengguna yang sedang aktif (misalnya, pengguna yang sudah login ke suatu situs web). Berikut adalah langkah serangan sederhana:

    1. Pengguna login ke aplikasi web yang sah, seperti akun perbankan online.
    2. Penyerang membuat situs web palsu atau mengirim email yang berisi permintaan POST ke aplikasi web yang sah.
    3. Saat pengguna yang telah login ke situs web sah mengunjungi situs web palsu tersebut, browser pengguna akan secara otomatis mengirimkan cookie sesi yang sah bersama permintaan POST tersebut ke server target.
    4. Tanpa validasi token CSRF, server menganggap permintaan tersebut berasal dari pengguna sah, sehingga permintaan diproses.

- **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
    - Membuat input form untuk menambahkan objek model pada app sebelumnya.
        1. Membuat file `forms.py` pada folder `main` yang berisi fungsi yang digunakan untuk memanggil form yang berisikan input sesuai dengan model yang dimiliki. File `forms.py` akan berisikan kode dibawah ini
            ```python
            from django.forms import ModelForm
            from main.models import Product

            class ProductForm(ModelForm):
                class Meta:
                    model = Product
                    fields = ["name", "price", "description", "stock"] 
            ```
            Note:
            - `model = Product` digunakan untuk mendefinisikan input pada form agar sesuai dengan atribut yang dimiliki oleh model Product.
            - `fields = ["name", "price", "description", "stock"]` digunakan untuk mendefinisikan atribut dari model Product mana yang akan digunakan sebagai input form.
        2. Membuat fungsi `create_product` serta mengimport beberapa module yaitu 
            ```python
            from django.shortcuts import render, redirect
            from main.forms import ProductForm
            from main.models import Product
            ``` 
            pada file `views.py`. Fungsi `create_product` akan berisikan
            ```python
            def create_product(request):
                form = ProductForm(request.POST or None)
                
                if form.is_valid() and request.method == 'POST':
                    form.save()
                    return redirect('main:show_main')
                
                context = {'form' : form}
                return render(request, "create_product.html", context)
            ```
            Note:
            - `form = ProductForm(request.POST or None)` digunakan untuk membuat ProductForm baru dengan memasukkan *QueryDict* berdasarkan input dari user pada `request.POST`.
            - `form.is_valid()` digunakan untuk memvalidasi isi dari input sesuai dengan tipe data atribut yang dimiliki oleh model `Product`.
            - `form.save` digunakan untuk menyimpan hasil input form ke dalam database.
            - `return redirect('main:show_main')` digunakan untuk kembali ke url yang sesuai dengan fungsi pada `views.py` yaitu `show_main(request)`
        3. Membuat file HTML pada folder `templates` yang berada di folder `main` yang berguna untuk menampilkan UI dari `forms.py` dengan nama `create_product.html` yang berisi 
            ```HTML
            {% extends 'base.html' %} 
            {% load static %}
            {% block meta %}
            <title>Create product</title>
            {% endblock meta %}

            {% block content %}
            <h1>Add New Product</h1>

            <form method="POST">
            {% csrf_token %}
            <table>
                {{ form.as_table }}
                <tr>
                <td></td>
                <td>
                    <input type="submit" value="Add Product" />
                </td>
                </tr>
            </table>
            </form>

            {% endblock content %}
            ```
        4. Menambahkan `urlpatterns` pada `urls.py` yang berguna untuk mendefinisikan url serta fungsi yang akan menampilkan `create_product.html` dengan menambahkan 
            ```python
            from main.views import ....., create_product
            urlpatterns = [
                ...., 
                path('create-product', create_product, name='create_product'),
                ....
            ]
            ```


    - Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
        - XML
            1. Menambahkan fungsi untuk melihat objek dalam format XML serta import module dengan menambahkan
                ```python
                from django.http import HttpResponse
                from django.core import serializers

                def show_xml(request):
                    data = Product.objects.all()
                    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
                ```
                Note:
                - `Product.objects.all()` berguna untuk mengambil seluruh objek `Product` yang terdaftar pada sistem.
                - `return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")` berguna untuk memberikan HTTP Response dengan menampilkan data `Product` berupa XML file.
            2. Meng-*import* fungsi yang sudah dibuat pada `views.py` serta menambahkan *path url* dalam `urlpatterns` untuk mengakses page yang berisikan hasil return dari fungsi `show_xml` pada `views.py`
                ```python
                urlpatterns=[
                    ...., 
                    path('xml/', show_xml, name='show_xml'),
                    ....
                ]
                ```
        - JSON
            1. Menambahkan fungsi untuk melihat objek dalam format JSON dengan menambahkan kode dibawah ini pada `views.py`
                ```python
                def show_json(request):
                    data = Product.objects.all()
                    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
                ```
                Note:
                - `Product.objects.all()` berguna untuk mengambil seluruh objek `Product` yang terdaftar pada sistem.
                - `return HttpResponse(serializers.serialize("json", data), content_type="application/json")` berguna untuk memberikan HTTP Response dengan menampilkan data `Product` berupa JSON file.
            2. Meng-*import* fungsi yang sudah dibuat pada `views.py` serta menambahkan *path url* dalam `urlpatterns` untuk mengakses page yang berisikan hasil return dari fungsi `show_json` pada `views.py`
                ```python
                urlpatterns=[
                    ...., 
                    path('json/', show_json, name='show_json'),
                    ....
                ]
                ```
        - XML by ID
            1. Menambahkan fungsi untuk melihat objek dalam format XML dengan ID spesifik dengan menambahkan
                ```python
                def show_xml_by_id(request, id):
                    data = Product.objects.filter(pk=id)
                    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
                ```
                Note:
                - `Product.objects.filter(pk=id)` berguna untuk mengambil sebuah objek `Product` dengan ID spesifik yang terdaftar pada sistem.
                - `return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")` berguna untuk memberikan HTTP Response dengan menampilkan data `Product` berupa XML file.
            2. Meng-*import* fungsi yang sudah dibuat pada `views.py` serta menambahkan *path url* dalam `urlpatterns` untuk mengakses page yang berisikan hasil return dari fungsi `show_xml_id` pada `views.py`
                ```python
                urlpatterns=[
                    ...., 
                    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
                    ....
                ]
                ```
        - JSON by ID
            1. Menambahkan fungsi untuk melihat objek dalam format XML dengan ID spesifik dengan menambahkan
                ```python
                def show_json_by_id(request, id):
                    data = Product.objects.filter(pk=id)
                    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
                ```
                Note:
                - `Product.objects.filter(pk=id)` berguna untuk mengambil sebuah objek `Product` dengan ID spesifik yang terdaftar pada sistem.
                - `return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")` berguna untuk memberikan HTTP Response dengan menampilkan data `Product` berupa JSON file.
            2. Meng-*import* fungsi yang sudah dibuat pada `views.py` serta menambahkan *path url* dalam `urlpatterns` untuk mengakses page yang berisikan hasil return dari fungsi `show_xml_id` pada `views.py`
                ```python
                urlpatterns=[
                    ...., 
                    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
                    ....
                ]
                ```
- **Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam `README.md`**

    <img src="./Tugas3/JSON.png"/>
    <img src="./Tugas3/XML.png"/>
    <img src="./Tugas3/JSONByID.png"/>
    <img src="./Tugas3/XMLByID.png"/>

---
# Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django

- Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`
    - `redirect()` lebih mudah digunakan karena dapat menerima argumen lain seperti view name atau model object, sementara `HttpResponseRedirect` hanya menerima URL.
    - `redirect()` lebih fleksibel dan mendukung nama view serta objek model untuk pengalihan, sedangkan `HttpResponseRedirect` hanya bekerja dengan URL eksplisit.
    - `redirect()` lebih disukai dalam praktik terbaik karena lebih ringkas dan membuat kode lebih mudah dibaca.
    <br/>

- Jelaskan cara kerja penghubungan model `Product` dengan `User`!
    Dengan menambahkan atribut `User` sebagai `ForeignKey` pada object `Product`. Cara implementasinya adalah sebagai berikut:
    - Menambahkan kode di bawah ini pada `models.py`
        ```python
        from django.contrib.auth.models import User
        ....
        class Product(models.Model):
            user = models.ForeignKey(User, on_delete=models.CASCADE)
            .....
        ```
- Apa perbedaan antara *authentication* dan *authorization*, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
    - *authentication* adalah cara untuk memastikan bahwa user merupakan bagian dari user yang teregistrasi oleh sistem. Cara implementasinya adalah sebagai berikut:
        1. Membuat `register form` serta `login form` yang digunakan untuk authentication yang nantinya diimplementasikan dalam `templates` agar `user` dapat menginput data credential mereka agar sistem dapat memastikan `user` benar teregistrasi dalam sistem. Hal ini dapat diimplementasi pada kode dengan menambahkan kode di bawah ini pada `views.py`
            ```python
            def register(request):
            form = UserCreationForm()
            if request.method == "POST":
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Your account has been successfully created!')
                    return redirect('main:login')
            context = {'form':form}
            return render(request, 'register.html', context)

            def login_user(request):
            if request.method == 'POST':
                form = AuthenticationForm(data=request.POST)
                if form.is_valid():
                    user = form.get_user()
                    login(request, user)
                    response = HttpResponseRedirect(reverse("main:show_main"))
                    response.set_cookie('last_login', str(datetime.datetime.now()))
                    return response
            else:
            form = AuthenticationForm(request)
            context = {'form': form}
            return render(request, 'login.html', context)
            ```
        2. Nantinya kita juga akan membuat `register.html` pada folder `templates` yang ada pada folder `main`. Kedua file ini berisikan 
            ```html
            {% extends 'base.html' %}

            {% block meta %}
            <title>Register</title>
            {% endblock meta %}

            {% block content %}

            <div class="login">
            <h1>Register</h1>

            <form method="POST">
                {% csrf_token %}
                <table>
                {{ form.as_table }}
                <tr>
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar" /></td>
                </tr>
                </table>
            </form>

            {% if messages %}
            <ul>
                {% for message in messages %}
                <li>{{ message }}</li>
                {% endfor %}
            </ul>
            {% endif %}
            </div>

            {% endblock content %}
            ```
        3. Kita juga akan membuat `login.html` pada folder `templates` yang ada pada folder `main`. Kedua file ini berisikan
            ```html
            {% extends 'base.html' %}

            {% block meta %}
            <title>Login</title>
            {% endblock meta %}

            {% block content %}
            <div class="login">
            <h1>Login</h1>

            <form method="POST" action="">
                {% csrf_token %}
                <table>
                {{ form.as_table }}
                <tr>
                    <td></td>
                    <td><input class="btn login_btn" type="submit" value="Login" /></td>
                </tr>
                </table>
            </form>

            {% if messages %}
            <ul>
                {% for message in messages %}
                <li>{{ message }}</li>
                {% endfor %}
            </ul>
            {% endif %} Don't have an account yet?
            <a href="{% url 'main:register' %}">Register Now</a>
            </div>

            {% endblock content %}
            ```
    - *authorization* adalah cara untuk memberikan role serta permisssions kepada user yang teregistrasi oleh sistem. Cara implementasinya adalah sebagai berikut:
        Berikut adalah cara mengatur grup pada Django Admin sesuai dengan panduan otentikasi di [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication):

        1. **Membuat Grup di Django Admin**:
        Akses halaman admin Django, lalu pilih bagian "Groups" di bawah kategori "Authentication and Authorization". Di sini, Anda bisa membuat grup baru dan memberi nama yang sesuai, misalnya "Admin" atau "Editor".

        2. **Menambahkan Izin ke Grup**:
        Setelah grup dibuat, Anda dapat menambahkan izin yang spesifik ke grup tersebut. Django menyediakan izin seperti tambah, ubah, hapus, dan lihat pada setiap model. Dengan ini, Anda bisa mengontrol apa yang bisa dilakukan oleh pengguna dalam grup tersebut.

        3. **Menambahkan Pengguna ke Grup**:
        Masuk ke bagian "Users" pada admin Django, pilih pengguna yang ingin ditambahkan ke grup, dan di bagian "Groups", pilih grup yang diinginkan. Pengguna tersebut akan mewarisi semua izin yang telah ditetapkan untuk grup tersebut.

        4. **Kustomisasi Tampilan Grup di Admin**:
        Anda dapat menyesuaikan bagaimana grup dan izin ditampilkan di antarmuka admin dengan mengedit file `admin.py`. Misalnya, Anda bisa membuat tampilan yang lebih mudah untuk mengelola pengguna dan grup secara efisien.


- Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari *cookies* dan apakah semua *cookies* aman digunakan?
    Django mengingat pengguna yang telah login menggunakan mekanisme **session** yang memanfaatkan **cookies**. Saat seorang pengguna login, Django membuat sebuah *session* yang disimpan di database atau backend lain (misalnya file-based atau cache). Kemudian, Django mengirimkan *session ID* kepada pengguna dalam bentuk cookie. <br>
    - Prosesnya secara singkat adalah sebagai berikut:
        1. **Login**: Saat pengguna memasukkan kredensial yang benar, Django membuat sebuah *session* untuk pengguna tersebut dan menyimpannya di backend *session*.
        2. **Cookie Session ID**: Django mengirimkan sebuah cookie berisi *session ID* ke browser pengguna.
        3. **Session Tracking**: Setiap kali pengguna mengirim request baru, browser akan mengirimkan *session ID* melalui cookie. Django akan memverifikasi *session ID* tersebut dan memastikan bahwa pengguna masih terotentikasi.
        4. **Logout**: Saat pengguna logout, Django akan menghapus *session* yang terkait dengan pengguna tersebut, sehingga cookie tersebut menjadi tidak berguna.<br>
    - Selain mengingat pengguna yang telah login, cookies memiliki beberapa kegunaan lain, antara lain:
        1. **Personalization**: Cookies dapat digunakan untuk menyimpan preferensi pengguna seperti tema tampilan atau bahasa yang dipilih.
        2. **Tracking**: Cookies sering digunakan oleh perusahaan untuk melacak perilaku pengguna di berbagai halaman dan situs, sering kali digunakan untuk kepentingan iklan berbasis perilaku (behavioral advertising).
        3. **Shopping Cart**: Dalam situs e-commerce, cookies dapat digunakan untuk menyimpan item yang dimasukkan ke dalam keranjang belanja meskipun pengguna belum login.

    - Tidak semua cookies aman digunakan. Ada beberapa aspek keamanan yang perlu dipertimbangkan:
        1. **Cookies Aman (Secure Cookies)**: Cookies ini hanya dikirim melalui koneksi HTTPS yang aman, sehingga mencegah penyadapan selama transmisi. Django memungkinkan pengaturan agar cookies hanya dikirim melalui HTTPS dengan pengaturan `SESSION_COOKIE_SECURE = True`.
        2. **HTTPOnly Cookies**: Cookies yang memiliki atribut *HttpOnly* hanya dapat diakses oleh server dan tidak oleh JavaScript, sehingga mencegah serangan *Cross-Site Scripting (XSS)*. Pengaturan `SESSION_COOKIE_HTTPONLY = True` pada Django mengaktifkan fitur ini.
        3. **SameSite Cookies**: Cookies dengan atribut *SameSite* mencegah pengiriman cookies lintas situs, yang dapat mengurangi risiko serangan *Cross-Site Request Forgery (CSRF)*.
        4. **Cookies yang Berbahaya**: Cookies dapat disalahgunakan untuk melacak pengguna tanpa izin mereka, yang sering menjadi perhatian privasi. Selain itu, jika cookies tidak diatur dengan baik (misalnya tanpa enkripsi atau HTTPOnly), mereka rentan terhadap serangan pihak ketiga.

- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    - Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
        1. `registrasi` <span style="font-family:Inter;"> -> </span> dilakukan dengan menambahkan fungsi pada `views.py`, yaitu
            ```python
            from django.contrib.auth.forms import UserCreationForm
            from django.contrib import messages

            def register(request):
                form = UserCreationForm()
                if request.method == "POST":
                    form = UserCreationForm(request.POST)
                    if form.is_valid():
                        form.save()
                        messages.success(request, 'Your account has been successfully created!')
                        return redirect('main:login')
                context = {'form':form}
                return render(request, 'register.html', context)
            ```
            lalu kita perlu menambahkan file `register.html` pada folder `templates` yang ada pada folder `main` yang berisi 
            ```html
            {% extends 'base.html' %}

            {% block meta %}
            <title>Register</title>
            {% endblock meta %}

            {% block content %}

            <div class="login">
            <h1>Register</h1>

            <form method="POST">
                {% csrf_token %}
                <table>
                {{ form.as_table }}
                <tr>
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar" /></td>
                </tr>
                </table>
            </form>

            {% if messages %}
            <ul>
                {% for message in messages %}
                <li>{{ message }}</li>
                {% endfor %}
            </ul>
            {% endif %}
            </div>

            {% endblock content %}
            ```
            hal terakhir yang kita butuhkan adalah kita harus mendefinisikan url yang akan memanggil fungsi serta mengembalikan response berupa file html. Hal ini dapat dilakukan dengan menambahkan path berikut pada `urlpatterns` pada `urls.py`
            ```python
            urlpatterns=[
                ..., 
                path('register/', register, name='register'),
            ]
            ```
        2. `login` <span style="font-family:Inter;"> -> </span> dilakukan dengan menambahkan fungsi pada `views.py`, yaitu
            ```python
            from django.contrib.auth.forms import ..., AuthenticationForm
            from django.http import ..., HttpResponseRedirect

            def login_user(request):
                if request.method == 'POST':
                    form = AuthenticationForm(data=request.POST)
                    if form.is_valid():
                        user = form.get_user()
                        login(request, user)
                        response = HttpResponseRedirect(reverse("main:show_main"))
                        response.set_cookie('last_login', str(datetime.datetime.now()))
                        return response
                else:
                form = AuthenticationForm(request)
                context = {'form': form}
                return render(request, 'login.html', context)
            ```
            lalu kita perlu menambahkan file `register.html` pada folder `templates` yang ada pada folder `main` yang berisi 
            ```html
            {% extends 'base.html' %}

            {% block meta %}
            <title>Login</title>
            {% endblock meta %}

            {% block content %}
            <div class="login">
            <h1>Login</h1>

            <form method="POST" action="">
                {% csrf_token %}
                <table>
                {{ form.as_table }}
                <tr>
                    <td></td>
                    <td><input class="btn login_btn" type="submit" value="Login" /></td>
                </tr>
                </table>
            </form>

            {% if messages %}
            <ul>
                {% for message in messages %}
                <li>{{ message }}</li>
                {% endfor %}
            </ul>
            {% endif %} Don't have an account yet?
            <a href="{% url 'main:register' %}">Register Now</a>
            </div>

            {% endblock content %}
            ```
            hal terakhir yang kita butuhkan adalah kita harus mendefinisikan url yang akan memanggil fungsi serta mengembalikan response berupa file html. Hal ini dapat dilakukan dengan menambahkan path berikut pada `urlpatterns` pada `urls.py`
            ```python
            urlpatterns=[
                ..., 
                path('login/', login_user, name='login'),
            ]
            ```
        3. `logout` <span style="font-family:Inter;"> -> </span> dilakukan dengan menambahkan fungsi pada `views.py`, yaitu
            ```python
            def logout_user(request):
                response = HttpResponseRedirect(reverse('main:login'))
                response.delete_cookie('last_login')
                logout(request)
                return redirect('main:login')
            ```
            lalu kita perlu menambahkan *button* pada file `main.html` yang berguna untuk memanggil fungsi `logout` dengan menambahkan 
            ```html
            <a href="{% url 'main:logout' %}">
                    <button class="logout-button">Logout</button>
            </a>
            ```
    - Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
        - Mendaftarkan akun user dengan melakukan registrasi akun ke dalam sistem melalui halaman `localhost:8000\register`.
        - Mendaftarkan product untuk user yang sudah login dengan menekan tombol `Add New Product`
    - Menghubungkan model Product dengan User.
        Dengan menambahkan atribut `User` sebagai `ForeignKey` pada object `Product`. Cara implementasinya adalah sebagai berikut:
        - Menambahkan kode di bawah ini pada `models.py`
            ```python
            from django.contrib.auth.models import User
            ....
            class Product(models.Model):
                user = models.ForeignKey(User, on_delete=models.CASCADE)
                .....
            ```
    - Menampilkan detail informasi pengguna yang sedang *logged in* seperti *username* dan menerapkan *cookies* seperti *last login* pada halaman utama aplikasi.
        - Menambahkan atribut pada `context` pada fungsi  `show_main` pada `views.py` dengan menambahkan 
            ```python
            def show_main(request):
                products = Product.objects.filter(user=request.user)
                context = {
                    'name':request.user.username,
                    ...,
                }
            ```
        - Menambahkan beberapa kode pada `main.html` untuk menampilkan beberapa detail informasi dari user yang telah login
            ```html
            <h3>Selamat datang, {{ name }}</h3>
            ```
        - Implementasi *cookies*
        <img src="./Tugas4/Cookies.png">
---
# Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS

- Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
    Urutan prioritas: 
    1. ID Selector (menggunakan # pada awal ID elemen)
    *Styling* yang dipakai dengan selector ini akan diprioritaskan paling pertama sehingga jika ada *styling* dengan menggunakan *class selector* maupun *element selector* akan ter-*overwrite* oleh *styling* dengan *ID selector*
    2. Class Selector (menggunakan . pada awal nama Class)
    *Styling* yang dipakai dengan selector ini akan diprioritaskan setelah *element selector* sehingga jika ada *styling* dengan menggunakan *element selector* akan ter-*overwrite* oleh *styling* dengan *class selector*. Namun, jika ada *styling* dengan *ID selector* maka tidak akan ter-*overwrite* oleh *styling* dengan *class selector*
    3. Element Selector (langsung menggunakan nama elemen saja)
    *Styling* yang dipakai dengan selector ini **tidak akan** diprioritaskan sehingga jika ada *styling* dengan menggunakan *class selector* atau *ID selector* maka styling dengan *element selector* ter-*overwrite* oleh *styling* dengan *class selector* atau *ID selector*.
- Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design sangat berpengaruh karena tidak semua pengguna dapat mengakses sebuah web melalui browser pada desktop. Oleh karena itu, responsive design akan menambah kenyamanan kepada pengguna. Sehingga pengguna tidak hanya bisa mengakses web dengan mudah melalui desktop, tetapi juga melalui mobile browser.
    - Contoh aplikasi web dengan responsive design : Scele
    - Contoh aplikasi web tanpa responsive design : Pacil Web Service 
- Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
    - Margin merupakan jarak yang didefinisikan sebagai jarak border sebuah elemen dengan elemen lain di luar tagnya (jarak dari luar objek)
    - Border merupakan batasan yang berada pada sebuah elemen dengan elemen di luar tagnya.
    - Padding merupakan jarak yang didefiniskan sebagai jarak border sebuah box atau container dengan item di dalamnya.
- Jelaskan konsep flex box dan grid layout beserta kegunaannya!
    - Flex box menggunakan konsep container yang dapat diatur penggunaannya secara horizontal atau vertical. Misal, kita ingin membuat sebuah gambar yang ditampilkan berurutan ke kanan. Maka kita dapat dengan mudah menggunakan flex box untuk membuatnya.
    - Grid layout menggunakan konsep container yang diatur dengan menggunakan koordinat sebagai tempat untuk sebuah elemen. Sebuah kombinasi (x,y) dapat diisi dengan sebuah elemen sehingga grid layout cocok digunakan untuk membuat catalog barang karena tidak hanya memerlukan design horizontal atau vertical melainkan design dengan menggabungkan keduanya sehingga gap serta tampilannya menjadi rapi.
- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
    - Implementasikan fungsi untuk menghapus dan mengedit product.
        1. Menambahkan fungsi `edit_product` pada `views.py` yang ada pada folder `main` dengan kode berikut.
            ```python
            def edit_product(request, id):
                product = Product.objects.get(pk = id)

                form = ProductForm(request.POST or None, instance=product)

                if form.is_valid() and request.method == "POST":
                    form.save()
                    return HttpResponseRedirect(reverse('main:show_main'))

                context = {'form': form}
                return render(request, "edit_product.html", context)
            ```
        2. Menambahkan path pada `urlpatterns` yang ada pada `urls.py` 
            ```python
            urlpatterns = [
                ....,
                path('edit-product/<uuid:id>', edit_product, name='edit_product'),
            ]
            ```
            Note: < uuid:id > digunakan untuk passing id ke dalam fungsi `edit_product`
        3. Menambahkan fungsi `delete_product` pada `views.py` yang ada pada folder `main` dengan kode berikut.
            ```python
            def delete_product(request, id):
                product = Product.objects.get(pk = id)
                product.delete()
                return HttpResponseRedirect(reverse('main:show_main'))

            ```
        4. Menambahkan path pada `urlpatterns` yang ada pada `urls.py` 
            ```python
            urlpatterns = [
                ....,
                path('delete/<uuid:id>', delete_product, name='delete_product'),
            ]
            ```
            Note: < uuid:id > digunakan untuk passing id ke dalam fungsi `delete_product`
        
    - Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:
        - Kustomisasi halaman login, register, dan tambah product semenarik mungkin.
        <img src="./Tugas5/LoginPage.png">
        <img src="./Tugas5/RegisterPage.png">
        <img src="./Tugas5/CreateProductPage.png">
        - Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. Kemudian, perhatikan kondisi berikut:
            - Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.
            <img src="./Tugas5/NoProductMobile.png">
            - Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!).
            <img src="./Tugas5/HomePage.png">
            <img src="./Tugas5/HomePageMobile.png">
        - Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!
        <img src="./Tugas5/CardProduct.png">
        - Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.
        <img src="./Tugas5/NavbarMobile.png">
        <img src="./Tugas5/NavbarDesktop.png">

---
# Tugas 6: JavaScript dan AJAX

- Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
JavaScript membantu *programmer web* untuk menambahkan interaksi user dengan web dimana JavaScript sebagai bahasa pemrograman tentunya menyediakan fitur untuk membuat logika yang dapat dibuat sebagai fungsi yang mengatur jalannya interaksi antara *user* dengan *web application*. Tanpa adanya JavaScript, *programmer web* akan sulit untuk membuat fitur interaksi dengan *web application* karena `HTML` dan `CSS` tidak mempunyai fitur logika pemrograman yang dapat diimplementasi ke dalam *web application* sebagai fitur interaksi.

- Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan `await`?
Penggunaan dari `await` adalah agar fungsi `fetch()` dijalankan sebagai fungsi asinkronus dimana fungsi `fetch()` dijalankan tanpa menunggu adanya *response* dari *endpoint* yang kita *passing* sebagai *argument* dalam fungsi `fetch()`. Hal ini memungkinkan *programmer* untuk menjalankan beberapa proses dalam suatu waktu tanpa harus menunggu fungsi `fetch()` me-*return* data dari endpoint. Fungsi `fetch()` dengan `await` akan me-*return* sebuah *object* `Promise` yang akan berubah menjadi *object* data `JSON` saat fungsi `fetch()` menerima *response* dari *web application* (*endpoint*).

- Mengapa kita perlu menggunakan decorator `csrf_exempt` pada `view` yang akan digunakan untuk AJAX `POST`?
Untuk exclude `view` dari pengecekan `csrf token`, karena saat kita menggunakan AJAX `POST` kita tidak bisa memasukkan input `csrf token` yang otomatis ter-*generate* oleh sistem *backend* dari django karena kita melakukan fetch tidak dari sistem django. Sehingga kita perlu meng-*exclude* `view` tersebut.

- Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (*backend*) juga. Mengapa hal tersebut tidak dilakukan di *frontend* saja?
Untuk mencegah masuknya data yang dapat mengganggu sistem baik sistem *backend* maupun *frontend*. Karena saat kita membersihkan data input pada *backend* kitaa memastikan bahwa data input tersebut sudah tidak mengandung data yang menyebabkan gangguan pada sistem sebelum kita memasukkan data tersebut ke *database* dari *web application* yang kita miliki.

- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
    - `AJAX GET`
        - Ubahlah kode cards data product agar dapat mendukung `AJAX GET`. Lakukan pengambilan data product menggunakan `AJAX GET`. Pastikan bahwa data yang diambil hanyalah data milik pengguna yang logged-in.
            1. Untuk mendapatkan data dari product dalam database kita perlu untuk membuat fungsi untuk mengambil data dari url API yang kita punya. untuk mendapatkan url API kita perlu membuat fungsi pada `views.py` yang berguna untuk mereturn response dalam bentuk JSON yang berisikan data product pada database sesuai keinginan kita yaitu product yang dimiliki oleh sebueh user. Setelah itu kita perlu mendefinisikan url yang sesuai sebagai url API yang nantinya kita panggil untuk mendapatkan data dari database.
            ```python
            def show_json(request):
                data = Product.objects.filter(user=request.user) # memilih data yang dimiliki oleh user
                return HttpResponse(serializers.serialize("json", data), content_type="application/json")
            ```
            2. Membuat fungsi untuk mendapatkan data dari database melalui url API yang telah kita definisikan sebelumnya. Hal ini dapat dilakukan dengan membuat fungsi berikut ini pada tag script dalam `main.html`. Kita menggunakan fungsi async agar kita tidak perlu menunggu response dari url API untuk melanjutkan program yang lain (asinkronus/non-blocking).
                ```javascript
                async function getProducts(){
                    return fetch("{% url 'main:show_json' %}").then((res) => res.json());
                }
                ```
            3. Untuk membuat cards yang nantinya dapat membuat data yang kita dapatkan menggunakan `AJAX GET` kita perlu mengubah yang sebelumnya kita menggunakan `card_product.html` sekarang kita memerlukan javascript untuk menghandle tampilan dari card product. Hal tersebut dapat kita buat dengan memasukkan kode yang kita miliki di dalam `card_product.html` ke dalam sebuah fungsi yaitu `refreshProduct()`
                ```javascript
                async function refreshProducts() {
                    document.getElementById("product_cards").innerHTML = "";
                    document.getElementById("product_cards").className = "";
                    const products = await getProducts();
                    let htmlString = "";
                    let classNameString = "";
                
                    if (products.length === 0) {
                        classNameString = "fixed flex flex-col justify-center items-center gap-2 left-1/2 bottom-1/3 -translate-x-1/2 translate-y-1/2";
                        htmlString = `
                            <img src="{% static "/icons/no-product.png" %}" alt="" class="h-auto w-28 ">
                            <p class="font-bold text-white text-lg text-center">Belum ada data products pada Sportify.</p>
                        `;
                    }
                    else {
                        classNameString = "relative w-full h-full text-white grid grid-cols-[repeat(auto-fill,345px)] grid-rows-[repeat(auto-fill,160px)] gap-4 pt-2 justify-evenly items-center overflow-y-scroll pl-4"
                        products.forEach((item) => {
                            const name = DOMPurify.sanitize(item.fields.name);
                            const description = DOMPurify.sanitize(item.fields.description);
                            htmlString += `<div class="w-full h-40 bg-[#ffffff17] rounded-2xl text-white flex justify-evenly items-center cursor-pointer">
                            <div class="w-28 h-28 bg-[#3b3d445d] rounded-2xl">
                            </div>
                            <div class="relative w-48 flex flex-col gap-1 group">
                                <h1 class="text-[1.5rem] font-semibold">${name}</h1>
                                <p class="truncate">${description}</p>
                                <p class="font-medium">Rp ${item.fields.price}</p>
                                <p class="product-stock">Stock : ${item.fields.stock}</p>
                                <div class="absolute right-0 -bottom-1 flex justify-between items-center h-9">
                                    <div class="hidden group-hover:flex gap-3">
                                        <a class="h-9 w-auto rounded-full flex justify-center items-center p-2 bg-[#ffffff17] cursor-pointer group" href="/delete/${item.pk}">
                                            <img src="{% static "/icons/delete.png" %}" alt="" class="h-full w-auto">
                                        </a>
                                        <a class="h-9 w-auto rounded-full flex justify-center items-center p-2 bg-[#ffffff17] cursor-pointer" href="edit/${item.pk}">
                                            <img src="{% static "/icons/edit.png" %}" alt="" class="h-full w-auto">
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>`;
                        });
                    }
                    document.getElementById("product_cards").className = classNameString;
                    document.getElementById("product_cards").innerHTML = htmlString;
                }
                ```  

    - `AJAX POST`
        - Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan product.
            1. Membuat button pada `main.html` dengan menambahkan prop onclick yang berisikan "showModal();". Nantinya fungsi showModal() akan berisikan.
                ```javascript
                function showModal(){
                    const modal = document.getElementById('crudModal'); // mengambil element html dengan id crudModal
                    modal.classList.remove('hidden');
                    modal.classList.add('flex');
                }
                ```
            2. Nantinya element dengan id crudModal akan berisikan modal yang ada kita tampilkan yaitu seperti dibawah ini.
                ```html
                    <div id="crudModal" class="hidden fixed w-full h-full justify-center items-center top-0 bg-[#ffffff17] backdrop-blur-sm pt-16">
                        <div class=" relative h-[40rem] w-[21rem] flex-col items-center justify-center bg-[#ffffff17] py-12 px-4 m-auto font-[Inter] rounded-3xl sm:px-6 sm:w-[30rem] lg:px-8">
                            <button id="back-button" class="absolute top-3 left-3 rounded-full p-1 bg-[#ffffff17] h-10 w-10 flex justify-center items-center text-xl font-bold text-white cursor-pointer" onclick="hideModal();"><-</button>
                            <h1 class="text-center text-white text-2xl font-extrabold">Create Product</h1>
                            <form method="POST" class="space-y-3 flex flex-col gap-1" id="productForm">
                                <div class="">
                                    <label for="name" class="font-semibold text-white">Name</label>
                                    <input type="text" id="name" name="name" class="appearance-none relative block w-full px-3 py-2 border border-transparent placeholder-white text-white rounded-xl focus:outline-none focus:border focus:ring-[#22c55ea6] focus:border-[#22c55ea6] bg-[#ffffff17] focus:z-10 sm:text-sm" placeholder="Enter product name" required>
                                </div>
                                <div class="">
                                    <label for="price" class="font-semibold text-white">Price</label>
                                    <input type="number" id="price" name="price" class="appearance-none relative block w-full px-3 py-2 border border-transparent placeholder-white text-white rounded-xl focus:outline-none focus:border focus:ring-[#22c55ea6] focus:border-[#22c55ea6] bg-[#ffffff17] focus:z-10 sm:text-sm" required placeholder="Enter product price">
                                </div>
                                <div class="">
                                    <label for="description" class="font-semibold text-white">Description</label>
                                    <textarea id="description" name="description" rows="3" class="h-36 appearance-none relative block w-full px-3 py-2 border border-transparent placeholder-white 0 text-white rounded-xl focus:outline-none focus:border focus:ring-[#22c55ea6] focus:border-[#22c55ea6] bg-[#ffffff17] focus:z-10 sm:text-sm" placeholder="Enter product description" required></textarea>
                                </div>
                                <div class="">
                                    <label for="stock" class="font-semibold text-white">Stock</label>
                                    <input type="number" id="stock" name="stock" class="appearance-none relative block w-full px-3 py-2 border border-transparent placeholder-white text-white rounded-xl focus:outline-none focus:border focus:ring-[#22c55ea6] focus:border-[#22c55ea6] bg-[#ffffff17] focus:z-10 sm:text-sm" required placeholder="Enter product stock">
                                </div>
                                <div class="flex justify-center items-center">
                                    <button type="submit" class="relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-xl text-white bg-[#22c55ea6] hover:bg-[#acf0c5a6] hover:text-black focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#22c55ea6] mt-10">
                                    Create Product
                                    </button>
                                </div>
                            </form>
                        </div>
                    </div>
                ```

        - Buatlah fungsi `view` baru untuk menambahkan product baru ke dalam basis data. Buatlah path `/create-ajax/` yang mengarah ke fungsi `view` yang baru kamu buat.
            1. Membuat fungsi pada `views.py` pada folder `main` yang berisikan.
                ```python
                @csrf_exempt # untuk meng-exclude fungsi di bawah dari pengecekan csrf token 
                @require_POST # memastikan fungsi di bawah hanya dapat dipanggil jika request dengan POST method
                def create_product_with_ajax(request):
                    name = strip_tags(request.POST.get("name"))
                    price = request.POST.get("price")
                    description = strip_tags(request.POST.get("description"))
                    stock = request.POST.get("stock")
                    user = request.user
                    
                    new_product = Product(
                        name = name, 
                        price = price,
                        description = description,
                        stock = stock,
                        user = user
                    )
                    new_product.save()
                    
                    return HttpResponse(b"CREATED", status=201)
                ```
            2. Mendefinisikan url pada `urls.py` dengan menambahkan block kode berikut pada `urlpatterns`
                ```python
                urlpatterns=[
                    ...,
                    path('create-ajax', create_product_with_ajax, name='create_product_with_ajax'),
                ]
                ```
        - Hubungkan form yang telah kamu buat di dalam modal kamu ke path `/create-ajax/`.
            Untuk menghubungkan form yang telah dibuat pada modal kita perlu menambahkan fungsi javascript yang digunakan untuk melakukan POST ke dalam server lalu memanggil fungsi `refreshProduct()` setelah fetch berhasil dilakukan. Nantinya kita perlu menambahkan event listener ke dalam productForm yaitu saat button submit ditekan. Hal ini dapat dilakukan dengan menambahkan fungsi dibawah ini pada tag script di file `main.html`.
            ```javascript
            function addProduct() {
                fetch("{% url 'main:create_product_with_ajax' %}", {
                method: "POST",
                body: new FormData(document.querySelector('#productForm')),
                })
                .then(response => refreshProducts())
            
                document.getElementById("productForm").reset(); 
                document.querySelector("#back-button").click();
            
                return false;
            }
            document.getElementById("productForm").addEventListener("submit", (e) => {
                e.preventDefault();
                addProduct();
            })
            ```
        - Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar product terbaru tanpa reload halaman utama secara keseluruhan.
            Kita dapat menambahkan kode dibawah ini untuk membuat fungsi yang berguna untuk merefresh tampilan dari halaman utama
            ```javascript
            async function refreshProducts() {
                document.getElementById("product_cards").innerHTML = "";
                document.getElementById("product_cards").className = "";
                const products = await getProducts();
                let htmlString = "";
                let classNameString = "";
            
                if (products.length === 0) {
                    classNameString = "fixed flex flex-col justify-center items-center gap-2 left-1/2 bottom-1/3 -translate-x-1/2 translate-y-1/2";
                    htmlString = `
                        <img src="{% static "/icons/no-product.png" %}" alt="" class="h-auto w-28 ">
                        <p class="font-bold text-white text-lg text-center">Belum ada data products pada Sportify.</p>
                    `;
                }
                else {
                    classNameString = "relative w-full h-full text-white grid grid-cols-[repeat(auto-fill,345px)] grid-rows-[repeat(auto-fill,160px)] gap-4 pt-2 justify-evenly items-center overflow-y-scroll pl-4"
                    products.forEach((item) => {
                        const name = DOMPurify.sanitize(item.fields.name);
                        const description = DOMPurify.sanitize(item.fields.description);
                        htmlString += `<div class="w-full h-40 bg-[#ffffff17] rounded-2xl text-white flex justify-evenly items-center cursor-pointer">
                        <div class="w-28 h-28 bg-[#3b3d445d] rounded-2xl">
                        </div>
                        <div class="relative w-48 flex flex-col gap-1 group">
                            <h1 class="text-[1.5rem] font-semibold">${name}</h1>
                            <p class="truncate">${description}</p>
                            <p class="font-medium">Rp ${item.fields.price}</p>
                            <p class="product-stock">Stock : ${item.fields.stock}</p>
                            <div class="absolute right-0 -bottom-1 flex justify-between items-center h-9">
                                <div class="hidden group-hover:flex gap-3">
                                    <a class="h-9 w-auto rounded-full flex justify-center items-center p-2 bg-[#ffffff17] cursor-pointer group" href="/delete/${item.pk}">
                                        <img src="{% static "/icons/delete.png" %}" alt="" class="h-full w-auto">
                                    </a>
                                    <a class="h-9 w-auto rounded-full flex justify-center items-center p-2 bg-[#ffffff17] cursor-pointer" href="edit/${item.pk}">
                                        <img src="{% static "/icons/edit.png" %}" alt="" class="h-full w-auto">
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>`;
                    });
                }
                document.getElementById("product_cards").className = classNameString;
                document.getElementById("product_cards").innerHTML = htmlString;
                }
            ```
            kita juga perlu memanggil fungsi `refreshProduct()` setelah kita melakukan submit form product dengan menambahkan
            ```javascript
            fetch("{% url 'main:create_product_with_ajax' %}", {
                method: "POST",
                body: new FormData(document.querySelector('#productForm')),
                })
                .then(response => refreshProducts()) // refreshProduct dipanggil setelah fetch berhasil
            ```