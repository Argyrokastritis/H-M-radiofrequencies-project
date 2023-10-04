import folium
import os
import webbrowser
from folium.plugins import FloatImage

class map_creation:
    def __init__(self, location, coordinates_arr, prediction):
        self.location = location
        self.coordinates_arr = coordinates_arr
        self.prediction = prediction

    def create_map(self):
        # Create a map centered on Greece
        m = folium.Map(location=self.location, zoom_start=7.5)

        # Add a title to the map
        title_html = '''
                     <h3 align="center" style="font-size:19px; margin-top: 10px; margin-bottom: 10px"><b>All Cosmote Stores in Greece</b></h3>
                     '''
        m.get_root().html.add_child(folium.Element(title_html))

        # Add a marker that allows the user to select a location on the map
        # marker location in coordination 38.23873568178249, 21.732222880214238

        folium.Marker(location=self.location, icon=folium.Icon(icon="glyphicon-star", color='red'),popup= folium.Popup("<b>The estimated electromagnetic radiation for this location is {}.</b>".format(self.prediction),max_width=500),
                       draggable=True).add_to(m),

        # Iterate over the array and add a marker for each coordinate
        for coord in self.coordinates_arr:
            lat, lon = coord[0], coord[1]
            folium.Marker(location=[lat, lon]).add_to(m)

            # Add a legend to the map
            legend_html = '''
                              <div style="position: fixed; 
                                          bottom: 75px; left: 50px; width: 300px; height: 400px; 
                                          border:2px solid grey; z-index:9999; font-size:17px;
                                          background-color:white;
                                          padding: 25px;
                                          ">
                                  &nbsp; <b>Markers explanation</b> <br><br>
                                  &nbsp; <i class="glyphicon glyphicon-map-marker" style="color:blue"></i> Blue markers<br>
                                  &nbsp; <b>Blue markers</b>: The blue markers are the Cosmote stores where the radiation measurements were taken. <br><br>
                                  &nbsp; <i class="glyphicon glyphicon-star" style="color:red"></i> Red marker<br>
                                  &nbsp; <b>Red marker</b>: The red marker is the location of the coordinates that the user inputted from the previous dialog. <br>
                                  <br>
                                  
                                  
                              </div>
            '''
            m.get_root().html.add_child(folium.Element(legend_html))

        # Display the map
        m.save('Radiation.html')

        # Open the HTML file in a browser automatically
        url = 'file://' + os.path.realpath('Radiation.html')
        webbrowser.open(url)


