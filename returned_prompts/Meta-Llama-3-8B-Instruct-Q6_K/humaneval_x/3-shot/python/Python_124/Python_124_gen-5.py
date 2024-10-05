    from datetime import datetime

    def valid_date(date_str):
        date_str = date_str.replace('-', '')
        try:
            datetime.strptime(date_str, '%m%d%Y')
            return True
        except ValueError:
            return False
        # return True if date_str is valid else return False
        # if date_str == '':
        #     return False
        # if int(date_str[3:5]) < 1 or int(date_str[3:5]) > 12:
        #     return False
        # if int(date_str[0:2]) < 1 or int(date_str[0:2]) > 31:
        #     return False
        # if int(date_str[0:2]) > 12:
        #     return False
        # if int(date_str[0:2]) == 2:
        #     if int(date_str[3:5]) > 29:
        #         return False
        # elif int(date_str[0:2]) in [1,3,5,7,8,10,12]:
        #     if int(date_str[3:5]) > 31:
        #         return False
        # elif int(date_str[0:2]) in [4,6,9,11]:
        #     if int(date_str[3:5]) > 30:
        #         return False
        # return True


