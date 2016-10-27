import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from playerinfo import PlayerInfo
import re
from pprint import pprint


def get_roster(idx):
    player_table = soup.find_all(
        'table', class_='playerTableTable')[idx].find_all('tr', 'pncPlayerRow')
    roster_list = []
    for n in range(len(player_table)):
        try:
            player = str(player_table[n].a).split('>')[1].split('</a')[0]
            roster_list.append(player)
        except (IndexError):
            pass
    return roster_list


def return_rosters(espn_league_url=None):
    """
    Will ask you to enter username and password for the espn fantasy login.
    """
    if espn_league_url is None:
        espn_league_url = "http://games.espn.com/fba/leagueoffice?leagueId=133847&seasonId=2017"
    driver = webdriver.Chrome()

    driver.get(espn_league_url)
    #implement wait it is mandatory in this case
    WebDriverWait(driver,1000).until(EC.presence_of_all_elements_located((By.XPATH,"(//iframe)")))
    frms = driver.find_elements_by_xpath("(//iframe)")

    driver.switch_to_frame(frms[2])
    time.sleep(2)
    driver.find_element_by_xpath("(//input)[1]").send_keys(input("username: "))
    driver.find_element_by_xpath("(//input)[2]").send_keys(input("password: "))
    driver.find_element_by_xpath("//button").click()
    driver.switch_to_default_content()
    time.sleep(4)

    rosters_button = driver.find_elements_by_xpath("//ul[@id='games-subnav-links']/*")[3]
    rosters_button.click()

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    team_names = []
    team_ids = range(1, 11)
    for tag in soup.find_all('tr', class_='playerTableBgRowHead'):
        team_names.append(str(tag.a).split('>')[1].split('<')[0].lower())


    roster_dict = {}
    for i, team in enumerate(team_names):
        roster_dict[team] = get_roster(i)

    driver.close()
    
    return roster_dict
