def division_elements(t1,t2):
    result = []
    for i in range(len(t1)):
        result.append(t1[i]/t2[i])
    return result

# assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)

print(division_elements((10, 4, 6, 9),(5, 2, 3, 3)))




"""
def division_elements(t1,t2):
    result = []
    for i in range(len(t1)):
        result.append(t1[i]/t2[i])
    return result

# assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)

print(division_elements