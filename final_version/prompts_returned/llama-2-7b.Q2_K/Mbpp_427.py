"""
Write a function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
assert change_date_format("2026-01-02") == '02-01-2026'
"""

def change_date_format(date: str) -> str:
    date_list = []
    for i in range(0, 3):
        if ord(date[i]) < 58 and ord(date[i]) > 47:
            date_list.append("0" + str(ord(date[i]) - 1))
        else:
            date_list.append(str(ord(date[i])))
    
    return "".join(date_list)
