from NhlScrap.items import PlayItem	

INDEX_NUMBER = 0
INDEX_PERIOD = 1
INDEX_STRENGTH = 2
INDEX_TIME = 3
INDEX_EVENT = 4
INDEX_DESCRIPTION = 5
INDEX_AWAY_PLAYERS = 6
INDEX_HOME_PLAYERS = 7

def parseFields(fields):
	item = PlayItem()

	item['period'] = fields[INDEX_PERIOD].xpath("text()").extract()
	item['number'] = fields[INDEX_NUMBER].xpath("text()").extract()
	item['strength'] = fields[INDEX_STRENGTH].xpath("text()").extract()
	item['time'] = fields[INDEX_TIME].xpath("text()[1]").extract()
	item['event'] = fields[INDEX_EVENT].xpath("text()").extract()
	item['description'] = fields[INDEX_DESCRIPTION].xpath("text()").extract()	
	item['awayPlayers'] = fields[INDEX_AWAY_PLAYERS].xpath("./table/tr/td/table/tr/td/font/text()").extract()
	item['homePlayers'] = fields[INDEX_HOME_PLAYERS].xpath("./table/tr/td/table/tr/td/font/text()").extract()	

	return item

	