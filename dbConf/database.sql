CREATE DATABASE sdchat;

USE sdchat;

CREATE TABLE messages (
    user VARCHAR(30),
    content TEXT,
    msgDate DATETIME,
    KEY(user, msgDate)
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;