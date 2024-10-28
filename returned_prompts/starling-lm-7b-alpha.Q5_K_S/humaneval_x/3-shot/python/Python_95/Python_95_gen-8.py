    def check_dict_case(dict):
        if not dict:
            return False
        for key in dict:
            if not isinstance(key, str) or not (key.isupper() == key.islower()):
                return False
        return True


