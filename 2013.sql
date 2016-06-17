CREATE TABLE IF NOT EXISTS `thirteen` (

`State` varchar(2) NOT NULL,

`Coal` float NOT NULL,

`Petroluim` float NOT NULL,

`Gas` float NOT NULL,

`Total` float NOT NULL,

PRIMARY KEY (`state`)

) ENGINE=MyISAM DEFAULT CHARSET=utf8 ;

INSERT INTO `thirteen` (`State`, `Coal`, `Petroluim`, `Gas`, `Total`) VALUES

('AK', 1.4, 17, 17.7, 36.1),

('AL', 53.3, 33.2, 33.3, 119.8),

('AR', 30.9, 21.6, 15.3, 67.8),

('AZ', 43, 32.8, 18.1, 93.8),

('CA', 3.6, 217.7, 131.8, 353.1),

('CO', 34.3, 30.6, 25.6, 90.5),

('CT', 0.7, 20.8, 12.7, 34.3),

('DE', 1.7, 6.3, 5.3, 13.4),

('DC', 0, 1, 1.8, 2.8),

('FL', 47.7, 103.9, 66.1, 217.6),

('GA', 40.2, 58.6, 33.7, 132.5),

('HI', 1.4, 16.8, 0, 18.2),

('IA', 38, 25.7, 16.3, 79.9),

('ID', 0.7, 10.3, 5.7, 16.7),

('IL', 96.8, 76.9, 56.4, 230.2),

('IN', 112.8, 50.9, 36.1, 199.8),

('KS', 30.9, 26.6, 15.3, 72.8),

('KY', 86.4, 38.1, 12.5, 137),

('LA', 21.5, 95.9, 77, 194.5),

('MA', 4, 37.2, 24.1, 65.3),

('MD', 17.3, 29.6, 11, 57.9),

('ME', 0.2, 12.6, 3.5, 16.2),

('MI', 62.1, 54, 44.1, 160.2),

('MN', 25.3, 38, 25.4, 88.6),

('MO', 76.2, 40.2, 14.9, 131.3),

('MS', 9.2, 28.2, 22.7, 60.1),

('MT', 15.7, 11.7, 4.4, 31.7),

('NC', 46.6, 52.1, 23.6, 122.4),

('ND', 37.1, 15.1, 4.4, 56.6),

('NE', 27.7, 15.8, 9.5, 53),

('NH', 1.6, 9.4, 3, 13.9),

('NJ', 2.4, 64.8, 37.8, 105.1),

('NM', 24.2, 16.2, 13.4, 53.9),

('NV', 6.1, 14.7, 15, 35.8),

('NY', 6.5, 83.7, 70.1, 160.3),

('OH', 104, 74.4, 50.2, 228.7),

('OK', 31.7, 35.1, 36.2, 103.1),

('OR', 3.7, 21.7, 13, 38.4),

('PA', 105.9, 77.1, 60.8, 243.9),

('RI', 0, 5.3, 4.7, 10),

('SC', 24.3, 32.3, 12.6, 69.2),

('SD', 3.2, 7.4, 4.5, 15.2),

('TN', 37.7, 43.8, 15.2, 96.7),

('TX', 150.8, 280.9, 209.2, 641),

('UT', 33.5, 19.1, 13.7, 66.4),

('VA', 27.3, 52.6, 23, 103),

('VT', 0, 5.1, 0.5, 5.6),

('WA', 7.1, 48.7, 17.4, 73.1),

('WI', 42.9, 32.7, 23.9, 99.5),

('WV', 72.8, 12.5, 8, 93.3),

('WY', 49.2, 11, 8.3, 68.4);