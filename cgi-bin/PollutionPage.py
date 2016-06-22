#!/usr/bin/env python
import cgi, cgitb
import json

print "content-type: text/html"
print

contents= '''
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
  <div id="container" style="position: relative; width:500px;height: 300px;"></div>
 
     
     <script>
      var map = new Datamap({
        scope: 'usa',
        element: document.getElementById('container'),
	  });
	</script>
'''
print contents
print"</body></html>"
