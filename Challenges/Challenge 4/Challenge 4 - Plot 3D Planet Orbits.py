from Challenge_4_Classes import SolarSystem, Sun, Planet

## create solar system's basic graph
solar_system = SolarSystem(400)

## create sun
sun = Sun(solar_system)

## create planets
planets = (
    ## planet 1
    Planet(
        solar_system,
        mass = 10,
        position=(150, 50, 0),
        velocity=(0, 5, 5),
    ),
    ## planet 2
    Planet(
        solar_system,
        mass=20,
        position=(100, -50, 150),
        velocity=(5, 0, 0)
    )
)

## loop for solar system simulation
while True:
    solar_system.calculate_all_body_interactions()
    solar_system.update_all()
    solar_system.draw_all()
