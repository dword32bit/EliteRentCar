from flask import Flask, render_template, request, url_for, session, redirect, flash
from flask_login import login_required
from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
from mysql import connector
import mysql.connector
import os

UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

conn = connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='rental'
)
cursor = conn.cursor()

app.secret_key = 'tahutempe'
if conn.is_connected():
    print('open connection succesfull')

# Fungsi untuk memeriksa ekstensi file yang diunggah


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Azkal


# Home
@app.route('/')
def index():
    return render_template('new/index.html', active_page='index')


@app.route('/about')
def about():
    return render_template('new/about.html', active_page='index')


# Old code
@app.route('/tampilan_user')
def tmpuser():
    return render_template('new/index.html', active_page='index')


@app.route('/biodata/', methods=['GET', 'POST'])
def tempat():
    if request.method == 'GET':
        return render_template('biodata.html')
    else:
        nik = request.form['nik']
        awal = request.form['awal']
        akhir = request.form['akhir']
        temphir = request.form['temphir']
        taghir = request.form['taghir']
        dusun = request.form['dusun']
        provinsi = request.form['provinsi']
        kota = request.form['kota']
        kecamatan = request.form['kecamatan']
        kelurahan = request.form['kelurahan']

        session['nik'] = nik

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM biodata WHERE nik = %s", (nik,))
        data = cursor.fetchone()

        if data is None:
            cursor.execute("INSERT INTO biodata (nik, nama_awal, nama_akhir, tempat_lahir, tanggal_lahir, dusun, provinsi, kabupaten, kecamatan, kelurahan) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           (nik, awal, akhir, temphir, taghir, dusun, provinsi, kota, kecamatan, kelurahan))
            conn.commit()
        else:
            flash('NIK Sudah Digunakan', 'danger')
            return (render_template('biodata.html'))
        return redirect(url_for('pendaftaran'))


@app.route('/pendaftaran/', methods=['GET', 'POST'])
def pendaftaran():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if 'nik' in session:
            nik = session['nik']
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM accounts WHERE username=%s OR email=%s', (username, email, ))
            akun = cursor.fetchone()
            if akun is None:
                cursor.execute('INSERT INTO accounts (username, email, password, nik) VALUES (%s, %s, %s, %s)', (username, email, password, nik))
                conn.commit()
                flash('Registrasi Berhasil', 'success')
            else:
                flash('Username Sudah Digunakan', 'danger')
            session.pop('nik', None)
        else:
            flash('Data NIK belum diisi di halaman biodata', 'danger')
    return (render_template('new/register.html'))


def user_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'sewa1' not in session:
            return redirect('/booking')
        return f(*args, **kwargs)
    return decorated_function


@app.route('/login/', methods=['GET', 'POST'])
def login():
    # msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = conn.cursor()
        cursor.execute(
            'SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        account = cursor.fetchone()
        if account:
            session['username'] = username
            session['password'] = password
            cursor.execute('SELECT accounts.nik, biodata.nama_awal FROM accounts INNER JOIN biodata ON accounts.nik=biodata.nik where accounts.username = %s and accounts.password = %s', (username, password,))
            biodata = cursor.fetchone()
            if biodata:
                session['username'] = biodata[1]
                session['nik'] = biodata[0]
                session['loggedin'] = True
            return redirect(url_for('user'))
        else:
            flash("Username / password salah!")
    return render_template('new/login.html')

@app.route('/reset/', methods=['GET', 'POST'])
def reset():
    if request.method == 'POST':
        username = request.form['username']
        nik = request.form['nik']
        taghir = request.form['taghir']
        cursor = conn.cursor()
        cursor.execute(
            'SELECT accounts.username, biodata.nik, biodata.tempat_lahir from accounts inner join biodata on accounts.username = %s AND biodata.nik = %s AND biodata.tanggal_lahir = %s', (username, nik, taghir))
        akun = cursor.fetchone()
        cursor.close()

        if akun is None:
            return render_template('new/reset_password.html', error='Data tidak cocok. Silahkan coba lagi')

        new_pws = request.form['new_pws']
        cursor = conn.cursor()
        cursor.execute(
            'update accounts set password = %s where username =%s', (new_pws, username))
        conn.commit()
        cursor.close()

        return render_template('new/login.html', success='password telah diubah')

    return render_template('new/reset_password.html')

# Azkal


# car
@app.route('/explore/', methods=['GET', 'POST'])
def car():
    if request.method == 'POST':
        nik = request.form['nik']
        jenis_mobil = request.form['nama_mobil']
        tanggal_pickup = request.form['tanggal_pickup']
        jam_pickup = request.form['jam_pickup']
        tanggal_dropoff = request.form['tanggal_dropoff']
        jam_dropoff = request.form['jam_dropoff']
        try:
            cursor = conn.cursor()
            query = "SELECT harga_sewa_per_jam FROM car WHERE nama_mobil = %s"
            cursor.execute(query, (jenis_mobil,))
            harga_sewa_per_jam = cursor.fetchone()[0]
            pickup_datetime = datetime.strptime(
                tanggal_pickup + " " + jam_pickup, '%Y-%m-%d %H:%M')
            dropoff_datetime = datetime.strptime(
                tanggal_dropoff + " " + jam_dropoff, '%Y-%m-%d %H:%M')
            selisih_waktu = dropoff_datetime - pickup_datetime
            selisih_jam = selisih_waktu.total_seconds() / 3600
            total_biaya = 0
            if selisih_jam <= 24:
                total_biaya = harga_sewa_per_jam * selisih_jam
            else:
                harga_per_hari = 24 * harga_sewa_per_jam
                total_biaya += harga_per_hari
                jumlah_hari = selisih_waktu.days
                total_biaya += harga_per_hari * (jumlah_hari - 1)
                sisa_jam = selisih_jam % 24
                total_biaya += harga_sewa_per_jam * sisa_jam
            # Save data to the database
            insert_query = "INSERT INTO cobapesanan (nik, jenis_mobil, tanggal_pickup, jam_pickup, tanggal_dropoff, jam_dropoff, harga_sewa_per_jam, total_biaya) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (nik, jenis_mobil, tanggal_pickup, jam_pickup,
                           tanggal_dropoff, jam_dropoff, harga_sewa_per_jam, total_biaya))
            conn.commit()
            return redirect('/hasilbooking?jenis_mobil={}&tanggal_pickup={}&jam_pickup={}&tanggal_dropoff={}&jam_dropoff={}&harga_sewa_per_jam={}&total_biaya={}'.format(
                jenis_mobil, tanggal_pickup, jam_pickup, tanggal_dropoff, jam_dropoff, harga_sewa_per_jam, total_biaya))
        except conn.Error as err:
            print(err)
        finally:
            cursor.close()
    # Ambil parameter filter tipe mobil dan pengurutan harga
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM car")
    mobil_list_user = cursor.fetchall()
    filter_tipe = request.args.get('filter_tipe')
    sort_harga = request.args.get('sort_harga')
    # Buat query SQL dengan filter dan pengurutan
    query = "SELECT * FROM car"
    if filter_tipe:
        query += f" WHERE Tipe_Mobil = '{filter_tipe}'"
    if sort_harga:
        query += " ORDER BY Harga_Sewa_Per_jam ASC" if sort_harga == 'asc' else " ORDER BY Harga_Sewa_Per_jam DESC"
    # Eksekusi query
    cursor.execute(query)
    mobil_list = cursor.fetchall()
    # Ambil daftar tipe mobil untuk filter
    cursor.execute("SELECT DISTINCT Tipe_Mobil FROM car")
    tipe_mobil_list = cursor.fetchall()
    return render_template('new/explore.html', mobil_list=mobil_list, tipe_mobil_list=tipe_mobil_list, active_page='car', mobil_list_user=mobil_list_user)


