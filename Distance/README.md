# Distance Data Usage of Python File Explained
1. use [Request_From_UREG.py](https://github.com/awesome-schedule/data/blob/master/Distance/Request_From_UREG.py) to scrape data from official building list on [UREG](http://www.virginia.edu/registrar/buildings.html)
* The program scrapes and saves the data to [Building_Names.json](https://github.com/awesome-schedule/data/blob/master/Distance/Building_Names.json)
2. use [GoogleMapRequests.py](https://github.com/awesome-schedule/data/blob/master/Distance/GoogleMapRequests.py) to create the following data files: 
* [Building_Array.json](https://github.com/awesome-schedule/data/blob/master/Distance/Building_Array.json): The 1d array serving as a dictionary which uses index as key and the building names as value
* [Building_MetaData.json](https://github.com/awesome-schedule/data/blob/master/Distance/Building_MetaData.json): Meta Data related to Google Geocoding API
* [Time_Matrix.json](https://github.com/awesome-schedule/data/blob/master/Distance/Time_Matrix.json): The 2d array serving as a dictionary which contains the time it takes to walk from one building to another. Use Building_Array to look up the name of the building in each index
* [Distance_MetaData.json](https://github.com/awesome-schedule/data/blob/master/Distance/Distance_MetaData.json): Meta Data related to Google Distance Matrix API

### Remark: Functions in GoogleMapRequests.py Explained
api_key in the file has expired. Create a google map platform account to retrieve a valid api before running the program. The instruction can be found at [https://cloud.google.com/maps-platform/](https://cloud.google.com/maps-platform/)
