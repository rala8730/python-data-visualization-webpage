#!/usr/bin/env python
import MySQLdb

################please enter your password in the place of password#######
# open databases connection
db = MySQLdb.connect("localhost","sarah","test","pollution2")
print "content-type: text/html"
print
 
con = '''
<html>
<head>
   <title> Pollution in the U.S. </title>
</head>
<body>


  <script src="http://d3js.org/d3.v3.min.js"></script>
  <script src="http://d3js.org/topojson.v1.min.js"></script>
  <script src="http://datamaps.github.io/scripts/0.5.4/datamaps.all.min.js"></script>
  <!-- this link to the source code -->
  <!--<p><a href="http://datamaps.github.io/">DataMaps Project Homepage</a></p> -->
  <!-- changing the width in the div below will change the size of the map -->
<form><span class="Button_explanation">Choose year to visualise: </span>
<button formaction="/cgi-bin/main.py">1990</button>
 <button formaction="/cgi-bin/main2.py"> 2000</button>
 <button formaction="/cgi-bin/main3.py"> 2010</button>
 <button formaction="/cgi-bin/main4.py">2013</button>
</form>
  <div id="container" style="position: relative; width: 500px; height: 300px;"></div>

 
     
     <script>
	/*
       //basic map config with custom fills, mercator projection
      var map = new Datamap({
        element: document.getElementById('container'),
	scope:'usa'
	});
	*/

	var map  = new Datamap({
  scope: 'usa',
  element: document.getElementById('container'),
  geographyConfig: {
    highlightBorderColor: '#bada55',
  popupTemplate: function(geography, data) {
      return '<div class="hoverinfo">' + 
'Total:' +  data.Total + '</br>' +  'Coal:' + data.Coal + '</br>' +  'Petroleum:' + data.Pet + '</br>' +  'Gas:' + data.Gas +' '
    },
    highlightBorderWidth: 3
  },

  fills: {
  '0-50': '#ccffff',
  '51-100': '#66ccff',
  '101-150': '#3399ff',
  '151-200': '#0066ff',
  '201-300': '#0000ff',
  '301-400': '#0000cc',
  '400+': '#000099',
  defaultFill: '#EDDC4E'
},
data:{
'''
print con
cursor=db.cursor()

cursor.execute("SELECT * FROM `2000`")

def filler(value):
	if value > 400:
		return "400+"
	elif value >300:
		return "301-400"
	elif value > 200:
		return "201-300"
	elif value > 150:
		return "151-200"
	elif value > 100:
		return "101-150"
	elif value > 50:
		return "51-100"
	else:
		return "0-50"

for row in cursor.fetchall():
	#print(row[0])
	state = row[0]
	coal = row[1]
	pet = row[2]
	gas = row[3]
	total = row[4]
	color = filler(total)  
	print '''
  	"%s": {
      "fillKey": "%s",
	"Coal": %d,
	"Pet": %d,
	"Gas": %d,
      "Total": %d 
  },

	'''%(state, color, coal, pet, gas, total)

footer = '''
}
});
map.legend();
map.labels();
	</script>
<!--<form name="myform" method="GET" action="cgi-bin/access.py">
<input type= "text" id="name" name ="name" >
<input type = "text" id="product"name ="product" >
<input type = "submit"> -->
	
</body>

'''
print footer
#prepare SQl query to UPDATE required records
#cursor=db.cursor()
# execute SQL query using execute() method.
#cursor.execute("SELECT * FROM `1990`,`2000`,`2010`,`2013`")
#cursor.execute("SELECT * FROM `1990`")

# Fetch a single row using fetchone() method.
#data = cursor.fetchall()

#print (data)

# disconnect from server
db.close()   
#steps 
# read the databases and color the map based on the dense population
