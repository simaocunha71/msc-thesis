    import re

    def file_name_check(file_name):
        match = re.fullmatch(r'[a-zA-Z][a-zA-Z0-9]{0,2}\.[\w]{3}', file_name)
        return 'Yes' if match else 'No'

