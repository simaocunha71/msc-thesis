    def is_valid_name(name: str) -> bool:
        if len(name) < 2 or len(name) > 255:
            return False
        if name.count('.') != 1:
            return False
        if not name[name.index('.'):].lower() in ['txt', 'exe', 'dll']:
            return False
        if not name[:name.index('.')].isalnum():
            return False
        if name.count('0') + name.count('1') + name.count('2') + name.count('3') + name.count('4') + name.count('5') + name.count('6') + name.count('7') + name.count('8') + name.count('9') > 3:
            return False
        return True

    if is_valid_name(file_name):
        return 'Yes'
    else:
        return 'No'  # or raise an exception


