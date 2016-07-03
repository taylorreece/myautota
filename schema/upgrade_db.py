#!../venv/bin/python3
import glob
import os
import sys
sys.path.append('.')
sys.path.append('..')
import psycopg2
from bck import database

db = database.BckDB()

try:
	schemaVersion = db.getSchemaVersion()
except psycopg2.ProgrammingError:
	schemaVersion = -1

def applySchema():
	try:
		schemaVersion = db.getSchemaVersion()
	except psycopg2.ProgrammingError:
		schemaVersion = -1
	nextFile = 's%s.sql' % str(int(schemaVersion) + 1)
	if os.path.isfile(nextFile):
		print("Applying %s..." % nextFile)
		f = open(nextFile, 'r')
		db.runFile(f)
		applySchema()

applySchema()
