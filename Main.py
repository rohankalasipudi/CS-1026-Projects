# Import Volume module
from Volume import cubeVolume, ellipsoidVolume

cube = []
ellipsoid = []
shape = ""

# While loop for input
while shape != "quit":
  shape = input("Enter the shape: ")
  shape = shape.lower()

  if shape == "cube" or shape == "c":
    vol = cubeVolume()
    cube.append(vol)

  elif shape == "ellipsoid" or shape == "e":
    vol = ellipsoidVolume()
    ellipsoid.append(vol)

  elif shape == "quit:" or shape == "q":
    break

  else:
   print("Invalid input")
print("You have reached the end of your session. The volumes calculated for each shape are: ")

# Code for conditional that no input has been entered for either shape
if len(cube) == 0 and len(ellipsoid) == 0:
    print("You did not perform any volume calculations")

else:
    if len(cube) > 0:
        print("Cube:" ,sum(cube), ',',max(cube), ',',min(cube))
    else:
        print("Cube: No shapes entered")

    if len(ellipsoid) > 0:
        print("Ellipsoid:" ,sum(ellipsoid), ',',max(ellipsoid), ',',min(ellipsoid))
    else:
        print("Ellipsoid: No shapes entered")
