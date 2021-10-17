import copy

#1
y = [1,2,3,4,5,6,7,8]
print(y)

#y = [*range(1,9)]
#print(y)

#newlist = [x for x in range(1,9)]
#print(newlist)

x = ["a","b","c","d","e","f","g","h"]
print("_"*10)

#2
CB = [["" for i in range(9)] for j in range(8)]
for i in range(len(y)):
    row = y[i]
    for j in range(len(x)):
        character = x[j]
        box = str(row) + character
        #print(i+1,j+1)
        CB[i][j-1]=box 
print(CB)
print("*********")

#3 
result = {}
for CB in CB:
    for item in CB[1:]:
        result[item] = CB[0]
print(result)
# =============================================================================
# CD1 = {}
# for i in y:
#  for value in x:
#  	CD1[i] = value
#  	x.remove(value)
#  	break
# print(str(CD1))
# =============================================================================
#PS: Feel Free To Comment Anything As Long As You Can See It And It's Correct

#4
#CB2 = copy.deepcopy(CB)
#print(CB2)
#y = ["P","R","N","B","Q","K","B","N","R"]
#x = ["w","b"]
#I am not sure on how to modify or change it with still deep copying cb.

#CB2 = [["" for q in range(9)] for w in range(3)]
#for q in range(len(y)):
   # row2 = y[q]
    #for w in range(len(x)):
     #   character2 = x[w]
      #  box2 = str(row2) + character2
       # CB2[q][w-1]= box2
#print(CB2)

#5
#You need #4




