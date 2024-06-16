const selectProvinsi = document.getElementById("provinsi");
const selectKota = document.getElementById("kota");
const selectKecamatan = document.getElementById("kecamatan");
const selectKelurahan = document.getElementById("kelurahan");

selectProvinsi.addEventListener("change", (e) => {
  var provinsi = e.target.options[e.target.selectedIndex].dataset.prov;
  fetch(`https://kanglerian.github.io/api-wilayah-indonesia/api/regencies/${provinsi}.json`)
    .then((response) => response.json())
    .then((regencies) => {
      var data = regencies;
      var tampung = `<option>Pilih</option>`;
      document.getElementById("kota").innerHTML = "<option>Pilih</option>";
      document.getElementById("kecamatan").innerHTML = "<option>Pilih</option>";
      document.getElementById("kelurahan").innerHTML = "<option>Pilih</option>";
      data.forEach((element) => {
        tampung += `<option data-prov="${element.id}" value="${element.name}">${element.name}</option>`;
      });
      document.getElementById("kota").innerHTML = tampung;
    });
});

selectKota.addEventListener("change", (e) => {
  var kota = e.target.options[e.target.selectedIndex].dataset.prov;
  fetch(`https://kanglerian.github.io/api-wilayah-indonesia/api/districts/${kota}.json`)
    .then((response) => response.json())
    .then((districts) => {
      var data = districts;
      var tampung = `<option>Pilih</option>`;
      document.getElementById("kecamatan").innerHTML = "<option>Pilih</option>";
      document.getElementById("kelurahan").innerHTML = "<option>Pilih</option>";
      data.forEach((element) => {
        tampung += `<option data-prov="${element.id}" value="${element.name}">${element.name}</option>`;
      });
      document.getElementById("kecamatan").innerHTML = tampung;
    });
});
selectKecamatan.addEventListener("change", (e) => {
  var kecamatan = e.target.options[e.target.selectedIndex].dataset.prov;
  fetch(`https://kanglerian.github.io/api-wilayah-indonesia/api/villages/${kecamatan}.json`)
    .then((response) => response.json())
    .then((villages) => {
      var data = villages;
      var tampung = `<option>Pilih</option>`;
      document.getElementById("kelurahan").innerHTML = "<option>Pilih</option>";
      data.forEach((element) => {
        tampung += `<option data-prov="${element.id}" value="${element.name}">${element.name}</option>`;
      });
      document.getElementById("kelurahan").innerHTML = tampung;
    });
});
