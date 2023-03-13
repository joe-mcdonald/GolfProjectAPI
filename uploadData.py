from bs4 import BeautifulSoup
import requests
import pandas as pd
import json


soup = BeautifulSoup(requests.get('https://www.espn.com/golf/leaderboard/_/tour/pga').text, "html.parser")
tournament_name = soup.find_all("h1", class_="headline headline__h1 Leaderboard__Event__Title")[0].text
course_name = soup.find_all("div", class_="Leaderboard__Course__Location n8 clr-gray-04")[0].text
tournament_status = str(soup.find_all("div", class_="status cf mt4 mb4")[0].text)
if tournament_status == "Final":
    print("FINAL")
    column_names = "POS    PLAYER           SCORE R1  R2  R3  R4  TOTAL   Earnings  FEDEX PNTS"
    rows = soup.find_all("tr", class_="PlayerRow__Overview PlayerRow__Overview--expandable Table__TR Table__even")

    for i in range(0, len(soup.find_all("tr", class_="PlayerRow__Overview PlayerRow__Overview--expandable Table__TR Table__even"))):
        rows = soup.find_all("tr", class_="PlayerRow__Overview PlayerRow__Overview--expandable Table__TR Table__even")
        name = str(rows[i].find("a", class_="AnchorLink leaderboard_player_name").text.strip())
        nameParsedLen = len(name[0] + ". " + name.split(" ")[1])


        rows = soup.find_all("tr", class_="PlayerRow__Overview PlayerRow__Overview--expandable Table__TR Table__even")
        position = str(rows[i].find("td", class_="tl Table__TD").text.strip())


        name = str(rows[i].find("a", class_="AnchorLink leaderboard_player_name").text.strip())
        nameParsed = name[0] + ". " + name.split(" ")[1]

        score4 = rows[i].find_all("td", class_="Table__TD")[3].text.strip()


        r1 = rows[i].find_all("td", class_="Table__TD")[4].text.strip()


        r2 = rows[i].find_all("td", class_="Table__TD")[5].text.strip()


        r3 = rows[i].find_all("td", class_="Table__TD")[6].text.strip()


        r4 = rows[i].find_all("td", class_="Table__TD")[7].text.strip()


        total = rows[i].find_all("td", class_="Table__TD")[8].text.strip()


        earnings = rows[i].find_all("td", class_="Table__TD")[9].text.strip()


        fedexPnts = rows[i].find_all("td", class_="Table__TD")[10].text.strip()


        listObj = []
        with open('sample.json') as fp:
            listObj = json.load(fp)


        listObj[i]["position"] = str(position)
        listObj[i]["nameParsed"] = str(nameParsed)
        listObj[i]["score4"] = str(score4)
        listObj[i]["today"] = str(r1)
        listObj[i]["thru"] = str(r2)
        listObj[i]["score7"] = str(r3)
        listObj[i]["score8"] = str(r4)
        listObj[i]["score9"] = str(total)
        listObj[i]["score10"] = str(earnings)
        listObj[i]["total"] = str(fedexPnts)


        with open('sample.json', 'w') as json_file:
            json.dump(listObj, json_file, indent=4)
    exit()



column_names = "POS    PLAYER           SCORE TODAY THRU  R1   R2   R3   R4  TOTAL"
rows = soup.find_all("tr", class_="PlayerRow__Overview PlayerRow__Overview--expandable Table__TR Table__even")


for i in range(0, len(soup.find_all("tr", class_="PlayerRow__Overview PlayerRow__Overview--expandable Table__TR Table__even"))):
    rows = soup.find_all("tr", class_="PlayerRow__Overview PlayerRow__Overview--expandable Table__TR Table__even")
    name = str(rows[i].find("a", class_="AnchorLink leaderboard_player_name").text.strip())
    nameParsedLen = len(name[0] + ". " + name.split(" ")[1])


    rows = soup.find_all("tr", class_="PlayerRow__Overview PlayerRow__Overview--expandable Table__TR Table__even")
    position = str(rows[i].find("td", class_="tl Table__TD").text.strip())


    name = str(rows[i].find("a", class_="AnchorLink leaderboard_player_name").text.strip())
    nameParsed = name[0] + ". " + name.split(" ")[1]


    score4 = rows[i].find_all("td", class_="Table__TD")[4].text.strip()


    today = rows[i].find_all("td", class_="Table__TD")[5].text.strip()


    thru = rows[i].find_all("td", class_="Table__TD")[6].text.strip()


    score7 = rows[i].find_all("td", class_="Table__TD")[7].text.strip()


    score8 = rows[i].find_all("td", class_="Table__TD")[8].text.strip()


    score9 = rows[i].find_all("td", class_="Table__TD")[9].text.strip()


    score10 = rows[i].find_all("td", class_="Table__TD")[10].text.strip()


    total = rows[i].find_all("td", class_="Table__TD")[11].text.strip()


    listObj = []
    with open('sample.json') as fp:
        listObj = json.load(fp)


    listObj[i]["position"] = str(position)
    listObj[i]["nameParsed"] = str(nameParsed)
    listObj[i]["score4"] = str(score4)
    listObj[i]["today"] = str(today)
    listObj[i]["thru"] = str(thru)
    listObj[i]["score7"] = str(score7)
    listObj[i]["score8"] = str(score8)
    listObj[i]["score9"] = str(score9)
    listObj[i]["score10"] = str(score10)
    listObj[i]["total"] = str(total)


    with open('sample.json', 'w') as json_file:
        json.dump(listObj, json_file, indent=4)