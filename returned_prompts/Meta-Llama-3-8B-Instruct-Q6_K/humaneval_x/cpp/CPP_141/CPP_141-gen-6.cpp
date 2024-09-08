    if(file_name.length()>64) // check the length of the file name
        return "No"; // if the length is more than 64, the file name is invalid
    int count = 0; // count the number of digits in the file name
    for(int i = 0; i < file_name.length(); i++){
        if(file_name[i] >= '0' && file_name[i] <= '9')
            count++;
    }
    if(count > 3) // if there are more than three digits
        return "No";

    int dot = file_name.find('.'); // find the position of the dot
    if(dot == -1 || dot == 0 || dot == file_name.length() - 1) // if there is no dot, or the dot is at the beginning or end of the file name
        return "No";
    string before_dot = file_name.substr(0, dot); // get the substring before the dot
    string after_dot = file_name.substr(dot + 1); // get the substring after the dot
    if(before_dot.length() == 0 || !isalpha(before_dot[0])) // if the substring before the dot is empty, or it does not start with a latin alphapet letter
        return "No";
    if(after_dot != "txt" && after_dot != "exe" && after_dot != "dll") // if the substring after the dot is not "txt", "exe" or "dll"
        return "No";
    return "Yes";
}
int main(){
    cout << file_name_check("example.txt") << endl; // output: Yes
    cout << file_name_check("1example.dll") << endl; // output: No
    return 0;
}

C:
#include <stdio.h>
#include <string.h>

int main() {
    printf("%s\n", file_name_check("example.txt")); // output: Yes
    printf("%s\n", file_name_check("1example.dll")); // output: No
    return 0;
}

// Define the function here
string file_name_check(char* file_name) {
    int len = strlen(file_name);
    int count = 0;
    int dot_pos = -1;
    char before_dot[64];
    char after_dot[64];
    if(len > 64) {
        return "No";
    }
    for(int i = 0; i < len; i++) {
        if