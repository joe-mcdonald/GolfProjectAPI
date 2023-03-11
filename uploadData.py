# import library
from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
from io import StringIO
import csv

# def mainHello():    
soup = BeautifulSoup(requests.get('https://www.espn.com/golf/leaderboard/_/tour/pga').text, "html.parser")
tournament_name = soup.find_all("h1", class_="headline headline__h1 Leaderboard__Event__Title")[0].text
course_name = soup.find_all("div", class_="Leaderboard__Course__Location n8 clr-gray-04")[0].text
tournament_status = str(soup.find_all("div", class_="status cf mt4 mb4")[0].text)
column_names = "POS    PLAYER           SCORE TODAY THRU  R1   R2   R3   R4  TOTAL"
rows = soup.find_all("tr", class_="PlayerRow__Overview PlayerRow__Overview--expandable Table__TR Table__even")

print("\n\nTournament: " + tournament_name + "\nCourse: " + course_name + '\n' + tournament_status.split("Auto")[0] + '\n\n' + '_' * len(column_names) + '\n\n' + column_names + ('\n' + '_' * len(column_names)))

longest_name_len = 0
output_length_override = False # set this to false to only display the top 10 players



for i in range(0, len(soup.find_all("tr", class_="PlayerRow__Overview PlayerRow__Overview--expandable Table__TR Table__even"))):
    rows = soup.find_all("tr", class_="PlayerRow__Overview PlayerRow__Overview--expandable Table__TR Table__even")
    name = str(rows[i].find("a", class_="AnchorLink leaderboard_player_name").text.strip())
    nameParsedLen = len(name[0] + ". " + name.split(" ")[1])
    # if(nameParsedLen > longest_name_len):
        # longest_name_len = nameParsedLen


    rows = soup.find_all("tr", class_="PlayerRow__Overview PlayerRow__Overview--expandable Table__TR Table__even")
    position = str(rows[i].find("td", class_="tl Table__TD").text.strip()) #position good
    # if len(str(position)) == 1:
        # position += ' ' * 3
    # elif len(str(position)) == 2:
        # position += ' ' * 2
    # elif len(str(position)) == 3:
        # position += ' ' * 1
    # elif position == "-":
        # position = "WD "


    name = str(rows[i].find("a", class_="AnchorLink leaderboard_player_name").text.strip())
    nameParsed = name[0] + ". " + name.split(" ")[1]
    # nameParsed += ' ' * (longest_name_len - len(str(nameParsed)))


    score4 = rows[i].find_all("td", class_="Table__TD")[4].text.strip()
    # if score4 == 'E':
        # score4 = " E "
    # if score4 == '-':
        # score4 = "WD"
    # else:
        # score4 += ((3-len(str(score4))) * ' ')


    today = rows[i].find_all("td", class_="Table__TD")[5].text.strip()
    # if today == 'E':
        # today = " E"
    # if today == '-':
        # today = "WD "
    # else:
        # today += ((3-len(str(today))) * ' ')


    thru = rows[i].find_all("td", class_="Table__TD")[6].text.strip()
    # if len(str(thru)) == 1:
        # thru += ' '


    score7 = rows[i].find_all("td", class_="Table__TD")[7].text.strip()
    # if score7 == 'E':
        # score7 = " E "
    # if score7 == '-':
        # score7 = "WD"
    # else:
        # score7 += ((2-len(str(score7))) * ' ')


    score8 = rows[i].find_all("td", class_="Table__TD")[8].text.strip()
    # if score8 == 'E':
        # score8 = " E "
    # if score8 == '-':
        # score8 = "WD"
    # else:
        # score8 += ((2-len(str(score8))) * ' ')


    score9 = rows[i].find_all("td", class_="Table__TD")[9].text.strip()
    # if score9 == 'E':
    #     score9 = " E "
    # if score9 == '-':
    #     score9 = "WD"
    # else:
        # score9 += ((2-len(str(score9))) * ' ')


    score10 = rows[i].find_all("td", class_="Table__TD")[10].text.strip()
    # if score10 == 'E':
    #     score10 = " E "
    # if score10 == '-':
    #     score10 = "WD"
    # else:
        # score10 += ((2-len(str(score10))) * ' ')


    total = rows[i].find_all("td", class_="Table__TD")[11].text.strip()


    listObj = []

    with open('sample.json') as fp:
        listObj = json.load(fp)
    
    # del listObj[i]["position"]
    # del listObj[i]["nameParsed"]
    # del listObj[i]["score4"]
    # del listObj[i]["today"]
    # del listObj[i]["thru"]
    # del listObj[i]["score7"]
    # del listObj[i]["score8"]
    # del listObj[i]["score9"]
    # del listObj[i]["score10"]

    
    
    # listObj.append({
    #     "position": str(position),
    #     "nameParsed": str(nameParsed),
    #     "score4": str(score4),
    #     "today": str(today),
    #     "thru": str(thru),
    #     "score7": str(score7),
    #     "score8": str(score8),
    #     "score9": str(score9),
    #     "score10": str(score10)
    # })
    listObj[i]["position"] = str(position)
    listObj[i]["nameParsed"] = str(nameParsed)
    listObj[i]["score4"] = str(score4)
    listObj[i]["today"] = str(today)
    listObj[i]["thru"] = str(thru)
    listObj[i]["score7"] = str(score7)
    listObj[i]["score8"] = str(score8)
    listObj[i]["score9"] = str(score9)
    listObj[i]["score10"] = str(score10)
    
    print(listObj)
    
    with open('sample.json', 'w') as json_file:
        json.dump(listObj, json_file, indent=4)
    

    # print(position + " | " + str(nameParsed) + " | " + score4 + " | " + today + " | " + thru + " | " + score7 + " | " + score8 + " | " + score9 + " | " + score10 + " | " + total)

    