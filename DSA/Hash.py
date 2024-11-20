# Hashset

s=set()
print(s)


#to add element in set  -O(1)
s.add(1)
s.add(2)
s.add(3)
print(s)

#to check wether element is in the set or not -O(1)
if 3 in s:
    print(bool(1))


#to remove element from a set
s.remove(2)
print(s)

#set construction -O(n)
string ='aaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbcccccccccddddddddeeeeeee'
sett=set(string)

print(sett)

#loop over items in set
for x in s:
    print(x)


#Hashmaps - Dictionaries
#Hashmap is a collection of key-value pairs

d={'greg':1,'steve':2,'rob':3}
print(d)

#Add key:val in dictionary -O(1)
d['john']=4
print(d)

#check wether key is in dictionary or not -O(1)
if 'greg' in d:
    print(bool(1))


#check the value corresponding to key in the dictionary -O(1)
print(d['greg'])

#looping over hashmap key val pair -O(n)
for key,val in d.items():
    print(f'key {key}: val {val}')

#Defaultdict

from collections import defaultdict
default = defaultdict(list)
default[2]
print(default[2])


#counter
from collections import Counter

counter=Counter(string)
print(counter)