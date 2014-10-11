import scrapy

class NhlItem(scrapy.Item):
	plays = scrapy.Field()
	url = scrapy.Field()

class PlayItem(scrapy.Item):
	period = scrapy.Field()
	number = scrapy.Field()
	strength = scrapy.Field()
	time = scrapy.Field()
	event = scrapy.Field()
	description = scrapy.Field()
	awayPlayers = scrapy.Field()
	homePlayers = scrapy.Field()

class SummaryItem(scrapy.Item):
	teams = scrapy.Field()
	url = scrapy.Field()

class PlayerItem(scrapy.Item):
	number = scrapy.Field()
	position = scrapy.Field()
	firstName = scrapy.Field()
	lastName = scrapy.Field()
	goals = scrapy.Field()
	assists = scrapy.Field()
	points = scrapy.Field()
	plusMinus = scrapy.Field()
	pim = scrapy.Field()
	shots = scrapy.Field()
	attemptedShots = scrapy.Field()
	missedShots = scrapy.Field()
	hits = scrapy.Field()
	giveaways = scrapy.Field()
	takeaways = scrapy.Field()
	blockedShots = scrapy.Field()
	faceoffsWon = scrapy.Field()
	faceoffsLost = scrapy.Field()