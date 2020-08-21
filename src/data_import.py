import pandas as pd 
import numpy as np
import sys


# import the nba players csv
players = pd.read_csv('data/players.csv')

players_height = players.height.apply(lambda x: x.split('-'))

player_inches = [int(x[0])*12 + int(x[1]) for x in players_height]

players['height_inches'] = player_inches

salaries = pd.read_csv('data/salaries_1985to2018.csv')
player_salaries = pd.merge(players, salaries, how='inner', left_on = '_id', right_on='player_id')



# Prep divy trips

def prep_divy():
    divy_trips = pd.read_csv('data/Divvy_Trips_2020_Q1.csv')
    divy_trips['started_at'] = pd.to_datetime(divy_trips['started_at'])
    divy_trips['weekday'] = divy_trips['started_at'].apply(lambda x: x.isoweekday())
    divy_trips['hour'] = divy_trips['started_at'].apply(lambda x: x.hour)
    
    return divy_trips
