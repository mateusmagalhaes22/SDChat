CREATE DATABASE sdchat;

USE sdchat;

CREATE TABLE messages (
    usuario VARCHAR(30),
    conteudo VARCHAR(200),
    msgDate DATETIME
)

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;