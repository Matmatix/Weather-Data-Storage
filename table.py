#This will be the class for the hash table

class HashTable:
    def __init__(self, length):
        if not isinstance(length, int) or length <= 0: #make the table at least one long
            length = 1
        self.length = length
        self.slots = [None for _ in range(0, self.length)]      #create a list of all of the slots for objects in the table, possibly other lists in each spot as we are chaining

    #used to find the location of a specific object
    def hashLocation(self, key):
        #use the hash number to specify which algorithm to use to hash the key
        #ie use the hasing class maybe
        return key % self.length

    #add a new object to the table
    def add(self, key, obj):
        location = self.hashLocation(key)                       #get the location to hash to
        if self.slots[location] is None:                        #check if the slot is filled if not add the object
            self.slots[location] = obj
        elif not isinstance(self.slots[location], list):             #if the slot already has a singular object in it replace with a list
            temp = self.slots[location]
            self.slots[location] = [temp, obj]
        else:                                                   #if already a list append object to the end of the list
            self.slots[location].append(obj)

    #update data that is already in the hash table
    def update(self, key, update):
        location = self.hashLocation(key)                  #if there is nothing to replace do nothing
        if not isinstance(self.slots[location], list):             #if there is only a single object there replace it
            self.slots[location] = update
        else:                                                   #if there is a list there look through the list to find the object to replace
            for x in range(0, len(self.slots[location])):
                if self.slots[location][x].getKey == key:          #compate the key provided to update to the each objects in the list's key
                    self.slots[location][x] = update
                    break

    #looking for the location of a specific object
    def search(self, key):
        location = self.hashLocation(key)
        if self.slots[location] is None:                    #return an error if the object associated with the key doesnt exist in the table
            return None
        elif not isinstance(self.slots[location], list):            #if there is only an object return that object
            return self.slots[location]
        else:                                               #if there is a list traverse it and compare keys looking for the same key
            for x in range(0, len(self.slots[location])):
                if self.slots[location][x].getKey == key:
                    return self.slots[location][x]
