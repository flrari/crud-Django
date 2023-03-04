CREATE TABLE IF NOT EXIST `dipendenti` (
    `id` integer not null auto_increment unique primary key,
    `name` varchar(100),
    `email` varchar(100),
    `job_title` varchar(100),
    `phone` varchar(100),
    `employee_code` varchar(100) unique not null
)  ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;