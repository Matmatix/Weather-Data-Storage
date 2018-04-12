class DataObj:
    def __init__(self, key, data):
       #check key is int
       self.key = key
       self.data = data
    
    def getKey(self):
        return self.key

    def getData(self):
        return self.data