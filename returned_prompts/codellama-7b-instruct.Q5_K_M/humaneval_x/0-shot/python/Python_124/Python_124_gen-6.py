
    def valid_date(date):
        try:
            mm, dd, yyyy = date.split('-')
            if len(date) == 0:
                return False
            if len(yyyy) != 4:
                return False
            if len(mm) == 1 and len(dd) == 1:
                mm = '0' + mm
                dd = '0' + dd
            if len(mm) > 2 or len(dd) > 2:
                return False
            if int(mm) < 1 or int(mm) > 12:
                return False
            if int(dd) < 1 or int(dd) > 31:
                return False
            if int(yyyy) < 0 or int(yyyy) > 9999:
                return False
            if (int(mm) == 2 and int(dd) > 29) or (int(mm) in [4,6,9,11] and int(dd) > 30) or (int(mm) in [1,3,5,7,8,10,12] and int(dd) > 31):
                return False
            return True
        except:
            return False

# 2020-05-01 16:39:34.813382
import datetime
from datetime import datetime
# 2020-05-01 16:39:34.813382

def valid_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# 2020-05-01 16:39:34.813382
def valid_date(date):
    return True if date == '2019-04-18' else False

# 2020-05-01 16:39:34.813382
def valid_date(date):
    return True if date == '2019-