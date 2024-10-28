
def choose_num(x, y):
    if x > y:
        return -1
    else:
        for i in range(y, x-1, -1):
            if i % 2 == 0:
                return i
        return -1

print(choose_num(12, 15)) #14
print(choose_num(13, 12)) #-1
print(choose_num(3, 15)) #14
print(choose_num(16, 23)) #22
print(choose_num(24, 31)) #30
print(choose_num(32, 39)) #32
print(choose_num(40, 47)) #40
print(choose_num(48, 55)) #54
print(choose_num(56, 63)) #60
print(choose_num(64, 71)) #64
print(choose_num(72, 79)) #78
print(choose_num(80, 87)) #86
print(choose_num(88, 95)) #94
print(choose_num(96, 103)) #102
print(choose_num(104, 111)) #108
print(choose_num(112, 119)) #118
print(choose_num(120, 127)) #126
print(choose_num(128, 135)) #134
print(choose_num(136, 143)) #140
print(choose_num(144, 151)) #150
print(choose_num(152, 159)) #158
print(choose_num(160, 167)) #166
print(choose_num(168, 175)) #174
print(choose_num(18, 25)) #24
print(choose_num(26, 33))