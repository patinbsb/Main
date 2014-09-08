Welcome to my rep- page.

Included are various projects which may be work in progress and may have been adapted into other projects. Some of the codes may not be runnable as my API authentication key for websites such as twitch and Google have been removed for security purposes. If you would like to try these scripts please insert your own oauth key into the relevant area. All scripts running using python 2.x and relevant libraries

as of 08/09/2014 the project in this folder include:

irc_threaded.py: An irc application that runs the socket in a separate thread, this removes latency in the gui. an improvement on the twitch.py script. This script requires the user to replace the irc login information and provide an oauth key

weather.py: An application with a GUI that allows the user to look up the local weather information using IP geolocation. If this proves to be inaccurate the user can input a city and country name and be delivered the relevant weather information. This script requires the Beautiful soup library to run and also a Google API key which is input into the api_key string. This script uses the openweathermap API to get weather information in JSON format and the google maps api to convert country and city information into latitude and longitude information.

twitch.py: A script which uses the twitch.tv (an online streaming website for popular video games) IRC chat to predict when exciting highlights happen within a stream. When the chats post rate increases above the average for at least 20 posts a time stamp for the period when the highlight occurred and a text file containing the posts in the chat during the period of time is created. This script uses the twitch API to authenticate to the IRC server which can be input into the PASS string. Planning to improve accuracy which lies at ~80% from previous testing.

gui_wrapper.py: A test of the gui features of the tkinter library which expanded into adding and retrieving information from a database.

test2.py: a testing script which is for functionality tests of various projects. ignore this as it varies rapidly

Montypython.py: A fun project which hopes to get all sorts of information of the script from the movie Monty Python and the quest for the holy grail. Currently not feature complete.
