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