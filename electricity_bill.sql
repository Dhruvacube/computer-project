-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 22, 2020 at 03:41 PM
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

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`id`, `meterno`, `consumerno`, `consumername`, `load_con`, `unit_consumed`, `month`, `year`, `email`, `address`, `amountgen`) VALUES
(1, 1567581, 7584956123, 'Dhruva Shaw', '4.5', 363, 'May', 2020, 'dhruvashaw@gmail.com', '75d, Nelson Manickam Road, Aminjikarai,Chennai,?Tamil Nadu, 600029', '925.60000'),
(2, 1567582, 7584956124, 'Ayush Saha', '4.5', 56, 'May', 2020, 'ayushsaha@gmail.com', 'D 74,Delhi, Delhi, 110017', '791.60000'),
(3, 1567583, 7584956125, 'Smyan Kotkar', '4.5', 563, 'May', 2020, 'smyankotkar@gmail.com', '75d, Nelson Manickam Road, Aminjikarai,Chennai,?Tamil Nadu, 600029', '791.60000'),
(4, 1567584, 7584956126, 'Aritra Das', '4.5', 458, 'May', 2020, 'aritradada@gmail.com', 'D 74,Delhi, Delhi, 110017', '791.60000'),
(5, 1567585, 7584956127, 'Chirag Majumdar', '4.5', 156, 'May', 2020, 'chiragbaba@gmail.com', '75d, Nelson Manickam Road, Aminjikarai,Chennai,?Tamil Nadu, 600029', '791.60000'),
(6, 1567586, 7584956128, 'Hritesh Kumar De', '4.5', 100, 'May', 2020, 'hkdmarke@gmail.com', '2nd Flr, No 7, Readymoney Terrace, 167, Dr Annie Besant Road, Opp Canera Bank, Worli,Mumbai, Maharashtra, 400018', '791.60000'),
(7, 1567587, 7584956129, 'Gourab Sen', '4.5', 145, 'May', 2020, 'gourabkaka@gmail.com', '2nd Flr, No 7, Readymoney Terrace, 167, Dr Annie Besant Road, Opp Canera Bank, Worli,Mumbai, Maharashtra, 400018', '925.60000'),
(8, 1567588, 7584956130, 'Aman Singh', '4.5', 144, 'May', 2020, 'amanphelwan@ggmail.com', '75d, Nelson Manickam Road, Aminjikarai,Chennai,?Tamil Nadu, 600029', '1273.50000'),
(9, 1567589, 7584956131, 'Aman Sa', '4.5', 58, 'May', 2020, 'amanvidyamandir@gmail.com', 'D 74,Delhi, Delhi, 110017', '1200.50000'),
(10, 1567590, 7584956132, 'Suvojit Dutta', '4.5', 756, 'May', 2020, 'suvojitkaka@gmail.com', '75d, Nelson Manickam Road, Aminjikarai,Chennai,?Tamil Nadu, 600029', '1081.50000'),
(11, 1567581, 7584956123, 'Dhruva Shaw', '4.5', 456, 'June', 2020, 'dhruvashaw@gmail.com', '75d, Nelson Manickam Road, Aminjikarai,Chennai,?Tamil Nadu, 600029', '0.00000'),
(12, 1567582, 7584956124, 'Ayush Saha', '4.5', 785, 'June', 2020, 'ayushsaha@gmail.com', 'D 74,Delhi, Delhi, 110017', '0.00000'),
(13, 1567583, 7584956125, 'Smyan Kotkar', '4.5', 150, 'June', 2020, 'smyankotkar@gmail.com', '75d, Nelson Manickam Road, Aminjikarai,Chennai,?Tamil Nadu, 600029', '0.00000'),
(14, 1567584, 7584956126, 'Aritra Das', '4.5', 156, 'June', 2020, 'aritradada@gmail.com', 'D 74,Delhi, Delhi, 110017', '0.00000'),
(15, 1567585, 7584956127, 'Chirag Majumdar', '4.5', 256, 'June', 2020, 'chiragbaba@gmail.com', '75d, Nelson Manickam Road, Aminjikarai,Chennai,?Tamil Nadu, 600029', '0.00000'),
(16, 1567586, 7584956128, 'Hritesh Kumar De', '4.5', 588, 'June', 2020, 'hkdmarke@gmail.com', '2nd Flr, No 7, Readymoney Terrace, 167, Dr Annie Besant Road, Opp Canera Bank, Worli,Mumbai, Maharashtra, 400018', '0.00000'),
(17, 1567587, 7584956129, 'Gourab Sen', '4.5', 586, 'June', 2020, 'gourabkaka@gmail.com', '2nd Flr, No 7, Readymoney Terrace, 167, Dr Annie Besant Road, Opp Canera Bank, Worli,Mumbai, Maharashtra, 400018', '0.00000'),
(18, 1567588, 7584956130, 'Aman Singh', '4.5', 36, 'June', 2020, 'amanphelwan@ggmail.com', '75d, Nelson Manickam Road, Aminjikarai,Chennai,?Tamil Nadu, 600029', '0.00000'),
(19, 1567589, 7584956131, 'Aman Sa', '4.5', 366, 'June', 2020, 'amanvidyamandir@gmail.com', 'D 74,Delhi, Delhi, 110017', '0.00000'),
(20, 1567590, 7584956132, 'Suvojit Dutta', '4.5', 366, 'June', 2020, 'suvojitkaka@gmail.com', '75d, Nelson Manickam Road, Aminjikarai,Chennai,?Tamil Nadu, 600029', '0.00000');

