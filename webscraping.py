from bs4 import BeautifulSoup
import requests
page=requests.get("https://www.cricbuzz.com/live-cricket-scorecard/31633/aus-vs-ind-1st-odi-india-tour-of-australia-2020-21")
soup=BeautifulSoup(page.text)
print(soup)
table=soup.find("div",class_="cb-col cb-col-100 cb-ltst-wgt-hdr")
names=[x.get_text() for x in table.find_all("div",class_="cb-col cb-col-27")]
player_names=[]
for i in names:
   player_names.append(i.strip())
print(player_names)
runs=[x.get_text() for x in table.find_all("div",class_="cb-col cb-col-8 text-right text-bold")]
player_runs=runs[1:]
print(player_runs)
x=str(input("enter the player name:"))
x=x.capitalize()
for i in range(0,len(player_names)):
    if x==player_names[i]:
        print(f"The player name is {player_names[i]} and his innings runs is:{player_runs[i]}")




