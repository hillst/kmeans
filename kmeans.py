# Load dataset into a list
# Randomly choose two points
# Calculate distance between all other nodes and those two points, put them in the group = to the closer one
# Calculate new center
# Classify again according to center
# Continue until no update.
import csv
import random

def load_dataset(filename):
    fd = csv.reader(open(filename, 'r'))
    initset = []
    for lines in fd:
        lines[0] = float((lines[0]))
        lines[1] = float((lines[1]))
        initset.append(lines)
    return initset   
    
def choose_base(set, k):
    #choose k random points and append them to base
    #upon choosing remove them
    #after we classify all our points, put them back in their respective groups
    base = []
    kbase = [] #the first element of each sublist is our "distance" measuring point.
    point_a = []
    point_b = []
    #creates k different items and puts them in our kbase list
    for i in range(k):
        kbase.append(set.pop(random.randint(0, len(set) - 1)))
        
    return kbase

def distance(point_a, point_b):
    return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])

def choose_cluster(clusters, point):
    mindistance = 1000000 #really big
    smallest = None
    for i in range(len(clusters)):
        if (distance(clusters[i], point)) <= mindistance:
            mindistance = distance(clusters[i],point)
            smallest = i
    #finds closest cluster and returns that index.
    return smallest

def calc_center(set, first = False):
    #our center is defined by 1/sizeofcluster * sum(elements)
    #on the first run our first point will be also be our center, so on each other one ignore the first point
    centers = []
    #print set
    for i in set:
        tmp = []
        sumx = 0
        sumy = 0
        print i
        #If it's the first time we are finding the center, our center is actually a point. so include it. otherwise ignore.
        if first == False:
            for j in i[1:]:
                sumx += j[0]
                sumy += j[1]
                tmp.append((1/len(i)) * sumx)
                tmp.append((1/len(i)) * sumy)
                i.insert(0,tmp)
        else:
            for j in i:
                sumy = sumy + j[1]
                sumx = sumx + j[0]
                tmp.append((1/len(i)) * sumx)
                tmp.append((1/len(i)) * sumy)
                i[0] = tmp
    return set
	
initset = load_dataset('cluster-data.csv')
#our working point is always the first element of kbase
#next thing to do is to group our sets
kbase = choose_base(initset, 3)
print kbase
for i in initset:
    kbase[choose_cluster(kbase, i)].append(i)
print kbase[0]
print "\n"
print kbase[1]
print "\n"
print kbase[2]
print "\n"
#Note that our centers are not being maintained as points, they hold two element spots which is fucking weird

 
        
    
