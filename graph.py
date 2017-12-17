

# This is a program made by Parsa Mansouri. It is an algorithm for the TSP (traveling salesperson problem).
# The aproach this algorithm takes is two part:
# First it runs a simple greedy algorithm on the coordinates given.
# Then, it looks at each line in the graph and optimizes it.

import turtle
import math
import random

totalcounter = 0
totalcounter2 = 0

def drawlist(xxxx): # This function draws the graph in turtle graphics.
    turtle.penup()
    turtle.goto(xxxx[0])
    turtle.pendown()
    loop = 1
    while loop < len(xxxx):
        turtle.goto(xxxx[loop])
        loop = loop + 1 
    turtle.goto(xxxx[0])
    
def distance(a, b):
    distance = math.sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2)) # Uses the pythagorean theorem to determine the distance between the two points.
    return distance

def fulldistance(xxx):# This function uses the previous function to determine the total length of a graph.
    length = len(xxx)
    summ = 0
    counter = 0

    while counter < length - 1:
        summ = summ + distance(xxx[counter], xxx[counter + 1])
        counter = counter + 1

    summ = summ + distance(xxx[counter], xxx[0])

    return summ

def shortestdistance(x, l, ul): # Where x is the point and l is the list of points.
    loop = len(l) - 1 
    sd = 2 * fulldistance(l) #This is the original "shortest distance" chosen because it ensures that there is atleast one value that will be determined smaller than it in the while loop.
    sdnum = 2
    
    
    while loop >= 0:
        
        if distance(x, l[loop]) < sd and distance(x, l[loop]) > 0 and l[loop] not in ul:
            sd = distance(x, l[loop])
            sdnum = loop
        loop = loop - 1

    return l[sdnum]

def subtractsets(set1, set2):# Set1 - Set2 -- I couldn't find any functions in pythons that worked for lists in this version.
    newset = []
    loop = 0
    while loop < len(set1):
        xx = set1[loop]
        if xx not in set2:
            newset.append(xx)
        loop = loop + 1
    return newset

def scp(listt, a, b, c): # Where a is the position of the first point of the line, b is the lower limit of the set of points being moved and c is the upper limit.
# This function puts the points from b to c, infront of a. It then checks if this modified list is

    global totalcounter
    totalcounter = totalcounter + 2 # + 2 because the algorithm also checks the reverse of the moving algorithms.  

    if len(listt) < 4:
        return listt # This is just to double check and make sure the list is of length 4 or more.

### This portion of the function calibrates the "moving objects".
    
    if b < c:
        mo = listt[b:c+1] #moving objects

    if b > c: # There are four possiblilities that must be manipulated differently. 
        
        if b == len(listt) - 1 and c == 0:
            mo = listt[b:b+1] + listt[c:c+1]
            
        if b != len(listt) - 1 and c != 0:
            mo = listt[b:len(listt)] + listt[0:c+1]

        if b == len(listt) - 1 and c != 0:
            mo = listt[b:b+1] + listt[0:c+1]
            
        if b != len(listt) - 1 and c == 0:
            mo = listt[b:len(listt)] + listt[c:c+1]

    if b == c:
        mo = [listt[b]]

### The moving objects have been set.
    
    #The following lines simply insert the mo in the correct position in the final list (which is going to be called nl)

    sp = listt[a] # This is the acutal point represented by 'a'.
    nl = subtractsets(listt, mo) # 'New List'-- The moving objects are subtracted from the original list and will later be put in their intended positions.        
    index = nl.index(sp) + 1 # This is the index of mo in nl.

    mo.reverse()# Reverse mo 
    ln = nl[0:index] + mo[0:len(mo)] + nl[index:len(nl)]
    mo.reverse()# Back to original

    nl = nl[0:index] + mo[0:len(mo)] + nl[index:len(nl)]

    if fulldistance(ln) < fulldistance(nl):# This 'if' statement checks to see if the reverse of mo produces a better result. If so, nl is modified accordingly.
        nl = ln


    if fulldistance(nl) < fulldistance(listt): 
        return nl
    else:
        return listt
        
def level1(llistt, pl, po):

    if pl == len(llistt) - 1:
        lo = llistt[0:pl]
    else:
        lo = llistt[0:pl] + llistt[pl+2:len(llistt)]

    var = llistt[po]
    i = lo.index(var)
    loop = i
    best = llistt #Before the while loop runs the 'best' graph is said to be the inputed list.
    
    while loop < len(lo):

        ii = llistt.index(lo[loop])

        #print pl, ii, po #This line may be used to show the vast amount of checks the computer caries out. 
        if ii > pl and po < pl:
            nl = scp(llistt, pl, ii, po)
        else:
            nl = scp(llistt, pl, po, ii)

        loop = loop + 1

        if fulldistance(nl) < fulldistance(best):
            best = nl

    return best

