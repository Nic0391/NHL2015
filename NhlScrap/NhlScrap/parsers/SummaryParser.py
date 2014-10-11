from NhlScrap.items import SummaryItem, PlayerItem 

HOME_TEAM_INDEX = 0
AWAY_TEAM_INDEX = 25

HEADER_OFFSET = 2
NUM_PLAYERS = 20

PLAYER_NUMBER_INDEX = 0
PLAYER_POSITION_INDEX = 1
PLAYER_NAME_INDEX = 2
PLAYER_GOALS_INDEX = 3
PLAYER_ASSISTS_INDEX = 4
PLAYER_POINTS_INDEX = 5
PLAYER_PLUSMINUS_INDEX = 6
PLAYER_PIM_INDEX = 8
PLAYER_SHOTS_INDEX = 15
PLAYER_ATTEMPTED_SHOTS_INDEX = 16
PLAYER_MISSED_SHOTS_INDEX = 17
PLAYER_HITS_INDEX = 18
PLAYER_GIVEAWAYS_INDEX = 19
PLAYER_TAKEAWAYS_INDEX = 20
PLAYER_BLOCKED_SHOTS_INDEX = 21
PLAYER_FACEOFFS_LOST_INDEX = 22
PLAYER_FACEOFFS_WON_INDEX = 23

def parseSummary(lines):
	item = SummaryItem()
	item['teams'] = []
	item['teams'].append(parseTeam(HOME_TEAM_INDEX, lines))
	item['teams'].append(parseTeam(AWAY_TEAM_INDEX, lines))
	return item

def parseTeam(teamIndex, lines):
	team = {}
	team['name'] = lines[teamIndex].xpath("./td[1]/text()").extract()

	team['players'] = []
	startIndex = teamIndex + HEADER_OFFSET
	for i in range(startIndex, (startIndex + NUM_PLAYERS)):
		team['players'].append(dict(parsePlayer(lines[i])))
		
	return team

def parsePlayer(playerLine):
	playerFields = playerLine.xpath("./td/text()")
	player = PlayerItem()
	player['number'] = playerFields[PLAYER_NUMBER_INDEX].extract()
	player['position'] = playerFields[PLAYER_POSITION_INDEX].extract()
	player['firstName'] = playerFields[PLAYER_NAME_INDEX].extract().split(',')[1].strip()
	player['lastName'] = playerFields[PLAYER_NAME_INDEX].extract().split(',')[0]
	player['goals'] = int(playerFields[PLAYER_GOALS_INDEX].extract().replace(u'\u00a0', '0'))
	player['assists'] = int(playerFields[PLAYER_ASSISTS_INDEX].extract().replace(u'\u00a0', '0'))
	player['points'] = int(playerFields[PLAYER_POINTS_INDEX].extract().replace(u'\u00a0', '0'))
	player['plusMinus'] = int(playerFields[PLAYER_PLUSMINUS_INDEX].extract().replace(u'\u00a0', '0').replace('+', ''))
	player['pim'] = int(playerFields[PLAYER_PIM_INDEX].extract().replace(u'\u00a0', '0'))
	player['shots'] = int(playerFields[PLAYER_SHOTS_INDEX].extract().replace(u'\u00a0', '0'))
	player['attemptedShots'] = int(playerFields[PLAYER_ATTEMPTED_SHOTS_INDEX].extract().replace(u'\u00a0', '0'))
	player['missedShots'] = int(playerFields[PLAYER_MISSED_SHOTS_INDEX].extract().replace(u'\u00a0', '0'))
	player['hits'] = int(playerFields[PLAYER_HITS_INDEX].extract().replace(u'\u00a0', '0'))
	player['giveaways'] = int(playerFields[PLAYER_GIVEAWAYS_INDEX].extract().replace(u'\u00a0', '0'))
	player['takeaways'] = int(playerFields[PLAYER_TAKEAWAYS_INDEX].extract().replace(u'\u00a0', '0'))
	player['blockedShots'] = int(playerFields[PLAYER_TAKEAWAYS_INDEX].extract().replace(u'\u00a0', '0'))
	player['faceoffsWon'] = int(playerFields[PLAYER_TAKEAWAYS_INDEX].extract().replace(u'\u00a0', '0'))
	player['takeaways'] = int(playerFields[PLAYER_TAKEAWAYS_INDEX].extract().replace(u'\u00a0', '0'))

	return player