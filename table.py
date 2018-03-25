#This will be the class for the hash table

class HashTable:
    def __init__(self, length, hash):
        if type(length) != int or length <= 0: #make the table at least one long
            length = 1
        if type(hash) != int or hash < 0 or hash > 1:           #this integer value(can possibly change later) will be used to choose a hashing alogrithm for this specific hash table
            hash = 0
        self.hash = hash
        self.length = length
        self.slots = [None for x in range(0, self.length)]      #create a list of all of the slots for objects in the table, possibly other lists in each spot as we are chaining

    #used to find the location of a specific object 
    def hashLocation(self, key):
        #use the hash number to specify which algorithm to use to hash the key
        #ie use the hasing class maybe
        if self.hash == 0:
            return 0

    #add a new object to the table
    def add(self, key, object):
        location = self.hashLocation(key)                       #get the location to hash to 
        if self.slots[location] == None:                        #check if the slot is filled if not add the object 
            self.slots[location] = object
        elif type(self.slots[location]) != list:             #if the slot already has a singular object in it replace with a list 
            temp = self.slots[location]
            self.slots[location] = [temp, object]
        else:                                                   #if already a list append object to the end of the list
            self.slots[location].append(object)
    
    #update data that is already in the hash table
    def update(self, key, update):
        location = self.hashLocation(key)                  #if there is nothing to replace do nothing
        if type(self.slots[location]) != list:             #if there is only a single object there replace it
            self.slots[location] = update 
        else:                                                   #if there is a list there look through the list to find the object to replace
            for x in range(0, len(self.slots[location])):
                if self.slots[location].getKey == key:          #compate the key provided to update to the each objects in the list's key
                    self.slots[location] = update
                    break
