create database
mariadb -u root -e "CREATE DATABASE compose;"

create table
mariadb -u root compose < create_users_table.sql

