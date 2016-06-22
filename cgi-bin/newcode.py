#!/usr/bin/env python
import MySQLdb

################please enter your password in the place of password#######
# open databases connection
db = MySQLdb.connect("localhost","root","password","pollutiondata" )

print "content-type: text/html"
print 
contents ='''
<html>
<head>
</head>
<body>
<!--getting started-->

<script src="//cdnjs.cloudflare.com/ajax/libs/d3/3.5.3/d3.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/topojson/1.6.9/topojson.min.js"></script>
<script src="/datamaps.usa.min.js"></script>
<div id="container" style="position: relative; width: 500px; height: 300px;"></div>

<!--usmaps only-->
<script>
    var map = new Datamap({
        element: document.getElementById('container'),
        scope: 'usa'
    });
</script>
'''
print contents
print "</body></html>"

#prepare SQl query to UPDATE required records
cursor=db.cursor()
# execute SQL query using execute() method.
#cursor.execute("SELECT * FROM `1990`,`2000`,`2010`,`2013`")
cursor.execute("SELECT * FROM `1990`")

# Fetch a single row using fetchone() method.
data = cursor.fetchall()

print data

# disconnect from server
db.close()   
#steps 
# read the databases and color the map based on the dense population
