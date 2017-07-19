import random
import matplotlib.pyplot as mp

data_set =[]
f = open("clusters.txt", 'r')
for line in f.readlines():
    app = map(float, line.split(','))
    line_tuple = tuple(app)
    data_set.append(line_tuple)

print data_set
f.close()

def calmeans(listofpoint,key):
    sumofx = 0.0
    sumofy = 0.0
    count = 0.0

    for point in listofpoint[key]:
        sumofx = sumofx + float(point[0])
        sumofy = sumofy + float(point[1])
        count = count + 1

    meanofx = sumofx / count
    meanofy = sumofy / count
    cenpoint = (meanofx,meanofy)
    listofpoint[key][0] = cenpoint

    return cenpoint,listofpoint


def cluster(data_set,class_a,class_b,class_c):

    for point in data_set:
        distance = []

        distance_a = ((point[0] - class_a["a"][0][0])**2 + (point[1] - class_a["a"][0][1])**2)**0.5
        distance_b = ((point[0] - class_b["b"][0][0])**2 + (point[1] - class_b["b"][0][1])**2)**0.5
        distance_c = ((point[0] - class_c["c"][0][0])**2 + (point[1] - class_c["c"][0][1])**2)**0.5

        distance.append(distance_a)
        distance.append(distance_b)
        distance.append(distance_c)

        if min(distance) == distance_a:
            class_a["a"].append(point)
        elif min(distance) == distance_b:
            class_b["b"].append(point)
        elif min(distance) == distance_c:
            class_c["c"].append(point)

    return class_a,class_b,class_c


def delpoint(listofpoint,key):
    return {key: [listofpoint[key][0]]}


def kmeans(data_set):
    randomcenpoint = random.sample(data_set,3)

    class_a = {}
    class_b = {}
    class_c = {}

    class_a["a"] = [randomcenpoint[0]]
    class_b["b"] = [randomcenpoint[1]]
    class_c["c"] = [randomcenpoint[2]]

    class_aa = {}
    class_bb = {}
    class_cc = {}

    cenpoint_a = class_a["a"]
    cenpoint_b = class_b["b"]
    cenpoint_c = class_c["c"]

    cenpoint_aa = (0.0,0.0)
    cenpoint_bb = (0.0,0.0)
    cenpoint_cc = (0.0,0.0)

    while(cenpoint_a!=cenpoint_aa and cenpoint_b!=cenpoint_bb and cenpoint_b!=cenpoint_cc):
        cenpoint_aa = cenpoint_a
        cenpoint_bb = cenpoint_b
        cenpoint_cc = cenpoint_c

        class_a, class_b, class_c = cluster(data_set, class_a, class_b, class_c)

        cenpoint_a, class_a = calmeans(class_a, "a")
        cenpoint_b, class_b = calmeans(class_b, "b")
        cenpoint_c, class_c = calmeans(class_c, "c")

        class_aa = class_a
        class_bb = class_b
        class_cc = class_c

        class_a = delpoint(class_a, "a")
        class_b = delpoint(class_b, "b")
        class_c = delpoint(class_c, "c")
    print class_aa["a"][0]
    print class_bb["b"][0]
    print class_cc["c"][0]
    return class_aa,class_bb,class_cc

a,b,c = kmeans(data_set)

for i in a['a']:
    mp.plot(i[0],i[1],'or')
for i in b['b']:
    mp.plot(i[0],i[1],'ob')
for i in c['c']:
    mp.plot(i[0],i[1],'og')
mp.show()