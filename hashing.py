# This is where our hashing algorithm will go
from table import HashTable
from dataObj import DataObj

hashtable = HashTable(3)

d0 = DataObj(10, 'green')
d1 = DataObj(12, 'small')
d2 = DataObj(3, 4)
d3 = DataObj(6, 10)

hashtable.add(d0.key, d0)
hashtable.add(d1.key, d1)
hashtable.add(d2.key, d2)
hashtable.add(d3.key, d3)


hashtable.remove(d3.key)



for k in range(hashtable.length):
    if isinstance(hashtable.slots[k], list):
        for t in range(len(hashtable.slots[k])):
            print '(', k,',', t, ')', hashtable.slots[k][t].data
    elif isinstance(hashtable.slots[k], DataObj):
        print '(', k,',', 0, ')', hashtable.slots[k].data