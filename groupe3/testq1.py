from question1 import *

print(plus_petit([[2], [33, 1], [1, 7]], 2))
"""
Notre code va passer dans la liste et regarder 
les premiers éléments, donc, il retournera [[1, 7], [2]]
"""
x = [[2], [3, 2], [3, 1]]
y = plus_petit(x, 2)
for a in y:
   a.sort()

print(x)
"""
on pose x = [[2], [3, 2], [3, 1]] et y = plus_petits(x, 2)
Donc y = [[2], [3, 1]]
Ensuite, on trie chaque élément de y, ce qui donne y = [[2], [1, 3]]
Enfin, on affiche x, qui a été modifié par le tri de y, donc x = [[2], [3, 2],[1, 3]]
"""

z = [1,6,19,-3,2,3.12,0,54,3,3.21]
z1 = [1,6,[19,-3,2],3.12,[0,54],3,3.21]
print(plus_petit(z,5))
print(plus_grand(z,4))
print(positifs_croissants(z1))
print(plus_grand([1,14,65,-1,0.15],4))
print(plus_petit([1,14,65,-1,0.15],4))
print(plus_grand([[3],[35]],2))
print(plus_grand([[31.2],[21,31,35]],2))

"""
[-3, 0, 1, 2, 3]
[54, 19, 6, 3.21]
[0, 1, 2, 3, 3.12, 3.21, 6, 19, 54]
[65, 14, 1, 0.15]
[-1, 0.15, 1, 14]
[[35], [3]]
[[31.2], [21, 31, 35]]
"""