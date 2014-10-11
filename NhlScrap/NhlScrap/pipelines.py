import json

class NhlScrapPipeline(object):
    def process_item(self, item, spider):
    	fileSplitList = item['url'].split("/")
    	fileUrl = fileSplitList[len(fileSplitList) - 1]
    	self.file = open(fileUrl, 'wb')
    	content = json.dumps(dict(item))
        self.file.write(content)
        self.file.close()
        
        return item