# Coba Fery
# Decorator untuk memeriksa apakah admin sudah login atau belum
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin' not in session:
            return redirect('/login/admin')
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login/admin', methods=['GET', 'POST'])
def login_admin():
    if 'admin' in session:
        return redirect('/admin')
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Query untuk mencari admin berdasarkan username dan password
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM admin WHERE username = %s AND password = %s", (username, password))
        admin = cursor.fetchone()
        cursor.close()
        if admin:
            # Simpan admin yang berhasil login dalam session
            session['admin'] = admin
            return redirect('/admin')
        else:
            error = 'Username atau password salah'
    return render_template('admin/login.html', error=error)

# Logout admin


@app.route('/logout')
def logout():
    # Hapus admin dari session
    session.pop('admin', None)
    return redirect('/')

# Halaman kontrol admin


@app.route('/admin')
@login_required
def admin():
    # Ambil daftar mobil dari database
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM car')
    mobil_list = cursor.fetchall()
    cursor.close()
    # Hitung jumlah mobil tersedia dan tidak tersedia
    tersedia = sum(mobil[6] == 1 for mobil in mobil_list)
    tidak_tersedia = sum(mobil[6] == 0 for mobil in mobil_list)
    # Ambil jumlah user dari database
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM accounts')
    user_count = cursor.fetchone()[0]
    cursor.close()
    # Ambil jumlah pesanan dari database
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM cobapesanan')
    pesanan_count = cursor.fetchone()[0]
    cursor.close()
    # Ambil jumlah mobil dari database
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM car')
    mobil_count = cursor.fetchone()[0]
    cursor.close()
    cursor = conn.cursor()
    cursor.execute('SELECT SUM(total_biaya) FROM cobapesanan')
    pendapatan_count = cursor.fetchone()[0]
    cursor.close()
    return render_template('admin.html', mobil_list=mobil_list, user_count=user_count, pesanan_count=pesanan_count, mobil_count=mobil_count, tersedia=tersedia, tidak_tersedia=tidak_tersedia, pendapatan_count=pendapatan_count)


