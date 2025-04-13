-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 12, 2025 at 10:44 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `quanly_banthietbi`
--

-- --------------------------------------------------------

--
-- Table structure for table `chitiethoadon`
--

CREATE TABLE `chitiethoadon` (
  `id` int(11) NOT NULL,
  `id_hoadon` int(11) DEFAULT NULL,
  `id_thietbi` int(11) DEFAULT NULL,
  `soluong` int(11) NOT NULL,
  `dongia` decimal(15,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `chitiethoadon`
--

INSERT INTO `chitiethoadon` (`id`, `id_hoadon`, `id_thietbi`, `soluong`, `dongia`) VALUES
(7, 4, 6, 1, 30000000.00),
(8, 5, 6, 1, 30000000.00),
(9, 6, 7, 1, 1.00),
(10, 6, 8, 1, 1.00),
(11, 7, 6, 4, 30000000.00),
(12, 7, 8, 4, 1.00),
(13, 8, 10, 5, 2000000.00),
(14, 8, 6, 4, 30000000.00),
(15, 9, 6, 2, 30000000.00),
(16, 9, 10, 2, 2000000.00);

-- --------------------------------------------------------

--
-- Table structure for table `hoadon`
--

CREATE TABLE `hoadon` (
  `id` int(11) NOT NULL,
  `id_khachhang` int(11) DEFAULT NULL,
  `ngaylap` datetime DEFAULT current_timestamp(),
  `tongtien` decimal(15,2) DEFAULT 0.00
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `hoadon`
--

INSERT INTO `hoadon` (`id`, `id_khachhang`, `ngaylap`, `tongtien`) VALUES
(1, 1, '2025-04-12 00:00:00', 30990000.00),
(4, 1, '2025-04-12 00:00:00', 30000000.00),
(5, 2, '2025-04-12 00:00:00', 30000000.00),
(6, 1, '2025-04-12 00:00:00', 2.00),
(7, 2, '2025-04-12 00:00:00', 120000004.00),
(8, 2, '2025-04-12 00:00:00', 130000000.00),
(9, 1, '2025-04-12 00:00:00', 64000000.00);

-- --------------------------------------------------------

--
-- Table structure for table `khachhang`
--

CREATE TABLE `khachhang` (
  `id` int(11) NOT NULL,
  `ten` varchar(255) NOT NULL,
  `sdt` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `diachi` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `khachhang`
--

INSERT INTO `khachhang` (`id`, `ten`, `sdt`, `email`, `diachi`) VALUES
(1, 'Nguyễn Văn C', '0987654321', 'c.nguyen@example.com', 'Hà Nội'),
(2, 'Lê Thị D', '0912345678', 'd.le@example.com', 'TP. HCM'),
(3, 'Trần Văn E', '0909090909', 'e.tran@example.com', 'Đà Nẵng2');

-- --------------------------------------------------------

--
-- Table structure for table `nhanvien`
--

CREATE TABLE `nhanvien` (
  `id` int(11) NOT NULL,
  `HoTen` varchar(100) DEFAULT NULL,
  `VaiTro` varchar(20) DEFAULT NULL,
  `TenDangNhap` varchar(50) DEFAULT NULL,
  `MatKhau` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `nhanvien`
--

INSERT INTO `nhanvien` (`id`, `HoTen`, `VaiTro`, `TenDangNhap`, `MatKhau`) VALUES
(1, 'Nguyen Van A', 'Admin', '1', '1'),
(2, 'Tran Thi B', 'NhanVien', '2', '2');

-- --------------------------------------------------------

--
-- Table structure for table `thietbi`
--

CREATE TABLE `thietbi` (
  `id` int(11) NOT NULL,
  `ten` varchar(255) NOT NULL,
  `hang` varchar(100) DEFAULT NULL,
  `gia` decimal(15,2) NOT NULL,
  `soluong` int(11) DEFAULT 0,
  `mota` text DEFAULT NULL,
  `hinhanh` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `thietbi`
--

INSERT INTO `thietbi` (`id`, `ten`, `hang`, `gia`, `soluong`, `mota`, `hinhanh`) VALUES
(6, 'Iphone 14 promax', 'iphone', 30000000.00, 88, 'đẹp', 'C:/Users/duong/PycharmProjects/TASK2/assets/images/iphone.jpg'),
(7, '1', '1', 1.00, 10, '1', ''),
(8, '12', '122', 1.00, 117, '12', 'C:/Users/duong/PycharmProjects/TASK2/assets/images/iphone.jpg'),
(10, 'iphone 19', 'iphone', 2000000.00, 3, 'đẹp', 'C:/Users/duong/PycharmProjects/TASK2/assets/images/Iphone19prm.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `chitiethoadon`
--
ALTER TABLE `chitiethoadon`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_hoadon` (`id_hoadon`),
  ADD KEY `id_thietbi` (`id_thietbi`);

--
-- Indexes for table `hoadon`
--
ALTER TABLE `hoadon`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_khachhang` (`id_khachhang`);

--
-- Indexes for table `khachhang`
--
ALTER TABLE `khachhang`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `nhanvien`
--
ALTER TABLE `nhanvien`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `thietbi`
--
ALTER TABLE `thietbi`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `chitiethoadon`
--
ALTER TABLE `chitiethoadon`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `hoadon`
--
ALTER TABLE `hoadon`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `khachhang`
--
ALTER TABLE `khachhang`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `nhanvien`
--
ALTER TABLE `nhanvien`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `thietbi`
--
ALTER TABLE `thietbi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `chitiethoadon`
--
ALTER TABLE `chitiethoadon`
  ADD CONSTRAINT `chitiethoadon_ibfk_1` FOREIGN KEY (`id_hoadon`) REFERENCES `hoadon` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `chitiethoadon_ibfk_2` FOREIGN KEY (`id_thietbi`) REFERENCES `thietbi` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `hoadon`
--
ALTER TABLE `hoadon`
  ADD CONSTRAINT `hoadon_ibfk_1` FOREIGN KEY (`id_khachhang`) REFERENCES `khachhang` (`id`) ON DELETE SET NULL ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
