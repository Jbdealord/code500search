#!/usr/bin/python

import re
import sqlite3

keyword = 'in'
# connect to blog database, retrieve all posts
conn = sqlite3.connect('indexing.sqlite3')

print "Opened database successfully";

cursor = conn.execute("SELECT id, title, slug, publish from search_post")
for row in cursor:
   print "ID = ", row[0]
   print "title = ", row[1]
   arr = [m.start() for m in re.finditer(keyword, row[1])]

   # check in dictionary, if not exists then insert
   cursor = conn.execute("SELECT hash from dictionary where word = ?",(keyword,))
   rowcount = len(cursor.fetchall())
   print "count = ", rowcount
   if rowcount == 0:
   		conn.execute("INSERT INTO dictionary (hash,word) \
      	VALUES (?, ?)",(keyword,keyword,));
		conn.commit()

   for idx, val in enumerate(arr):
	   # check in reverse_index, if not exists then insert
	   cursor = conn.execute("SELECT hash from reverse_index where hash = ? and post = ? and field = ? and start = ?",(keyword,row[0], 'title',val))
	   rowcount = len(cursor.fetchall())
	   if rowcount == 0:
		   print "arr = ", idx
		   conn.execute("INSERT INTO reverse_index (post,hash, field, start) \
		      	VALUES (?,?,?,?)",(row[0],keyword,'title', val));
		   conn.commit()

   print "appear: ", arr

# recount and update to index_count
print "Operation done successfully";
conn.close()	