# Tampilan form tambah mobil
@app.route('/tambah_mobil', methods=['GET', 'POST'])
@login_required
def tambah_mobil():
    if request.method == 'POST':
        # Ambil data dari form
        plat_mobil = request.form['plat']
        nama_mobil = request.form['nama']
        tipe_mobil = request.form['tipe']
        tahun_pembuatan = request.form['tahun']
        harga_sewa = request.form['harga']
        ketersediaan = request.form['ketersediaan']
        gambar = request.files['gambar']
        warna = request.form['warna']
        # Simpan gambar ke folder 'static/images'
        if gambar and allowed_file(gambar.filename):
            filename = secure_filename(gambar.filename)
            gambar.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Simpan data mobil baru ke database
        cursor.execute("INSERT INTO car (plat_mobil, nama_mobil, tipe_mobil, tahun_pembuatan, harga_sewa_per_jam, status_ketersediaan, gambar, warna) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                       (plat_mobil, nama_mobil, tipe_mobil, tahun_pembuatan, harga_sewa, ketersediaan, filename, warna))
        conn.commit()
        return redirect('/admin')
    else:
        return render_template('tambah_mobil.html')

# Hapus mobil


@app.route('/hapus_mobil/<int:id>', methods=['POST'])
@login_required
def hapus_mobil(id):
    # Hapus mobil dari database berdasarkan ID
    cursor.execute('DELETE FROM car WHERE ID_Mobil = %s', (id,))
    conn.commit()
    return redirect('/admin')

@app.route('/hapus_pengguna/<username>', methods=['POST'])
@login_required
def hapus_pengguna(username):
    # Hapus mobil dari database berdasarkan ID
    cursor.execute('DELETE FROM accounts WHERE username = %s', (username,))
    conn.commit()
    return redirect('/pengguna')

# Ubah mobil
@app.route('/ubah_mobil/<int:id>', methods=['GET', 'POST'])
@login_required
def ubah_mobil(id):
    if request.method == 'POST':
        # Ambil data dari form
        nama_mobil = request.form['nama']
        tipe_mobil = request.form['tipe']
        tahun_pembuatan = request.form['tahun']
        harga_sewa = request.form['harga']
        ketersediaan = request.form['ketersediaan']
        gambar = request.files['gambar']
        warna = request.form['warna']
        # Ambil data mobil dari database berdasarkan ID
        cursor.execute('SELECT * FROM car WHERE ID_Mobil = %s', (id,))
        mobil = cursor.fetchone()
        # Simpan gambar ke folder 'static/images' jika ada perubahan gambar
        if gambar and gambar.filename and allowed_file(gambar.filename):
            filename = secure_filename(gambar.filename)
            gambar.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Hapus gambar lama jika ada
            if mobil[7] and mobil[7] != 'default.jpg':
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], mobil[7]))
        else:
            # Jika tidak ada perubahan gambar, gunakan gambar lama
            filename = mobil[7]
        # Update data mobil ke database
        cursor.execute("UPDATE car SET Nama_Mobil = %s, Tipe_Mobil = %s, Tahun_Pembuatan = %s, Harga_Sewa_Per_Jam = %s, Status_Ketersediaan = %s, Gambar = %s, warna = %s WHERE ID_Mobil = %s",
                       (nama_mobil, tipe_mobil, tahun_pembuatan, harga_sewa, ketersediaan, filename, warna, id))
        conn.commit()
        return redirect('/admin')
    else:
        # Ambil data mobil dari database berdasarkan ID
        cursor.execute('SELECT * FROM car WHERE ID_Mobil = %s', (id,))
        mobil = cursor.fetchone()
        return render_template('ubah_mobil.html', mobil=mobil)


