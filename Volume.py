def cubeVolume():
    side = int(input("Enter the length of the side: "))
    volume = side * side * side
    volume = round(volume, 2)
    return volume


def ellipsoidVolume():
    # import math module in order for math.pi to function
    import math
    x = int(input("Enter radius x of ellipsoid: "))
    y = int(input("Enter radius y of ellipsoid: "))
    z = int(input("Enter radius z of ellipsoid: "))
    volume = (4 / 3) * math.pi * x * y * z
    volume = round(volume, 2)
    return volume
