#!/bin/bash
#
# build_database.sh - create empty temperature database schema for to log temperature in.
#
# Tom Holderness 22/01/2012
sqlite3 piTemps.db 'DROP TABLE temperature_records;'
sqlite3 piTemps.db 'CREATE TABLE temperature_records(
                        sensno int,
                        unix_time bigint,
                        celsius real,
                        PRIMARY KEY(sensno, unix_time)
                        );' 
sqlite3 piTemps.db 'DROP TABLE sensors;'

sqlite3 piTemps.db 'CREATE TABLE sensors(
                        sensno int,
                        sens_description TEXT,
                        sensid TEXT,
                        PRIMARY KEY(sensno)
                        );' 

