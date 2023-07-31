import csv
import matplotlib.pyplot as plt


############### TAKING DATA FROM CSV FILE ################

## open file in read mode
filename = open('planet_positions.csv', 'r')
 
## create dictreader object
file = csv.DictReader(filename)

## create lists to store data points for sun, mercury, venus & mars
##sunx = []
##suny = []
##merx = []
##mery = []
##venx = []
##veny = []
##marx = []
##mary = []
x = [[],[],[],[]]
y = [[],[],[],[]]


## iterate over each row and append values to empty list
for col in file:
    x[0].append(float(col["ï»¿Sun x"]))
    x[1].append(float(col["Mercury x"]))
    x[2].append(float(col["Venus x"]))
    x[3].append(float(col["Mars x"]))
    
    y[0].append(float(col["Sun y"]))
    y[1].append(float(col["Mercury y"]))
    y[2].append(float(col["Venus y"]))
    y[3].append(float(col["Mars y"]))


########## CALCULATING POSITIONS IN RELATION TO EARTH #########

## variables to store the positions of planets in relation to earth
diffx = [[],[],[],[]]
diffy = [[],[],[],[]]

## sun's relation to earth
diffx[0] = x[0]
diffy[0] = y[0]


## planet relations to earth
for i in range(1,4):
    for j in range(len(x[i])):
        diffx[i].append(x[0][j]-x[i][j])

    for k in range(len(y[i])):
        diffy[i].append(y[0][k]-y[i][k])


############ DRAWING THE GRAPH ###########
plt.plot(0, 0, color="blue", marker="o")
plt.plot(diffx[3], diffy[3], color="pink", marker=None)
plt.plot(diffx[2], diffy[2], color="grey", marker=None)
plt.plot(diffx[1], diffy[1], color="red", marker=None)
plt.plot(diffx[0], diffy[0], color="yellow", marker=None)


plt.xlabel("x/AU")
plt.ylabel("y/AU")
plt.title("Inner Solar System Relative to Earth")

plt.show()

