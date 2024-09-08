import math
def area_tetrahedron(edge_length):
    # Calculate the area of each face using Heron's formula
    s1 = edge_length / 2
    area1 = math.sqrt(s1 * (s1 - edge_length) ** 3)
    
    s2 = (edge_length + math.sqrt(3) * edge_length) / 2
    area2 = math.sqrt(s2 * (s2 - edge_length) * (s2 - edge_length) * (s2 - math.sqrt(3) * edge_length))
    
    s3 = (edge_length + math.sqrt(3) * edge_length) / 2
    area3 = math.sqrt(s3 * (s3 - edge_length) * (s3 - edge_length) * (s3 - math.sqrt(3) * edge_length))
    
    s4 = edge_length / 2
    area4 = math.sqrt(s4 * (s4 - edge_length) ** 3)
    
    # Sum up the areas of the four faces
    total_area = area1 + area2 + area3 + area4
    
    return total_area