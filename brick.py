import math
from cadquery import func as cf


# Function to create a 2 x 4 toy brick
def clutch_brick(length, width, height, stud_d, stud_h, spacing):

    # Create the main rectangular body
    body = cf.box(length, width, height)

    # Create one cylindrical stud
    stud = cf.cylinder(d=stud_d, h=stud_h)

    # Repeat the stud in 4 columns and 2 rows
    for i in range(4):
        for j in range(2):

            # Calculate stud positions
            x = (i - 1.5) * spacing
            y = (j - 0.5) * spacing

            # Move stud to its position
            new_stud = stud.moved(x=x, y=y, z=height)

            # Join stud with the brick body
            body = body + new_stud

    return body


# Create the 2 x 4 brick
brick = clutch_brick(31.2, 15.6, 9.6, 4.8, 1.7, 8.0)


# Calculate expected volume
expected = (
    31.2 * 15.6 * 9.6
    + 8 * math.pi * (4.8 / 2) ** 2 * 1.7
)


# Display results
print("Valid:", brick.isValid())
print("Actual Volume:", round(brick.Volume(), 2))
print("Expected Volume:", round(expected, 2))


# Verify the volume
assert abs(brick.Volume() - expected) < 0.5


# Export the model
brick.exportStl("brick.stl")