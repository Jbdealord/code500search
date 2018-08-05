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
   # check in reverse_index, if not exists then insert
   print "appear: ", arr

# recount and update to index_count
print "Operation done successfully";
conn.close()	