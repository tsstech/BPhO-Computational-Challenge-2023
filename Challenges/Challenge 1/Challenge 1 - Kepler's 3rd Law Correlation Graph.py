import csv
import matplotlib.pyplot as plt

########## SELECTING DATA ##########
# variables to hold relevant rows
orbitalPeriod = []
semiMajorAxis = []

# opening CSV file
with open("Solar System Info.csv","r") as solarSystem:
    table = csv.DictReader(solarSystem, delimiter=",")

    # calculating values for each row
    for row in table:
        orbitalPeriod.append(round(float(row["Orbital Period/Years"]),0))
        semiMajorAxis.append(round(float(row["Distance from Sun in AU"])**1.5,0))


########## CREATING LINE GRAPH ########
plt.plot(orbitalPeriod, semiMajorAxis, color="blue", marker="o")

plt.xlabel("Semi-major Axis (AU^1.5)")
plt.ylabel("Orbital Period (yrs)")
plt.title("Kepler's 3rd Law")

plt.show()
