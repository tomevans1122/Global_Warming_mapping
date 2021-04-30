# Global-Warming-Mapping

This project uses a downloaded JSON file from the OpenWeatherMap API which includes hourly weather reports for a set of coordinates (local to me) over a 40 year period.
The JSON file is too large to include in this repository, but here is a snippet of the data to give an idea of the information provided:

{"dt":315532800,"dt_iso":"1980-01-01 00:00:00 +0000 UTC","timezone":0,"main":{"temp":0.72,"temp_min":-1.42,"temp_max":2.16,"feels_like":-3.27,"pressure":1013,"humidity":86},"wind":{"speed":2.6,"deg":180},"clouds":{"all":90},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"city_name":"Llangrannog","lon":-4.47,"lat":52.16}

## Libraries Used

For the purposes of this project I have exploited the "temp" element of each entry. 
I used Numpy in order to organise the API data in arrays ready for plotting using Matplotlib.

## Figure

The figure includes 40 data points - the average temperature over 52 weeks of every year from 1981 to 2021. 
There is also a trendline included on the figure using the polyfit function of Matplotlib. I've extended the trendline to continue into the future to provide a basic prediction of the temperature rise over time (if all variables remain the same!!).
