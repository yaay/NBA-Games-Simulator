![NBA Game Simulator](header.png)

# NBA-Games-Simulator

This application will simulate NBA games for the purpose of predicting the outcomes of any game between two teams choosen by user. The games will be repeated by a number of times selected by user to approximate the chance of a particular team winning a match and the possibility of going to an overtime. 

This project have two componenets, a scraper and python application.

# Data Collection 
Teams data will be collected from stats.nba.com. This is a website by the NBA that have all the teams data and statistics for every game. Unfortunately the site doesn't have a public API, so we will be using the Requests library to access the data for the current NBA season. The data will be gathered and transformed into a DataFrame that will allow us to use it easily.
