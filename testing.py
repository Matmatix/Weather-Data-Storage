from table import HashTable
from dataObj import DataObj
import time
from random import *

seed(a = None)
file = open("data.txt", "r")
read_data = file.readlines()

hashtable = HashTable(1201)
for i in range(1080):
    data_arr = read_data[i].split(",", 1)

    obj = DataObj(int(data_arr[0]), data_arr[1])
    hashtable.add(int(data_arr[0]), obj)

start = time.time()
for i in range(1080):
    data_arr = read_data[i].split(",", 1)
    hashtable.search(int(data_arr[0]))
end = time.time()

print(end - start)

file.close()