@app.route('/explore/')
def user():
    return render_template('new/explore.html')


@app.route('/mobil/')
def mobil():
    # Ambil parameter filter tipe mobil dan pengurutan harga
    cursor = conn.cursor()
    filter_tipe = request.args.get('filter_tipe')
    sort_harga = request.args.get('sort_harga')
    # Buat query SQL dengan filter dan pengurutan
    query = "SELECT * FROM car"
    if filter_tipe:
        query += f" WHERE Tipe_Mobil = '{filter_tipe}'"
    if sort_harga:
        query += " ORDER BY Harga_Sewa_Per_jam ASC" if sort_harga == 'asc' else " ORDER BY Harga_Sewa_Per_jam DESC"
    # Eksekusi query
    cursor.execute(query)
    mobil_list = cursor.fetchall()
    # Ambil daftar tipe mobil untuk filter
    cursor.execute("SELECT DISTINCT Tipe_Mobil FROM car")
    tipe_mobil_list = cursor.fetchall()
    return render_template('mobil.html', mobil_list=mobil_list, tipe_mobil_list=tipe_mobil_list, active_page='car')


@app.route('/logout_user')
def logout_user():
    session.pop('username', None)
    session.pop('password', None)
    session.pop('loggedin', None)
    return redirect(url_for('login'))


@app.route('/sampah')
def sampah():
    cursor = conn.cursor
    cursor.execute("SELECT * FROM pesan")
    booking_list = cursor.fetchall()
    cursor.close()
    return render_template('sampah.html', booking_list=booking_list)

@app.route('/hasilbooking')
def hasil1():
    jenis_mobil = request.args.get('jenis_mobil')
    tanggal_pickup = request.args.get('tanggal_pickup')
    jam_pickup = request.args.get('jam_pickup')
    tanggal_dropoff = request.args.get('tanggal_dropoff')
    jam_dropoff = request.args.get('jam_dropoff')
    harga_sewa_per_jam = float(request.args.get('harga_sewa_per_jam'))
    total_biaya = float(request.args.get('total_biaya'))
    return render_template('hasilbooking.html', jenis_mobil=jenis_mobil, tanggal_pickup=tanggal_pickup, jam_pickup=jam_pickup,
                           tanggal_dropoff=tanggal_dropoff, jam_dropoff=jam_dropoff, harga_per_jam=harga_sewa_per_jam,
                           total_biaya=total_biaya)


@app.route('/buka')
def buka():
    return render_template('booking.html')


@app.route('/pengguna')
def pengguna():
    cursor.execute("""
        SELECT accounts.username, accounts.email, biodata.nama_awal, biodata.nama_akhir, biodata.dusun, biodata.kelurahan, biodata.kecamatan, biodata.kabupaten, biodata.provinsi
        FROM accounts
        INNER JOIN biodata ON accounts.nik = biodata.nik
    """)
    pengguna_list = cursor.fetchall()

    return render_template('pengguna.html', pengguna_list=pengguna_list)


