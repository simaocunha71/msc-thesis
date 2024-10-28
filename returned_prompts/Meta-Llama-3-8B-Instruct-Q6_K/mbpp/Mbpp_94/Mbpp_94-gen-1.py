def index_minimum(lst):
    return min(lst, key=lambda x: x[1])[0]

# Test case
print(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]))  # Expected output: 'Varsha'
print(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100), ('Rakesh', 150)]))  # Expected output: 'Varsha'
print(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100), ('Rakesh', 150), ('Raj', 180)]))  # Expected output: 'Varsha'
print(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100), ('Rakesh', 150), ('Raj', 180), ('Rahul', 140)]))  # Expected output: 'Varsha'  # Expected output: 'Varsha'
print(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100), ('Rakesh', 150), ('Raj', 180), ('Rahul', 140), ('Rahul', 120)]))  # Expected output: 'Varsha'  # Expected output: 'Varsha'
print(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100), ('Rakesh', 150), ('Raj', 180), ('Rahul', 140), ('Rahul', 120), ('Rahul', 130)]))  # Expected output: 'Varsha'  # Expected output: 'Varsha'
print(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100), ('Rakesh', 150), ('Raj', 180), ('Rahul', 140), ('Rahul', 120), ('Rahul', 130), ('Rahul', 110)]))  # Expected output: 'Varsha'
print(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100), ('Rakesh', 150), ('Raj', 180), ('Rahul', 140), ('Rahul',