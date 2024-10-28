    int count_digit = 0;
    int count_dot = 0;
    int length = file_name.length();

    for(int i = 0; i < length; i++){
        if(isdigit(file_name[i])){
            count_digit++;
        }
        if(file_name[i] == '.'){
            count_dot++;
        }
    }

    if(count_digit > 3 || count_dot != 1 || !isalpha(file_name[0])){
        return "No";
    }

    string extension = file_name.substr(file_name.find_last_of(".") + 1);

    if(extension != "txt" && extension != "exe" && extension != "dll"){
        return "No";
    }

    return "Yes";
}

int main(){
    printf("%s\n", file_name_check("example.txt").c_str()); //Yes
    printf("%s\n", file_name_check("1example.dll").c_str()); //No
    return 0;
}
```

The function `file_name_check` takes a string `file_name` as argument. It first checks if the filename contains more than 3 digits or if it doesn't have exactly one dot. If either of these conditions is true, it returns "No". Then it checks if the first character of the filename is a letter. If not, it returns "No". Finally, it gets the file extension and checks if it's either "txt", "exe", or "dll". If it's not, it returns "No". If all the conditions are met, it returns "Yes".

The main function calls `file_name_check` with two test cases and prints the result.

This solution assumes that the file name is a valid C++ string.

In C++, the `isdigit` function is used to check if a character is a digit, `isalpha` function is used to check if a character is a letter and `find_last_of` function is used to find the last occurrence of a character in a string.

In C++, the `