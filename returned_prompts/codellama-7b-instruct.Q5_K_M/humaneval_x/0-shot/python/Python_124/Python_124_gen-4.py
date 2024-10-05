
import re
def valid_date(date):
    if date == '':
        return False
    elif re.match('^[0-9]{2}-[0-9]{2}-[0-9]{4}$', date) == None:
        return False
    else:
        months = ['01','03','05','07','08','10','12']
        for month in months:
            if date[:2] == month:
                if int(date[3:]) < 1 or int(date[3:]) > 31:
                    return False
        months = ['04','06','09','11']
        for month in months:
            if date[:2] == month:
                if int(date[3:]) < 1 or int(date[3:]) > 30:
                    return False
        if date[:2] == '02':
            if int(date[3:]) < 1 or int(date[3:]) > 29:
                return False
        months = ['01','02','03','04','05','06','07','08','09','10','11','12']
        if date[:2] not in months:
            return False
        return True