-- --------------------------------------------------------

--
-- Table structure for table `dept`
--

CREATE TABLE `dept` (
  `id` int(11) NOT NULL,
  `dept_no` int(20) NOT NULL,
  `deptname` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dept`
--

INSERT INTO `dept` (`id`, `dept_no`, `deptname`) VALUES
(1, 156758, 'ADMIN'),
(2, 145759, 'BILL GENERATION'),
(3, 145761, 'BILL DELIVERY'),
(5, 15675812, 'CUSTOMER');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `id` int(11) NOT NULL,
  `userid` varchar(250) NOT NULL,
  `branch` text NOT NULL,
  `session_in` datetime NOT NULL DEFAULT current_timestamp(),
  `session_out` datetime NOT NULL,
  `dept_no` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`id`, `userid`, `branch`, `session_in`, `session_out`, `dept_no`) VALUES
(80, '15675801#ADMIN', 'ADMIN', '2020-06-22 10:44:55', '2020-06-22 13:07:03', 156758),
(81, '15675801#ADMIN', 'ADMIN', '2020-06-22 13:07:16', '2020-06-22 13:08:53', 156758),
(82, '15675801#ADMIN', 'ADMIN', '2020-06-22 13:09:51', '2020-06-22 13:16:35', 156758),
(83, '15675801#ADMIN', 'ADMIN', '2020-06-22 13:16:49', '2020-06-22 13:21:15', 156758),
(84, '15675801#ADMIN', 'ADMIN', '2020-06-22 13:21:28', '2020-06-22 13:22:35', 156758),
(85, '15675801#ADMIN', 'ADMIN', '2020-06-22 13:26:14', '2020-06-22 13:26:42', 156758),
(86, '15675801#admin', 'ADMIN', '2020-06-22 18:12:05', '2020-06-22 18:12:54', 156758),
(87, '15675801#ADMIN', 'ADMIN', '2020-06-22 18:13:05', '0000-00-00 00:00:00', 156758);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(250) NOT NULL,
  `password` varchar(100) NOT NULL,
  `branch` varchar(250) NOT NULL,
  `dept_no` int(20) NOT NULL,
  `useradmin_id` varchar(250) NOT NULL COMMENT 'This the user id'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `branch`, `dept_no`, `useradmin_id`) VALUES
(1, 'dhruva', '60640c8984605878ac9854540a2ed071', 'ADMIN', 156758, '15675801#ADMIN'),
(3, 'test', '098f6bcd4621d373cade4e832627b4f6', 'ADMIN', 156758, '1567581te#ADMIN');

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
  ADD UNIQUE KEY `dept_no` (`dept_no`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `useradmin_id` (`useradmin_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `dept`
--
ALTER TABLE `dept`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=88;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
