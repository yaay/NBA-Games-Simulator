#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import requests
import csv
import matplotlib.pyplot as plt


# ### 1 - Getting Games Data 
# 

# In[2]:


url = "https://stats.nba.com/stats/teamgamelogs?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlusMinus=N&Rank=N&Season=2021-22&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&VsConference=&VsDivision="


# In[3]:


# using the headers to fool Adam Silver
headers  = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-token': 'true',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'x-nba-stats-origin': 'stats',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://stats.nba.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}


# In[4]:


response = requests.get(url=url, headers=headers).json()


# In[5]:


data = response['resultSets'][0]['rowSet']


# In[6]:


columns = response['resultSets'][0]['headers']


#  ### 2 - Cleaning Data and Getting Points for Opponent

# In[7]:
print(r"""
 @@,,,,,,,@@@@*,,,,@@      ,,,,,,,,    ,,,,,   ,,,,,,,,,,,,        .,,,,,,,,    
 @,,,,,,,,@@@@,,,,,,@      ,,,,,,,,,   ,,,,,   ,,,,,,,,,,,,,,      ,,,,,,,,,,   
 @,,,,,,@@@@%,,,,,,,@      ,,,,,,,,,   ,,,,,   ,,,,,,   ,,,,,,     ,,,, ,,,,,   
 @,,,@@@@@@@@@@,,,,,@      ,,,,,,,,,   ,,,,,   ,,,,,,   ,,,,,,     ,,,, ,,,,,   
 @,#@@@@@@@@@@@@,,,,@      ,,,,,,,,,,  ,,,,,   ,,,,,,   ,,,,,,     ,,,, ,,,,,   
 @@@@@@@@@@@,,@@&,,,@      ,,,,,,,,,,  ,,,,,   ,,,,,,   ,,,,,,    ,,,,, ,,,,,.  
 @@@@@@@@@@*,,,@@,,,@      ,,,,,,,,,,. ,,,,,   ,,,,,,   ,,,,,,    ,,,,, ,,,,,,  
 @,@@@@@@@@@@,,,@@,,@      ,,,,, ,,,,, ,,,,,   ,,,,,,   ,,,,,,    ,,,,,  ,,,,,  
 @,@@@@@@@@@@,@@@@@@@      ,,,,, ,,,,, ,,,,,   ,,,,,,,,,,,,,,     ,,,,,  ,,,,,  
 @,,@@@@@@@@@@@@@@@@@      ,,,,, ,,,,,,,,,,,   ,,,,,,,,,,,,,,    ,,,,,,  ,,,,,. 
 @,,,,@@@@@@@@,,@@,,@      ,,,,,  ,,,,, ,,,,   ,,,,,,   ,,,,,,   ,,,,,   ,,,,,, 
 @,,,,,,@@@@@@@,,,,,@      ,,,,,  ,,,,, ,,,,   ,,,,,,   ,,,,,,   ,,,,,   ,,,,,, 
 @,,,,,,,*@@@@@@,,,,@      ,,,,,  ,,,,,,,,,,   ,,,,,,   ,,,,,,   ,,,,,   ,,,,,, 
 @,,,,,,,,,,@@@@,,,,@      ,,,,,   ,,,,,,,,,   ,,,,,,   ,,,,,,  ,,,,,,,,,,,,,,, 
 @,,,,,,,,,,,,,@@,,,@      ,,,,,   ,,,,,,,,,   ,,,,,,   ,,,,,,  ,,,,,,,,,,,,,,,,
 @,,,,,,,,,,,,,%@,,,@      ,,,,,    ,,,,,,,,   ,,,,,,   ,,,,,,  ,,,,,,    ,,,,,,
 @,,,,,,,,,,,,,,@,,,@      ,,,,,    ,,,,,,,,   ,,,,,,,,,,,,,,   ,,,,,,    ,,,,,,
 @&,,,,,,,,,,,,,@@,@@      ,,,,,    ,,,,,,,,   ,,,,,,,,,,,,    ,,,,,,     ,,,,,,
  _____                              _____ _                 _       _             
 / ____|                            / ____(_)               | |     | |            
| |  __  __ _ _ __ ___   ___  ___  | (___  _ _ __ ___  _   _| | __ _| |_ ___  _ __ 
| | |_ |/ _` | '_ ` _ \ / _ \/ __|  \___ \| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|
| |__| | (_| | | | | | |  __/\__ \  ____) | | | | | | | |_| | | (_| | || (_) | |   
 \_____|\__,_|_| |_| |_|\___||___/ |_____/|_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|   
                                                                                                          
                                                                                                          
""")
print('Welcome to the NBA Game Simulator!')
Team1 = input("Entre the Home Team Name: ")
Team2 = input("Entre the Away Team Name: ")
HN = int(input("Entre the Number of Simulations to Run: "))
nba_df = pd.DataFrame(data, columns=columns)


# In[8]:


nba_df.columns


# In[9]:


nba_df['PLUS_MINUS']


# In[10]:


nba_df['ABS_PLUS_MINUS'] = nba_df['PLUS_MINUS'].abs()


# In[11]:


nba_df['ABS_PLUS_MINUS']


# In[12]:


tdf_w = nba_df[nba_df['WL'] == 'W']


# In[13]:


tdf_L = nba_df[nba_df['WL'] == 'L']


# In[14]:


nba_df['OPT_PTS'] = tdf_w['PTS'] - tdf_w['PLUS_MINUS']


# In[15]:


nba_df['OPT_PTS'].update(tdf_L['PTS'] + tdf_L['ABS_PLUS_MINUS'])


# In[16]:


nba_df.head()


# In[17]:


mavs = nba_df[nba_df['TEAM_NAME'] == Team1]
suns = nba_df[nba_df['TEAM_NAME'] == Team2]


# In[18]:


mavs['PTS'].hist()
suns['PTS'].hist()


# In[19]:


mavs['OPT_PTS'].hist()
suns['OPT_PTS'].hist()


# In[20]:


mavs_mean_pts = mavs['PTS'].mean()
mavs_std_pts = mavs['PTS'].std()
mavs_mean_opts = mavs['OPT_PTS'].mean()
mavs_std_opts = mavs['OPT_PTS'].std()

suns_mean_pts = suns['PTS'].mean()
suns_std_pts = suns['PTS'].std()
suns_mean_opts = suns['OPT_PTS'].mean()
suns_std_opts = suns['OPT_PTS'].std()


# In[21]:


def simulator():
    mavs_score = (np.random.normal(mavs_mean_pts, mavs_std_pts)+ np.random.normal(suns_mean_opts, suns_std_opts))/2
    suns_score = (np.random.normal(suns_mean_pts, suns_std_pts)+ np.random.normal(mavs_mean_opts, mavs_std_opts))/2
    if int(round(mavs_score)) > int(round(suns_score)):
        return 1
    elif int(round(mavs_score)) < int(round(suns_score)):
        return -1
    else: return 0


# In[22]:


def nsimulator(n):
    gamesout = []
    team1win = 0
    team2win = 0
    tie = 0
    for i in range(n):
        gm = simulator()
        gamesout.append(gm)
        if gm == 1:
            team1win +=1 
        elif gm == -1:
            team2win +=1
        else: tie +=1 
    print(Team1 +' Win ', team1win/(team1win+team2win+tie),'%')
    print(Team2+' Win ', team2win/(team1win+team2win+tie),'%')
    print('Possibility of Overtime ', tie/(team1win+team2win+tie), '%')
    return gamesout


# In[ ]:


nsimulator(HN)


# In[ ]:




