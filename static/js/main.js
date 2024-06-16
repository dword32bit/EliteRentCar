//https://api.telegram.org/bot5638633198:AAHhjPxdjq6_XgaoKAqMUcxY9oMFf05SPxU/sendMessage?chat_id=-862216614&text=Halo%0AJuga&parse_mode=html

//Nama%20%3A%20xxx%0ANomor%20WhatsApps%20%3A%20xxx%0AEmail%20%3A%20xxx%0AMobil%20%3A%20xxx%0ATanggal%20%3A%20xxx%0APengemudi%20%3A%20xxx%0ALokasi%20Penjemputan%20%3A%20xxx%0ALokasi%20Tujuan%20%3A%20xxx%0A

function kirimPesan() {
  var nama = document.getElementById("nama");
  var wa = document.getElementById("wa");
  var email = document.getElementById("email");
  var mobil = document.getElementById("mobil");
  var tanggal = document.getElementById("tanggal");
  var sopir = document.getElementById("sopir");
  var lokasi_penjemputan = document.getElementById("lokasi_penjemputan");
  var lokasi_tujuan = document.getElementById("lokasi_tujuan");

  var gabungan =
    "Ada%20pesanan%20masuk%20!%0ASegera%20konfirmasi%20!%0A%0A" +
    "Nama%20%3A%20" +
    nama.value +
    "%0ANomor%20WhatsApps%20%3A%20" +
    wa.value +
    "%0AEmail%20%3A%20" +
    email.value +
    "%0AMobil%20%3A%20" +
    mobil.value +
    "%0ATanggal%20%3A%20" +
    tanggal.value +
    "%0APengemudi%20%3A%20" +
    sopir.value +
    "%0ALokasi%20Penjemputan%20%3A%20" +
    lokasi_penjemputan.value +
    "%0ALokasi%20Tujuan%20%3A%20" +
    lokasi_tujuan.value;

  var token = "5638633198:AAHhjPxdjq6_XgaoKAqMUcxY9oMFf05SPxU";
  var grub = "-862216614";
  var kontak = "";

  $.ajax({
    url: `https://api.telegram.org/bot${token}/sendMessage?chat_id=${grub}&text=${gabungan}&parse_mode=html`,
    method: `POST`,
  });
}

// awal nama
function validateForm() {
  var awal = document.getElementById("form3Examplev2").value;
  var akhir = document.getElementById("form3Examplev3").value;
  var errorNama = document.getElementById("error-nama");
  var errorNamaku = document.getElementById("error-namaku");
  var regexNama = /^[A-Za-z\s]+$/;
  var regexNamaku = /^[A-Za-z\s]+$/;

  if (!regexNama.test(awal)) {
    errorNama.innerHTML = "Nama awal tidak boleh mengandung angka atau simbol.";
    return false;
  } else {
    errorNama.innerHTML = "";
  }

  if (!regexNamaku.test(akhir)) {
    errorNamaku.innerHTML = "Nama akhir tidak boleh mengandung angka atau simbol.";
    return false;
  } else {
    errorNama.innerHTML = "";
  }

  return true;
}
// akhir nama

// awal hidden

function change() {
  var x = document.getElementById("password").type;
  if (x == "password") {
    document.getElementById("password").type = "text";
    document.getElementById("mybutton").innerHTML = `<svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-eye-slash-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                                                <path d="M10.79 12.912l-1.614-1.615a3.5 3.5 0 0 1-4.474-4.474l-2.06-2.06C.938 6.278 0 8 0 8s3 5.5 8 5.5a7.029 7.029 0 0 0 2.79-.588zM5.21 3.088A7.028 7.028 0 0 1 8 2.5c5 0 8 5.5 8 5.5s-.939 1.721-2.641 3.238l-2.062-2.062a3.5 3.5 0 0 0-4.474-4.474L5.21 3.089z"/>
                                                                <path d="M5.525 7.646a2.5 2.5 0 0 0 2.829 2.829l-2.83-2.829zm4.95.708l-2.829-2.83a2.5 2.5 0 0 1 2.829 2.829z"/>
                                                                <path fill-rule="evenodd" d="M13.646 14.354l-12-12 .708-.708 12 12-.708.708z"/>
                                                                </svg>`;
  } else {
    document.getElementById("password").type = "password";
    document.getElementById("mybutton").innerHTML = `<svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-eye-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                                                <path d="M10.5 8a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0z"/>
                                                                <path fill-rule="evenodd" d="M0 8s3-5.5 8-5.5S16 8 16 8s-3 5.5-8 5.5S0 8 0 8zm8 3.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7z"/>
                                                                </svg>`;
  }
}
// akhir hidden
