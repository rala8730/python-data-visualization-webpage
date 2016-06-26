#!/usr/bin/env python
import MySQLdb

# open databases connection
#here, please enter the the username, passwaord, and mysql database you created
#you will have to do this for all four webpages
db = MySQLdb.connect("localhost","root","password","pollutiondata")

##beginning of the HTML header/webpage
print "content-type: text/html"
print
 
con = '''
<html>

<head>
   <title> Carbon Emissions (2013) </title>
   <link rel="stylesheet" type="text/css" href="MyStyle.css">
</head>
<body style="margin-left: 200px; margin-right: 200px; margin-top: 50px; margin-bottom: 50px;">

  <h2>Carbon Emissions In Each State</h2>
  <p>The map below visualizes data taken from the U.S. Energy Information Administration (EIA) Website for
  annual carbon emissions per State in Million Metric tons of CO<sub>2</sub>, and includes a breakdown of the
  individual contributions in each state due to Petroleum, Gas, and Coal.</p></br>
   <!--These three link to the source code for the map visualization --> 
  <script src="http://d3js.org/d3.v3.min.js"></script>
  <script src="http://d3js.org/topojson.v1.min.js"></script>
  <script src="http://datamaps.github.io/scripts/0.5.4/datamaps.all.min.js"></script>
  
  <!--Allows user to switch between years.  We had to link to multiple webpages -->
  <form> <span class="Button_explanation">Choose year to visualise: </span>
  <button formaction="/cgi-bin/main.py">1990</button>
  <button formaction="/cgi-bin/main2.py"> 2000</button>
  <button formaction="/cgi-bin/main3.py">2010</button>
  <button formaction="/cgi-bin/main4.py">2013</button>
  </form>

  <!-- creates a 'container' to hold the map visualization -->
  <div id="container" style="position: relative; width: 900px; height: 600px; margin: auto;"></div>

 
     
     <script>
	//Creates an instance of the map
	var map  = new Datamap({
 	 scope: 'usa',
 	 element: document.getElementById('container'),
  	 //this fetches the map JSON
	 geographyConfig: {
    	  highlightBorderColor: '#bada55',
  	  //creates the information displayed in the Popup hover
 	  popupTemplate: function(geography, data) {
	   return '<div class="hoverinfo" style="background-color:rgba(38, 82, 91, 0.9); color:white;">' + '<b>'+ geography.properties.name +'</b> </br>' +
	   'Total:' +  data.Total + '</br>' +  'Coal:' + data.Coal + '</br>' +  'Petroleum:' + data.Pet + '</br>' +  'Gas:' + data.Gas +' '
   	   },
   	 highlightBorderWidth: 3
 	 },
	 //map chloropeth fills
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

#in each .py file a different table in the database in accessed
cursor.execute("SELECT * FROM `2013`")

#defines the colors to be returned by the chloropeth
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

#this loops through the database, and fills in values according to each state. 
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
</br></br></br>

<p>Carbon occurs naturally in the atmosphere, however, human activities alter the carbon cycle by adding more CO<sub>2</sub> to it. The main human activity that emits CO<sub>2</sub> is the combustion of fossil fuels (oil, natural gas, and coal).
</p>

<p>
   Changes in Carbon emissions are influenced by many factors, some being changes in population, seasonal temperatures, and new technologies. Visualizing this data is useful in analyzing trends present in changing CO<sub>2</sub> levels; this data reveal a slight increase in emissions (about 9%)
 since 1990, which reflects increased energy usage due to a growing population and changing economy.
</p>



</body>

'''
print footer

# disconnect from server
db.close()   
