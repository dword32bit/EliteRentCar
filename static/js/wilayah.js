fetch(`https://kanglerian.github.io/api-wilayah-indonesia/api/provinces.json`)
  .then((response) => response.json())
  .then((provinces) => {
    var data = provinces;
    var tampung = `<option>Pilih</option>`;
    data.forEach((element) => {
      tampung += `<option data-prov="${element.id}" value="${element.name}">${element.name}</option>`;
    });
    document.getElementById("provinsi").innerHTML = tampung;
  });

fetch(`https://kanglerian.github.io/api-wilayah-indonesia/api/regencies/11.json`)
  .then((response) => response.json())
  .then((regencies) => console.log(regencies));
