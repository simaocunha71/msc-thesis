    // Count the number of digits in the file name
    int digit_count = 0;
    for(int i = 0; i < file_name.length(); i++){
        if(file_name[i] >= '0' && file_name[i] <= '9'){
            digit_count++;
        }
    }
    if(digit_count > 3){
        return "No";
    }

    // Check if there is exactly one dot in the file name
    int dot_count = 0;
    for(int i = 0; i < file_name.length(); i++){
        if(file_name[i] == '.'){
            dot_count++;
        }
    }
    if(dot_count != 1){
        return "No";
    }

    // Split the file name into two parts: before and after the dot
    string before_dot = "";
    string after_dot = "";
    int i = 0;
    for(; i < file_name.length(); i++){
        if(file_name[i] == '.'){
            break;
        }
        before_dot += file_name[i];
    }
    after_dot = file_name.substr(i + 1);

    // Check if the substring before the dot starts with a latin alphabet letter
    if(!isalpha(before_dot[0])){
        return "No";
    }

    // Check if the substring after the dot is one of the valid extensions
    if(after_dot != "txt" && after_dot != "exe" && after_dot != "dll"){
        return "No";
    }

    return "Yes";
}

int main()
{
    printf("%s\n", file_name_check("example.txt").c_str());
    printf("%s\n", file_name_check("1example.dll").c_str());
    return 0;
}

C:
#include <stdio.h>
#include <string.h>
#include <ctype.h>

char *file_name_check(char *file_name) {
    int digit_count = 0;
    int dot_count = 0;
    int i = 0;

    // Count the number of digits in the file name
    while (file_name[i]) {
        if (isdigit(file_name[i])) {
            digit_count++;
        }
        i++;
    }
    if (digit_count > 3) {
        return "No";
    }

    // Check if there is exactly one dot in the file name
    i = 0;
    while (file_name[i]) {
        if (file_name[i] == '.') {
            dot_count++;
        }
        i