    import re

    def file_name_check(file_name: str) -> str:
        match = re.fullmatch(r'[a-zA-Z][a-zA-Z0-9]{0,2}\.txt|exe|dll', file_name)
        return 'Yes' if match else 'No'


