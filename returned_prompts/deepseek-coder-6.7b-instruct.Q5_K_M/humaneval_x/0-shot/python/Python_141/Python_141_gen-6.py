
    import re

    def file_name_check(file_name):
        if len(file_name) < 5:
            return 'No'
        if file_name.count('.') != 1:
            return 'No'
        if not re.match("^[a-zA-Z][a-zA-Z0-9]*\.txt$", file_name) and not re.match("^[a-zA-Z][a-zA-Z0-9]*\.exe$", file_name) and not re.match("^[a-zA-Z][a-zA-Z0-9]*\.dll$", file_name):
            return 'No'
        if re.search(r'\d{4,}', file_name):
            return 'No'
        return 'Yes'

print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("1example.dll"))  # => 'No'
print(file_name_check("ex.ample.txt"))  # => 'No'
print(file_name_check("example.exe"))  # => 'Yes'
print(file_name_check("exam23ple.exe"))  # => 'No'
print(file_name_check("exam23ple.dll"))  # => 'Yes'
print(file_name_check("exam2345ple.dll"))  # => 'No'
print(file_name_check(".txt"))  # => 'No'
print(file_name_check("example"))  # => 'No'
print(file_name_check("example."))  # => 'No'
print(file_name_check("exa.mple.txt"))  # => 'No'
print(file_name_check("exa.mple.exe"))  # => 'No'
print(file_name_check("exa.mple.dll"))  # => 'No'
print(file_name_check("exa123.mple.dll"))  # => 'No'
print(file_name_check("e.