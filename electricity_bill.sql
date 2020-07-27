-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 27, 2020 at 02:28 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `electricity_bill`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `id` int(11) NOT NULL,
  `meterno` int(250) NOT NULL,
  `consumerno` bigint(250) NOT NULL,
  `consumername` varchar(250) NOT NULL,
  `load_con` varchar(5) NOT NULL DEFAULT '5',
  `unit_consumed` int(250) NOT NULL,
  `month` varchar(20) NOT NULL,
  `year` int(4) NOT NULL DEFAULT current_timestamp(),
  `email` varchar(250) NOT NULL,
  `address` text NOT NULL,
  `amountgen` decimal(11,5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `dept`
--

CREATE TABLE `dept` (
  `id` int(11) NOT NULL,
  `dept_no` int(20) NOT NULL,
  `deptname` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dept`
--

INSERT INTO `dept` (`id`, `dept_no`, `deptname`) VALUES
(1, 156758, 'ADMIN'),
(2, 145759, 'BILL GENERATION'),
(3, 145761, 'BILL DELIVERY'),
(4, 15675812, 'CUSTOMER');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `id` int(11) NOT NULL,
  `userid` varchar(250) NOT NULL,
  `branch` varchar(500) NOT NULL,
  `session_in` datetime NOT NULL DEFAULT current_timestamp(),
  `session_out` datetime NOT NULL,
  `dept_no` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(250) NOT NULL,
  `password` varchar(100) NOT NULL,
  `branch` varchar(500) NOT NULL,
  `dept_no` int(20) NOT NULL,
  `useradmin_id` varchar(250) NOT NULL COMMENT 'This the user id'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `branch`, `dept_no`, `useradmin_id`) VALUES
(1, 'dhruva', '60640c8984605878ac9854540a2ed071', 'ADMIN', 156758, '15675801#ADMIN'),
(2, 'test', '098f6bcd4621d373cade4e832627b4f6', 'ADMIN', 156758, '1567581te#ADMIN');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dept`
--
ALTER TABLE `dept`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `deptname` (`deptname`),
  ADD UNIQUE KEY `dept_no` (`dept_no`),
  ADD UNIQUE KEY `dept_unique` (`deptname`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id`),
  ADD KEY `branch` (`branch`),
  ADD KEY `userid` (`userid`),
  ADD KEY `login_ibfk_3` (`dept_no`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `useradmin_id` (`useradmin_id`),
  ADD KEY `branch` (`branch`),
  ADD KEY `dept_no` (`dept_no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `dept`
--
ALTER TABLE `dept`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `login`
--
ALTER TABLE `login`
  ADD CONSTRAINT `login_ibfk_1` FOREIGN KEY (`branch`) REFERENCES `user` (`useradmin_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `login_ibfk_2` FOREIGN KEY (`userid`) REFERENCES `user` (`useradmin_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `login_ibfk_3` FOREIGN KEY (`dept_no`) REFERENCES `user` (`dept_no`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`branch`) REFERENCES `dept` (`deptname`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `user_ibfk_2` FOREIGN KEY (`dept_no`) REFERENCES `dept` (`dept_no`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