def lineop(lllist, line):#The line is represented by its first point in the list.
    # This function is very similar to that last, and can be thought of as the 'level2'.

    if line == len(lllist) - 1:
        lo = lllist[1:line]
    else:
        lo = lllist[0:line] + lllist[line+2:len(lllist)]

    loop = 0
    best = lllist #Before the while loop runs the 'best' graph is said to be the inputed list.

    global totalcounter2
    totalcounter2 = totalcounter2 + 1
    
    while loop < len(lo):

        ii = lllist.index(lo[loop])
        nl = level1(lllist, line, ii)
        loop = loop + 1

        if fulldistance(nl) < fulldistance(best):
            best = nl

    return best
    
        
#GREEDY ALGORITHM

"""
llist = [[600, 600], [73.1588, 72.6027], [423.7493, 428.0372], [509.4693, 426.8362], [512.0536, 520.2136], [112.1935, 453.8568], [54.4830, 231.6509], [266.2236, 220.0501], [168.0002, 365.8709], [180.0541, 359.8832], [87.0681, 286.3926], [315.6692, 103.6946], [457.7327, 520.4371],
         [221.3036, 324.1944], [464.6742, 403.1801], [549.3704, 134.9750], [10.0000, 346.6937], [152.5254, 450.5733], [257.7839, 341.6199], [354.1409, 149.3780], [371.5071, 590.0000], [430.2164, 347.7012], [428.4436, 526.3642], [384.8782, 133.7609], [246.6101, 409.2352], [53.7277, 276.0534],
         [51.3431, 442.4751], [138.0119, 393.6293], [427.1514, 411.3751], [589.0593, 215.0038], [493.3952, 289.8690], [438.2191, 334.2714], [392.4814, 357.9693], [58.8089, 181.2302], [311.7615, 353.9954], [165.5282, 248.1620], [130.9518, 202.2638], [261.5480, 383.9406], [595.9071, 303.7975],
         [507.6590, 368.8210], [56.6928, 367.5756], [394.4477, 513.8520], [188.3190, 445.5601], [211.9338, 223.0796], [513.5830, 234.8127], [256.7040, 513.9357], [195.8223, 110.9538], [379.3163, 268.0682], [419.0551, 230.5192], [382.4749, 174.4978], [523.4022, 491.6742], [171.4522, 31.8651],
         [168.9303, 293.8379], [97.2369, 149.8287], [24.3200, 366.1980], [58.4656, 232.0548], [147.4940, 473.6869], [458.7439, 267.5501], [276.8106, 51.5341], [330.1640, 499.7318], [516.7853, 226.8680], [534.9506, 337.7491], [186.7959, 494.8372], [297.4665, 259.6835], [339.0843, 125.1764],
         [456.5466, 279.3881], [301.4429, 341.7011], [241.7536, 551.8405], [504.5441, 194.1188], [300.6439, 163.8465], [559.7077, 243.4871], [542.6786, 164.3521], [99.5465, 367.5969], [404.9224, 278.8069], [195.4291, 96.0121], [361.0886, 415.9177], [233.4325, 74.1015],
         [343.2292, 338.0936], [484.3626, 122.6139], [81.8307, 430.1109], [40.6437, 429.6571], [266.8353, 10.0000], [86.7809, 336.4725], [468.0013, 344.5027], [171.3398, 542.6068], [578.7719, 403.2444], [539.0705, 180.1515], [335.8320, 362.5449], [165.5969, 315.6168],
         [416.6955, 512.8015], [313.8028, 257.0729], [322.4235, 295.7811], [233.9381, 419.6163], [260.6304, 462.8601], [49.2269, 445.3535], [208.4506, 270.0458], [466.2847, 260.2540], [575.2262, 269.1700], [349.3280, 109.7422], [543.8085, 328.3337], [396.3891, 185.0917]] # THIS IS THE LIST OF COORIDINATES THAT WILL BE USED.
        # Right now, they are randomly chosen, but they may be increased, decreased and changed to any set of points.

"""
llist = [[random.randrange(-200, 200),random.randrange(-200, 200)], [random.randrange(-200, 200),random.randrange(-200, 200)], [random.randrange(-200, 200),random.randrange(-200, 200)], [random.randrange(-200, 200),random.randrange(-200, 200)], [random.randrange(-200, 200),random.randrange(-200, 200)],
         [random.randrange(-200, 200),random.randrange(-200, 200)], [random.randrange(-200, 200),random.randrange(-200, 200)], [random.randrange(-200, 200),random.randrange(-200, 200)], [random.randrange(-200, 200),random.randrange(-200, 200)], [random.randrange(-200, 200),random.randrange(-200, 200)],
         [random.randrange(-200, 200),random.randrange(-200, 200)], [random.randrange(-200, 200),random.randrange(-200, 200)], [random.randrange(-200, 200),random.randrange(-200, 200)], [random.randrange(-200, 200),random.randrange(-200, 200)], [random.randrange(-200, 200),random.randrange(-200, 200)],
         [random.randrange(-200, 200),random.randrange(-200, 200)], [random.randrange(-200, 200),random.randrange(-200, 200)], [random.randrange(-200, 200),random.randrange(-200, 200)], [random.randrange(-200, 200),random.randrange(-200, 200)], [random.randrange(-200, 200),random.randrange(-200, 200)],
         [random.randrange(-200, 200),random.randrange(-200, 200)], [random.randrange(-200, 200),random.randrange(-200, 200)], [random.randrange(-200, 200),random.randrange(-200, 200)], [random.randrange(-200, 200),random.randrange(-200, 200)], [random.randrange(-200, 200),random.randrange(-200, 200)]]
