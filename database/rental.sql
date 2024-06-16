-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 13 Jul 2023 pada 04.09
-- Versi server: 10.4.28-MariaDB
-- Versi PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rental`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `accounts`
--

CREATE TABLE `accounts` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(50) NOT NULL,
  `NIK` int(18) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `accounts`
--

INSERT INTO `accounts` (`id`, `username`, `email`, `password`, `NIK`) VALUES
(1, 'banu', 'banu@gmail.com', '1234', 123123),
(5, 'bnm', 'bnm@gmail.com', '123', 7777),
(10, 'bolo', 'bolo@gmail.com', 'pbkdf2:sha256:600000$2rl6Gc8cV92bSfjN$5e43f385b2a6', 12345609),
(15, 'budi123', 'budi@gmail.com', '123', 789789789),
(9, 'bvn', 'bvn@gmail.com', '111', 777),
(12, 'dot', 'dotcom@gmail.com', '1234123', 2147483647),
(8, 'fera', 'fera@gmail.com', 'pbkdf2:sha256:600000$77d5nIPwITS7RfmP$0f6dcd90c8a8', 812345),
(11, 'fff', 'fff@gmail.com', '111', 89898),
(4, 'iku', 'iki@gmail.com', 'pbkdf2:sha256:600000$Yr1MjIfmX6QDTVuA$e8e14271b8f3', 9999),
(2, 'jokoo', 'joko@gmail.com', 'pbkdf2:sha256:600000$AEvPwKxjQ1UFPvGp$7ce716ecd853', 1234567),
(16, 'karen123', 'karen@gmail.com', '123', 666666),
(14, 'kelaz', 'kelaz@gmail.com', '123', 45454),
(6, 'nyeni', 'nyeni@gmail.com', 'pbkdf2:sha256:600000$M8VnxyAzOW1psH0B$565709a9651e', 12312312),
(7, 'suku', 'suku@gmail.com', '123', 43433),
(13, 'udin', 'udin@pm.me', '123', 121212),
(3, 'wangun', 'cinta@gmail.com', 'pbkdf2:sha256:600000$JxFSPrvtbeiPtwJO$fc579af71cc3', 123123412);

-- --------------------------------------------------------

--
-- Struktur dari tabel `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`) VALUES
(1, 'admin', 'admin');

-- --------------------------------------------------------

--
-- Struktur dari tabel `biodata`
--

CREATE TABLE `biodata` (
  `nik` int(18) NOT NULL,
  `nama_awal` varchar(50) NOT NULL,
  `nama_akhir` varchar(50) NOT NULL,
  `tempat_lahir` varchar(255) NOT NULL,
  `tanggal_lahir` date NOT NULL,
  `dusun` varchar(25) NOT NULL,
  `provinsi` varchar(255) NOT NULL,
  `kabupaten` varchar(255) NOT NULL,
  `kecamatan` varchar(255) NOT NULL,
  `kelurahan` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `biodata`
--

INSERT INTO `biodata` (`nik`, `nama_awal`, `nama_akhir`, `tempat_lahir`, `tanggal_lahir`, `dusun`, `provinsi`, `kabupaten`, `kecamatan`, `kelurahan`) VALUES
(777, 'faf', 'fsdfds', 'suko', '2023-07-18', 'jbhh', 'NUSA TENGGARA TIMUR', 'KABUPATEN SABU RAIJUA', 'SABU BARAT', 'JADU'),
(7777, 'adadsa', 'fafaf', 'joko', '2023-07-26', 'qrwr', 'JAWA TIMUR', 'KABUPATEN PASURUAN', 'REMBANG', 'PEKOREN'),
(9999, 'hai', 'hui', 'fafa', '2023-07-25', 'wono', 'DI YOGYAKARTA', 'KABUPATEN KULON PROGO', 'NANGGULAN', 'DONOMULYO'),
(43433, 'suku', 'jh', 'suko', '2023-07-25', 'jhabhjahfah', 'NUSA TENGGARA TIMUR', 'KABUPATEN NAGEKEO', 'BOAWAE', 'GERODHERE'),
(45454, 'banu', 'wq', 'joko', '2023-07-12', 'gdfg', 'DI YOGYAKARTA', 'KABUPATEN KULON PROGO', 'NANGGULAN', 'BANYUROTO'),
(66666, 'joko', 'budi', 'Klaten', '2023-07-26', 'krangen', 'DI YOGYAKARTA', 'KABUPATEN SLEMAN', 'TEMPEL', 'SUMBER REJO'),
(89898, 'fff', 'fff', 'fff', '2023-07-21', 'fff', 'BALI', 'KOTA DENPASAR', 'DENPASAR TIMUR', 'PENATIH'),
(121212, 'Udin', 'Petot', 'Klaten', '2023-07-11', 'tgk', 'JAWA TENGAH', 'KABUPATEN KLATEN', 'PRAMBANAN', 'KEBON DALEM LOR'),
(123123, 'kijang', 'dasads', 'joko', '2023-07-10', 'wono', 'JAWA TENGAH', 'KABUPATEN GROBOGAN', 'GODONG', 'KOPEK'),
(666666, 'joko', 'budi', 'Klaten', '2023-07-26', 'krangen', 'DI YOGYAKARTA', 'KABUPATEN SLEMAN', 'TEMPEL', 'SUMBER REJO'),
(812345, 'Fera', 'Ka', 'klaten', '2023-07-11', 'tgk', 'JAWA TENGAH', 'KABUPATEN KLATEN', 'PRAMBANAN', 'KEBON DALEM LOR'),
(1234567, 'joko', 'damai', 'klaten', '2000-05-12', 'Prambanan', 'JAWA TENGAH', 'KABUPATEN KLATEN', 'PRAMBANAN', 'BRAJAN'),
(12312312, 'nyeni', 'dek', 'klaten', '1999-03-12', 'Prambanan', 'JAWA TENGAH', 'KABUPATEN KLATEN', 'PRAMBANAN', 'BRAJAN'),
(12345609, 'bolo', 'kurowo', 'klaten', '1999-07-14', 'Prambanan', 'JAWA TENGAH', 'KABUPATEN KLATEN', 'PRAMBANAN', 'BRAJAN'),
(123123123, 'joko', 'damai', 'klaten', '2000-03-12', 'Prambanan', 'JAWA TENGAH', 'KABUPATEN KLATEN', 'PRAMBANAN', 'BRAJAN'),
(123123412, 'cinta', 'damai', 'klaten', '1999-12-12', 'Prambanan', 'JAWA TENGAH', 'KABUPATEN KLATEN', 'PRAMBANAN', 'BRAJAN'),
(789789789, 'budi', 'Waluyo', 'Klaten', '2023-07-24', 'krangen', 'DKI JAKARTA', 'KOTA JAKARTA TIMUR', 'JATINEGARA', 'CIPINANG BESAR SELATAN'),
(1234512345, 'Udin', 'Waluyo', 'Klaten', '2023-07-12', 'tr', 'ACEH', 'KABUPATEN ACEH TENGGARA', 'DARUL HASANAH', 'MAKMUR JAYA'),
(2147483647, 'dot', 'com', 'klaten', '2000-05-14', 'Prambanan', 'JAWA TENGAH', 'KABUPATEN KLATEN', 'PRAMBANAN', 'BRAJAN');

-- --------------------------------------------------------

--
-- Struktur dari tabel `car`
--

CREATE TABLE `car` (
  `id_mobil` int(11) NOT NULL,
  `plat_mobil` varchar(255) NOT NULL,
  `nama_mobil` varchar(255) DEFAULT NULL,
  `tipe_mobil` varchar(255) DEFAULT NULL,
  `tahun_pembuatan` varchar(4) DEFAULT NULL,
  `harga_sewa_per_jam` int(15) DEFAULT NULL,
  `status_ketersediaan` tinyint(1) DEFAULT NULL,
  `gambar` varchar(255) DEFAULT NULL,
  `Warna` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `car`
--

INSERT INTO `car` (`id_mobil`, `plat_mobil`, `nama_mobil`, `tipe_mobil`, `tahun_pembuatan`, `harga_sewa_per_jam`, `status_ketersediaan`, `gambar`, `Warna`) VALUES
(23, 'AB 0851 BU', 'Daihatsu Ayla', 'Sedan', '2017', 20000, 0, 'pngwing.com_4.png', 'Kuning'),
(18, 'AB 1234 IH', 'Honda Corolla', 'Sedan', '2024', 100000, 0, 'pngegg_2.png', 'Putih'),
(22, 'AB 9877 CL', 'Honda Civic', 'Sport', '2077', 50000, 1, 'Civic.png', 'Putih'),
(21, 'AB A88B JO', 'Toyota Yaris', 'Sedan', '2018', 20000, 1, 'pngwing.com_3.png', 'Merah'),
(1, 'AD 1234 IH', 'Toyota Supri', 'Sport', '2077', 50000, 0, 'supra.png', 'Pink'),
(16, 'AU 4456 UI', 'Avanza', 'Sedan', '1945', 50000, 1, 'brio.png', 'Hitam'),
(19, 'B 9874 XYZ', 'Hiace', 'Minivan', '2018', 120000, 1, 'pngegg_1.png', 'Putih');

-- --------------------------------------------------------

--
-- Struktur dari tabel `cobapesanan`
--

CREATE TABLE `cobapesanan` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `jenis_mobil` varchar(255) DEFAULT NULL,
  `tanggal_pickup` date DEFAULT NULL,
  `jam_pickup` time DEFAULT NULL,
  `tanggal_dropoff` date DEFAULT NULL,
  `jam_dropoff` time DEFAULT NULL,
  `harga_sewa_per_jam` int(50) DEFAULT NULL,
  `total_biaya` int(50) DEFAULT NULL,
  `nik` int(18) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `cobapesanan`
--

INSERT INTO `cobapesanan` (`id`, `jenis_mobil`, `tanggal_pickup`, `jam_pickup`, `tanggal_dropoff`, `jam_dropoff`, `harga_sewa_per_jam`, `total_biaya`, `nik`) VALUES
(17, 'Daihatsu Ayla', '2023-07-01', '05:12:00', '2023-07-25', '08:12:00', 20000, 11580000, 123123),
(18, 'Hiace', '2023-07-22', '09:42:00', '2023-07-30', '11:43:00', 120000, 23282000, 123123),
(19, 'Daihatsu Ayla', '2023-07-18', '09:47:00', '2023-07-23', '11:47:00', 20000, 2440000, 45454),
(20, 'Honda Corolla', '2023-07-14', '08:21:00', '2023-07-15', '11:21:00', 100000, 2700000, 2147483647),
(21, 'Daihatsu Ayla', '2023-07-07', '08:47:00', '2023-07-23', '13:47:00', 20000, 7780000, 123123),
(22, 'Daihatsu Ayla', '2023-07-07', '10:55:00', '2023-07-20', '13:55:00', 20000, 6300000, 666666);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `accounts`
--
ALTER TABLE `accounts`
  ADD PRIMARY KEY (`username`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `hub_biodata` (`NIK`);

--
-- Indeks untuk tabel `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `biodata`
--
ALTER TABLE `biodata`
  ADD PRIMARY KEY (`nik`);

--
-- Indeks untuk tabel `car`
--
ALTER TABLE `car`
  ADD PRIMARY KEY (`plat_mobil`),
  ADD UNIQUE KEY `id_mobil` (`id_mobil`);

--
-- Indeks untuk tabel `cobapesanan`
--
ALTER TABLE `cobapesanan`
  ADD PRIMARY KEY (`id`),
  ADD KEY `wa` (`nik`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `accounts`
--
ALTER TABLE `accounts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT untuk tabel `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT untuk tabel `car`
--
ALTER TABLE `car`
  MODIFY `id_mobil` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT untuk tabel `cobapesanan`
--
ALTER TABLE `cobapesanan`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `accounts`
--
ALTER TABLE `accounts`
  ADD CONSTRAINT `hub_biodata` FOREIGN KEY (`NIK`) REFERENCES `biodata` (`nik`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `cobapesanan`
--
ALTER TABLE `cobapesanan`
  ADD CONSTRAINT `wa` FOREIGN KEY (`nik`) REFERENCES `biodata` (`nik`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