@app.route('/pesanan')
def pesanan():
    cursor.execute("""
        SELECT accounts.username, accounts.email,  biodata.nama_awal, biodata.nama_akhir, biodata.nik, biodata.dusun, biodata.kelurahan, biodata.kecamatan, biodata.kabupaten, biodata.provinsi, cobapesanan.*
        FROM cobapesanan
        INNER JOIN biodata ON cobapesanan.nik = biodata.nik
        INNER JOIN accounts ON biodata.nik = accounts.nik
    """)
    pesanan_list = cursor.fetchall()

    return render_template('pesanan.html', pesanan_list=pesanan_list)


# coba
@app.route('/pesan')
def pesan():
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM cobapesanan"
        cursor.execute(query)
        pesan_list = cursor.fetchall()
        cursor.close()
        return render_template('pesan.html', pesan_list=pesan_list)
    except conn.Error as err:
        print(err)


@app.route('/sewa', methods=['GET', 'POST'])
def sewa():
    if request.method == 'POST':
        jenis_mobil = request.form['nama_mobil']
        tanggal_pickup = request.form['tanggal_pickup']
        jam_pickup = request.form['jam_pickup']
        tanggal_dropoff = request.form['tanggal_dropoff']
        jam_dropoff = request.form['jam_dropoff']
        try:
            cursor = conn.cursor()
            query = "SELECT harga_sewa_per_jam FROM car WHERE nama_mobil = %s"
            cursor.execute(query, (jenis_mobil,))
            harga_sewa_per_jam = cursor.fetchone()[0]
            pickup_datetime = datetime.strptime(
                tanggal_pickup + " " + jam_pickup, '%Y-%m-%d %H:%M')
            dropoff_datetime = datetime.strptime(
                tanggal_dropoff + " " + jam_dropoff, '%Y-%m-%d %H:%M')
            selisih_waktu = dropoff_datetime - pickup_datetime
            selisih_jam = selisih_waktu.total_seconds() / 3600
            total_biaya = 0
            if selisih_jam <= 24:
                total_biaya = harga_sewa_per_jam * selisih_jam
            else:
                harga_per_hari = 24 * harga_sewa_per_jam
                total_biaya += harga_per_hari
                jumlah_hari = selisih_waktu.days
                total_biaya += harga_per_hari * (jumlah_hari - 1)
                sisa_jam = selisih_jam % 24
                total_biaya += harga_sewa_per_jam * sisa_jam
            # Simpan data ke tabel "pesanan"
            insert_query = "INSERT INTO pesanan (jenis_mobil, tanggal_pickup, jam_pickup, tanggal_dropoff, jam_dropoff, harga_per_jam, total_biaya) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (jenis_mobil, tanggal_pickup, jam_pickup,
                           tanggal_dropoff, jam_dropoff, harga_sewa_per_jam, total_biaya))
            conn.commit()
            return redirect('/hasil?jenis_mobil={}&tanggal_pickup={}&jam_pickup={}&tanggal_dropoff={}&jam_dropoff={}&harga_sewa_per_jam={}&total_biaya={}'.format(
                jenis_mobil, tanggal_pickup, jam_pickup, tanggal_dropoff, jam_dropoff, harga_sewa_per_jam, total_biaya))
        except mysql.connector.Error as err:
            print(err)
        finally:
            cursor.close()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM car")
    mobil_list = cursor.fetchall()
    cursor.close()
    return render_template('sewa.html', mobil_list=mobil_list)