"""

llist = [[6734, 1453], [2233, 10], [5530, 1424], [401, 841], [3082, 1644], [7608, 4458], [7573, 3716], [7265, 1268], [6898, 1885], [1112, 2049], [5468, 2606], [5989, 2873], [4706, 2674], [4612, 2035], [6347, 2683], [6107, 669], [7611, 5184], [7462, 3590], [7732, 4723], [5900, 3561], [4483, 3369],
         [6101, 1110], [5199, 2182], [1633, 2809], [4307, 2322], [675, 1006], [7555, 4819], [7541, 3981], [3177, 756], [7352, 4506], [7545, 2801], [3245, 3305], [6426, 3173], [4608, 1198], [23, 2216], [7248, 3779], [7762, 4595], [7392, 2244], [3484, 2829], [6271, 2135], [4985, 140], [1916, 1569],
         [7280, 4899], [7509, 3239],[10, 2676], [6807, 2993], [5185, 3258], [3023, 1942]]

"""
"""

llist = [[20833.3333, 17100.0000], [20900.0000, 17066.6667], [21300.0000, 13016.6667], [21600.0000, 14150.0000], [21600.0000, 14966.6667], [21600.0000, 16500.0000], [22183.3333, 13133.3333], [22583.3333, 14300.0000], [22683.3333, 12716.6667], [23616.6667, 15866.6667], [23700.0000, 15933.3333],
         [23883.3333, 14533.3333], [24166.6667, 13250.0000], [25149.1667, 12365.8333], [26133.3333, 14500.0000], [26150.0000, 10550.0000], [26283.3333, 12766.6667], [26433.3333, 13433.3333], [26550.0000, 13850.0000], [26733.3333, 11683.3333], [27026.1111, 13051.9444], [27096.1111, 13415.8333],
         [27153.6111, 13203.3333], [27166.6667, 9833.3333], [27233.3333, 10450.0000], [27233.3333, 11783.3333], [27266.6667, 10383.3333], [27433.3333, 12400.0000], [27462.5000, 12992.2222]]
"""
length = len(llist)

alg = [llist[0]]

usedlist = [llist[0]]

loop = 0

var = llist[0]


while loop < length - 1:
    
    var1 = shortestdistance(var, llist, usedlist)
    alg.append(var1)
    usedlist.append(var1)
    var = var1
    loop = loop + 1

if fulldistance(alg) > fulldistance(llist):
    alg = llist

# END OF GREEDY ALGORITHM



##########
#OPTIMIZATION

# So far, the function lineop uses the level1 and scp functions in particular to fully optimize a line.
# Meaning that it can check and see whether the graph would benefit if certain points were included in between the particular line.
# Now, the optimization will run the lineop function for all lines, and it will re-run the function until the graph is fully optimized.

print "This is Parsa Mansouri's TSP optimization algorithm."

check = "no"

while check == "no":  

    print "Checking"
    
    loop = 0
    prev = alg

    while loop < length:# This while loop checks all the lines for the possibility of optimization.
        alg = lineop(alg, loop)
        loop = loop + 1

    if prev == alg:# This 'if' statement works to break the while loop only when the above while loop has run atleast once without making any changes. 
        check = "yes"

#END OF OPTIMIZATION
        
print "The algorithm runs through", totalcounter, "many situations."
print "This is the list representing the optimal graph for the randomly chosen 40 points:", alg
print "The distance of this graph is:", fulldistance(alg)

drawlist(alg)

"""
lop = [1, 8, 38, 31, 44, 18, 7, 28, 6, 37, 19, 27, 17, 43, 30, 36, 46, 33, 20, 47, 21, 32, 39, 48, 5, 42, 24, 10, 45, 35,  4, 26, 2, 29, 34, 41, 16, 22, 3, 23, 14, 25, 13, 11, 12, 15, 40, 9]

print len(lop), len(llist)

optimal = []
loop = 0
while loop < len(llist):
    optimal.append(llist[lop[loop]-1])
    loop = loop + 1

print fulldistance(optimal)/fulldistance(alg)

"""











