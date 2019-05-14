CREATE TABLE `seo_redirect_location` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Org_Location` varchar(45) DEFAULT NULL,
  `Redirect_Location` varchar(45) DEFAULT NULL,
  `Redirect_Code` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ;

INSERT INTO `seo_redirect_location` (`Org_Location`,`Redirect_Location`,`Redirect_Code`)
VALUES ('/previous-feature/1','/new-feature-1',301);

INSERT INTO `seo_redirect_location` (`Org_Location`,`Redirect_Location`,`Redirect_Code`)
VALUES ('/previous-feature/2','/new-feature-2',302);