@app.route('/booking', methods=['GET', 'POST'])
def sewa1():
    if request.method == 'POST':
        jenis_mobil = request.form['nama_mobil']
        tanggal_pickup = request.form['tanggal_pickup']
        jam_pickup = request.form['jam_pickup']
        tanggal_dropoff = request.form['tanggal_dropoff']
        jam_dropoff = request.form['jam_dropoff']

        try:
            cursor = conn.cursor()
            query = "SELECT harga_sewa_per_jam FROM car WHERE nama_mobil = %s"
            cursor.execute(query, (jenis_mobil,))
            harga_sewa_per_jam = cursor.fetchone()[0]

            pickup_datetime = datetime.strptime(
                tanggal_pickup + " " + jam_pickup, '%Y-%m-%d %H:%M')
            dropoff_datetime = datetime.strptime(
                tanggal_dropoff + " " + jam_dropoff, '%Y-%m-%d %H:%M')
            selisih_waktu = dropoff_datetime - pickup_datetime
            selisih_jam = selisih_waktu.total_seconds() / 3600

            total_biaya = 0
            if selisih_jam <= 24:
                total_biaya = harga_sewa_per_jam * selisih_jam
            else:
                harga_per_hari = 24 * harga_sewa_per_jam
                total_biaya += harga_per_hari
                jumlah_hari = selisih_waktu.days
                total_biaya += harga_per_hari * (jumlah_hari - 1)
                sisa_jam = selisih_jam % 24
                total_biaya += harga_sewa_per_jam * sisa_jam

            return redirect('/hasilbooking?jenis_mobil={}&tanggal_pickup={}&jam_pickup={}&tanggal_dropoff={}&jam_dropoff={}&harga_sewa_per_jam={}&total_biaya={}'.format(
                jenis_mobil, tanggal_pickup, jam_pickup, tanggal_dropoff, jam_dropoff, harga_sewa_per_jam, total_biaya))
        finally:
            cursor.close()

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM car")
    mobil_list = cursor.fetchall()
    cursor.close()
    return render_template('booking.html', mobil_list=mobil_list)

@app.route('/cobasewa1', methods=['GET', 'POST'])
def cobasewa1():
    if request.method == 'POST':
        nik = request.form['nik']
        jenis_mobil = request.form['nama_mobil']
        tanggal_pickup = request.form['tanggal_pickup']
        jam_pickup = request.form['jam_pickup']
        tanggal_dropoff = request.form['tanggal_dropoff']
        jam_dropoff = request.form['jam_dropoff']
        try:
            cursor = conn.cursor()
            query = "SELECT harga_sewa_per_jam FROM car WHERE nama_mobil = %s"
            cursor.execute(query, (jenis_mobil,))
            harga_sewa_per_jam = cursor.fetchone()[0]
            pickup_datetime = datetime.strptime(
                tanggal_pickup + " " + jam_pickup, '%Y-%m-%d %H:%M')
            dropoff_datetime = datetime.strptime(
                tanggal_dropoff + " " + jam_dropoff, '%Y-%m-%d %H:%M')
            selisih_waktu = dropoff_datetime - pickup_datetime
            selisih_jam = selisih_waktu.total_seconds() / 3600
            total_biaya = 0
            if selisih_jam <= 24:
                total_biaya = harga_sewa_per_jam * selisih_jam
            else:
                harga_per_hari = 24 * harga_sewa_per_jam
                total_biaya += harga_per_hari
                jumlah_hari = selisih_waktu.days
                total_biaya += harga_per_hari * (jumlah_hari - 1)
                sisa_jam = selisih_jam % 24
                total_biaya += harga_sewa_per_jam * sisa_jam
            # Save data to the database
            insert_query = "INSERT INTO cobapesanan (nik, jenis_mobil, tanggal_pickup, jam_pickup, tanggal_dropoff, jam_dropoff, harga_sewa_per_jam, total_biaya) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (nik, jenis_mobil, tanggal_pickup, jam_pickup,
                           tanggal_dropoff, jam_dropoff, harga_sewa_per_jam, total_biaya))
            conn.commit()
            return redirect('/hasilbooking?jenis_mobil={}&tanggal_pickup={}&jam_pickup={}&tanggal_dropoff={}&jam_dropoff={}&harga_sewa_per_jam={}&total_biaya={}'.format(
                jenis_mobil, tanggal_pickup, jam_pickup, tanggal_dropoff, jam_dropoff, harga_sewa_per_jam, total_biaya))
        except conn.Error as err:
            print(err)
        finally:
            cursor.close()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM car")
    mobil_list = cursor.fetchall()
    cursor.close()
    return render_template('booking_user.html', mobil_list=mobil_list)


if __name__ == '__main__':
    app.run()
