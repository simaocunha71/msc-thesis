
def valid_date(date):
    if '-' not in date:
        return False
    date_split = date.split('-')
    if len(date_split) != 3:
        return False
    if date_split[0] not in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
        return False
    if len(date_split[1]) != 2 or len(date_split[2]) != 4:
        return False
    if date_split[1] == '02' and int(date_split[2]) % 4 == 0 and int(date_split[2]) % 100 != 0 and int(date_split[2]) % 400 == 0:
        if int(date_split[1]) < 1 or int(date_split[1]) > 29:
            return False
    elif int(date_split[1]) < 1 or int(date_split[1]) > 28:
        return False
    elif int(date_split[1]) < 1 or int(date_split[1]) > 31:
        return False
    return True

# def valid_date(date):
#     date_split = date.split('-')
#     if len(date_split) != 3:
#         return False
#     if date_split[0] not in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
#         return False
#     if len(date_split[1]) != 2 or len(date_split[2]) != 4:
#         return False
#     if date_split[1] == '02' and int(date_split[2]) % 4 == 0 and int(date_split[2]) % 100 != 0 and int(date_split[2]) % 400 ==