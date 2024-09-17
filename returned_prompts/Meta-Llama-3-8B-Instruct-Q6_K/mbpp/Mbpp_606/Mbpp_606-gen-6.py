def radian_degree(angle_degree):
    return angle_degree * (3.14159265359/180)  # 3.14159265359 is pi
# Test
print(radian_degree(90))  # Expected output: 1.5707963267948966
print(radian_degree(180))  # Expected output: 3.14159265359
print(radian_degree(270))  # Expected output: 4.71238898038469
print(radian_degree(360))  # Expected output: 6.283185307179586
# Test cases
assert radian_degree(90) == 1.5707963267948966
assert radian_degree(180) == 3.14159265359
assert radian_degree(270) == 4.71238898038469
assert radian_degree(360) == 6.283185307179586
# Test cases
assert radian_degree(-90) == -1.5707963267948966
assert radian_degree(-180) == -3.14159265359
assert radian_degree(-270) == -4.71238898038469
assert radian_degree(-360) == -6.283185307179586
print(radian_degree(0))
# Expected output: 0.0
print(radian_degree(-180))
# Expected output: -3.14159265359
print(radian_degree(90))
# Expected output: 1.5707963267948966
print(radian_degree(0))
# Expected output: 0.0
print(radian_degree(-360))
# Expected output: -6.283185307179586
print(radian_degree(-90))
# Expected output: -1.5707963267948966
print(radian_degree(270))
# Expected output: 4.71238898038469
print(radian_degree(-270))
# Expected output: -4.71238898038469
print(radian_degree(360))
# Expected output: 6.283185307179586
print(radian_degree(-360))
# Expected output: -6.283185307179586
print(radian_degree(-90))
# Expected output: -1.5707963267948966
print(radian_degree(90))
# Expected output: 1.5707963267948966
print(radian_degree(0))
# Expected output: 