# This is where our hashing algorithm will go
from table import HashTable
hashtable = HashTable(3, 0)

hashtable.add('color', 'green')
#hashtable.add('size', 'small')
#hashtable.add('number', 4)

print(hashtable.length)