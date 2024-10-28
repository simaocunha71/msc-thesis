function fileNameCheck(file_name) {
    if (file_name.length > 3) {
        return 'No';
    }
    let dot_index = file_name.indexOf('.');
    if (dot_index < 0) {
        return 'No';
    }
    if (file_name[dot_index - 1] === '.') {
        return 'No';
    }
    let first_part = file_name.slice(0, dot_index);
    if (!/[a-zA-Z]/.test(first_part)) {
        return 'No';
    }
    let second_part = file_name.slice(dot_index + 1);
    let valid_suffixes = ['txt', 'exe', 'dll'];
    if (!valid_suffixes.includes(second_part)) {
        return 'No';
    }
    return 'Yes';
}

    let result = fileNameCheck(file_name);
    return result;
}


/*
    The function takes a file's name as an input, and returns 'Yes' if the file's name is valid
    and 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    fileNameCheck("example.txt") # => 'Yes'
    fileNameCheck("1example.dll") # => 'No' (the name should start with a latin alphapet letter)

    In order to solve this problem, we need to define a function called fileNameCheck that takes a file's name as an argument and returns a boolean value depending on whether the name is valid or not.

    First, we check if there are