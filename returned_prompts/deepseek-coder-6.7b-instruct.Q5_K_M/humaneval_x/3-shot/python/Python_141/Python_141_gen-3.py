    import re

    def file_name_check(file_name):
        if not re.match("^[A-Za-z][A-Za-z0-9]{0,2}\.([tT][xX][tT])|([eE][xX][eE])|([dD][lL][lL])$", file_name):
            return 'No'
        return 'Yes'


