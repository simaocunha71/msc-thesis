def check_monthnumb_number(month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return True
    else:
        return False

#Testing
print(check_monthnumb_number(5)) #Expected output: True

