
def valid_date(date):
    if date=='':
        return False
    else:
        date=date.split("-")
        if len(date)!=3:
            return False
        else:
            if date[0] in ['01','03','05','07','08','10','12']:
                if int(date[1])>31 or int(date[1])<1:
                    return False
            elif date[0] in ['04','06','09','11']:
                if int(date[1])>30 or int(date[1])<1:
                    return False
            elif date[0]=='02':
                if int(date[1])>29 or int(date[1])<1:
                    return False
            elif int(date[1])>31 or int(date[1])<1 or int(date[0])>12 or int(date[0])<1:
                return False
            else:
                return True


