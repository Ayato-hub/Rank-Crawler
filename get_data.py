from __future__ import division
import urllib.parse
import os

import sqlite3

import time
from datetime import datetime
import schedule

import requests

from requests.auth import AuthBase




division_list = {
    "IRONE" : 0,
    "BRONZE" : 400,
    "SILVER" : 800,
    "GOLD" : 1200,
    "PLATINUM" : 1600,
    "DIAMOND" : 2000,
    "MASTER" : 2400,
    "GANDMASTER" : 2400,
    "CHALLENGER" : 2400
}

tier_list = {
    "I" : 300,
    "II" : 200,
    "III" : 100,
    "IV" : 0
}



# https://docs.python-requests.org/en/latest/user/advanced/#custom-authentication
class RiotAuth(AuthBase):
    def __init__(self, api_key):
        self.api_key = api_key

    def __call__(self, r):
        r.headers["X-Riot-Token"] = self.api_key
        return r



class RiotClient:
    def __init__(self, api_key, region="euw1"):
        self.auth = RiotAuth(api_key)
        self.endpoint = f"https://{region}.api.riotgames.com"
        # https://docs.python-requests.org/en/latest/user/advanced/#session-objects
        self.session = requests.Session()
        self.session.auth = self.auth

    def get_summoner_v4(self, summoner_name):
        summoner_name = urllib.parse.quote(summoner_name)
        return self.session.get(
            f"{self.endpoint}/lol/summoner/v4/summoners/by-name/{summoner_name}"
        ).json()

    def get_summoner_entries(self, summoner_id):
        return self.session.get(
            f"{self.endpoint}/lol/league/v4/entries/by-summoner/{summoner_id}"
        ).json()



"""def print_summoner_ranks(summoner_entries):
    print(f"{summoner_entries[0]['summoner_name']}:")
    for e in summoner_entries:
        print(f"{e['queueType']}: {e['tier']} {e['rank']} {e['leaguePoints']}")
    print("")"""



def main(summoner_name):
    api_key = "******************************************"

    client = RiotClient(api_key)

    summoner_id = client.get_summoner_v4(summoner_name)["id"]
    summoner_entries = client.get_summoner_entries(summoner_id)

    # 

    for e in summoner_entries:
        # Opens the connection
        conn = sqlite3.connect('riot_api_database.db')
        c = conn.cursor()

        if e['queueType'] == "RANKED_SOLO_5x5":
            SoloDivision = e['tier']
            SoloTier = e['rank']
            SoloLp = e['leaguePoints']
            SoloRelRank = division_list[SoloDivision] + tier_list[SoloTier] + SoloLp
            SoloLastSumIndex = 0
            SoloLastLp = None

            c.execute(f"SELECT Lp FROM {e['queueType']} WHERE SummonerName = ? ORDER BY date DESC LIMIT 1", (
                [summoner_name]
                ))
            temp = c.fetchone()
            if temp: SoloLastLp = temp[0]

            if SoloLp != SoloLastLp:
                c.execute(f"SELECT SummonerIndex FROM {e['queueType']} WHERE SummonerName = ? ORDER BY date DESC LIMIT 1", (
                    [summoner_name]
                    ))
                temp = c.fetchone()
                
                if temp: SoloLastSumIndex = temp[0]
                SoloSumIndex = SoloLastSumIndex + 1

                
                c.execute("INSERT INTO RANKED_SOLO_5x5 VALUES(datetime('now'), ?, ?, ?, ?, ?, ?, ?)",(
                    SoloSumIndex, summoner_name, summoner_id, SoloDivision, SoloTier, SoloLp, SoloRelRank
                    ))
                print("")
                print(f"Saving data from >>{summoner_name}<< to the Database:")
                print("")
                print("Mode: Solo")
                print(f"Division: {SoloDivision}")
                print(f"Tier: {SoloTier}")
                print(f"LP: {SoloLp}")
                print(f"Relativ LP: {SoloRelRank}")
                print("")



        if e['queueType'] == "RANKED_FLEX_SR":
            FlexDivision = e['tier']
            FlexTier = e['rank']
            FlexLp = e['leaguePoints']
            FlexRelRank = division_list[FlexDivision] + tier_list[FlexTier] + FlexLp
            FlexLastSumIndex = 0
            FlexLastLp = None

            c.execute(f"SELECT Lp FROM {e['queueType']} WHERE SummonerName = ? ORDER BY date DESC LIMIT 1", (
                [summoner_name]
                ))
            temp = c.fetchone()
            if temp: FlexLastLp = temp[0]

            if FlexLp != FlexLastLp:
                c.execute(f"SELECT SummonerIndex FROM {e['queueType']} WHERE SummonerName = ? ORDER BY date DESC LIMIT 1", (
                    [summoner_name]
                    ))
                temp = c.fetchone()
                
                if temp: FlexLastSumIndex = temp[0]
                FlexSumIndex = FlexLastSumIndex + 1

                
                c.execute("INSERT INTO RANKED_FLEX_SR VALUES(datetime('now'), ?, ?, ?, ?, ?, ?, ?)",(
                    FlexSumIndex, summoner_name, summoner_id, FlexDivision, FlexTier, FlexLp, FlexRelRank
                    ))
                print("")
                print(f"Saving data from >>{summoner_name}<< to the Database:")
                print("")
                print("Mode: Flex")
                print(f"Division: {FlexDivision}")
                print(f"Tier: {FlexTier}")
                print(f"LP: {FlexLp}")
                print(f"Relativ LP: {FlexRelRank}")
                print("")



        # Comit our command
        conn.commit()

        # Close the connection
        conn.close()
                
    
 
def run_main():
    print("")
    print(f"Time: {datetime.now()}")
    print("")
    sum_list = [
        "G5 Easy",
        "WeingottBachus",
        "pyke del oro",
        "KelpKannon",
        "xXSM3SHXx",
        "G5 EZAY",
        "BlxckSentix",
        "dying alive",
        "Leo5000Twitch",
        "Shinzoυ",
        "zLkiiii",
        "ADHSMR",
        "Reax05",
        "2muchAD4u",
        "Sren778"
    ]

    i = 0
    f = len(sum_list) - 1
    while i <= f:
        print(sum_list[i])
        main(sum_list[i])
        i = i+1
        #time.sleep(20)


run_main()

schedule.every(5).minutes.at(":00").do(run_main)

try:
    while True:
        schedule.run_pending()
        time.sleep(1)

except Expection as e:
    print(e,datetime.datetime.now())
