-- ----------------------------------------------------------------------------------
-- Notes:  * Script to create BOOKS Database, Tables DDL 
--         * Inserts for Initial Data load for all tables
--
-- ----------------------------------------------------------------------------------

-- ----------------------------------------------------------------------------------
-- 1. Create Schema and assign  user to that schema 
-- ----------------------------------------------------------------------------------
CREATE SCHEMA books;
ALTER SCHEMA books OWNER TO arti;

set search_path=books;

-- ----------------------------------------------------------------------------------
-- 2. Create tables book 
-- ----------------------------------------------------------------------------------
-- table books.book
--
create table book(
id int primary key generated always as identity,
title varchar(100),
number_of_pages int,
publish_date date,
quantity int)

-- ----------------------------------------------------------------------------------
-- 3. Load Data for book
-- ----------------------------------------------------------------------------------

-- 
-- books.book
INSERT INTO books.book
(title, number_of_pages, publish_date, quantity)
VALUES('Harry Potter',300, '2011-2-2', 30);







