
def get_coordinates(coordinates):
    return [(coordinates[0], i) for i in range(coordinates[1]-1, coordinates[1]+2)] + [(i, coordinates[1]) for i in range(coordinates[0]-1, coordinates[0]+2)]


