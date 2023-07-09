import math
import matplotlib.pyplot as plt

########## CLASS FOR VECTORS ####### 
class Vector:
    ## initialiser
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"

    ## indexing vector
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        else:
            raise IndexError("There are only three elements in the vector")

    ## adding to the vector
    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )

    ## subtracting from the vector
    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
        )

    ## multiplying with the vector
    def __mul__(self, other):
        if isinstance(other, Vector):  # Vector dot product
            return (
                self.x * other.x
                + self.y * other.y
                + self.z * other.z
            )
        elif isinstance(other, (int, float)):  # Scalar multiplication
            return Vector(
                self.x * other,
                self.y * other,
                self.z * other,
            )
        else:
            raise TypeError("operand must be Vector, int, or float")

    ## dividing with vector
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(
                self.x / other,
                self.y / other,
                self.z / other,
            )
        else:
            raise TypeError("operand must be int or float")
        
    def get_magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalize(self):
        magnitude = self.get_magnitude()
        return Vector(
            self.x / magnitude,
            self.y / magnitude,
            self.z / magnitude,
        )


######### CLASS FOR OVERALL SOLAR SYSTEM #########
class SolarSystem:
    def __init__(self, size):
        self.size = size
        self.bodies = []

        ## Create a figure and set of axes with matplotlib
        self.fig, self.axes = plt.subplots(
            1,
            1,
            subplot_kw={"projection": "3d"},        ## 3D projection
            figsize=(self.size / 50, self.size / 50),   ## overall figure size
        )
        self.fig.tight_layout() ## reduce margins at edge of figure
         
    ## adds a body to the solar system
    def add_body(self, body):
        self.bodies.append(body)

    ## moves and draws each body
    def update_all(self):
        for body in self.bodies:
            body.move()
            body.draw()

    ## updates graph and clears axes for next plot
    def draw_all(self):
        self.axes.set_xlim((-self.size / 2, self.size / 2))
        self.axes.set_ylim((-self.size / 2, self.size / 2))
        self.axes.set_zlim((-self.size / 2, self.size / 2))
        plt.pause(0.001)
        self.axes.clear()



###### CLASS FOR INDIVIDUAL BODIES #######
class SolarSystemBody:
    min_display_size = 10
    display_log_base = 1.3
    
    def __init__(self, solar_system, mass, position=(0, 0, 0), velocity=(0, 0, 0)):
        self.mass = mass    ## mass of body in arbitrary units
        self.position = position  ## a tuple with x,y,z co-ordinates
        self.velocity = Vector(*velocity)   ## a vector with velocity of body
        
        self.solar_system = solar_system ## lets body connect to solar system graph
        self.solar_system.add_body(self) ## add body to the solar system

        ## setting default pen size & color for drawing body
        self.display_size = max(
            math.log(self.mass, self.display_log_base),
            self.min_display_size,
        )
        self.colour = "black"

    ## move body based on its velocity
    def move(self):
        self.position = (
            self.position[0] + self.velocity[0],
            self.position[1] + self.velocity[1],
            self.position[2] + self.velocity[2],
        )

    ## draw body onto 3D graph
    def draw(self):
        self.solar_system.axes.plot(
            *self.position,
            marker="o",
            markersize=self.display_size,
            color=self.colour
        )



solar_system = SolarSystem(400)
body = SolarSystemBody(solar_system, 100, velocity=(5, 5, 5))
for _ in range(100):
    solar_system.update_all()
    solar_system.draw_all()
