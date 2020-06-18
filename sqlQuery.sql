

CREATE TABLE `customer` (
  `id` int(11) NOT NULL,
  `meterno` int(11) NOT NULL,
  `consumerno` int(11) NOT NULL,
  `load_con` varchar(5) NOT NULL DEFAULT '5',
  `reading` int(11) NOT NULL,
  `month` datetime NOT NULL DEFAULT current_timestamp(),
  `email` varchar(250) NOT NULL,
  `address` text NOT NULL
);



CREATE TABLE `dept` (
  `id` int(11) NOT NULL,
  `dept_no` int(20) NOT NULL,
  `deptname` text NOT NULL
);



INSERT INTO `dept` (`id`, `dept_no`, `deptname`) VALUES
(1, 156758, 'ADMIN'),
(2, 145759, 'BILL GENERATION'),
(3, 145760, 'METER READING'),
(4, 145761, 'BILL DELIVERY');




CREATE TABLE `login` (
  `id` int(11) NOT NULL,
  `userid` varchar(250) NOT NULL,
  `branch` text NOT NULL,
  `session_in` datetime NOT NULL DEFAULT current_timestamp(),
  `session_out` datetime NOT NULL,
  `dept_no` int(20) NOT NULL
);



CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(250) NOT NULL,
  `password` varchar(100) NOT NULL,
  `branch` varchar(250) NOT NULL,
  `dept_no` int(20) NOT NULL,
  `useradmin_id` varchar(250) NOT NULL COMMENT 'This the user id'
);


INSERT INTO `user` (`id`, `username`, `password`, `branch`, `dept_no`, `useradmin_id`) VALUES
(1, 'dhruva', '60640c8984605878ac9854540a2ed071', 'ADMIN', 156758, '15675801#ADMIN'),
(2, 'smyan', 'cb3566691eeae07640e854f76bf355ff', 'ADMIN', 156758, '1567581#ADMIN'),
(3, 'test', '098f6bcd4621d373cade4e832627b4f6', 'ADMIN', 156758, '1567581te#ADMIN');


ALTER TABLE `customer`
  ADD PRIMARY KEY (`id`);


ALTER TABLE `dept`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `dept_no` (`dept_no`);


ALTER TABLE `login`
  ADD PRIMARY KEY (`id`);


ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `useradmin_id` (`useradmin_id`);


ALTER TABLE `customer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;


ALTER TABLE `dept`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;


ALTER TABLE `login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60;


ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;


