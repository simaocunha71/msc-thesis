    int count = 0;
    int dot_index = -1;
    for(int i = 0; i < file_name.length(); i++){
        if(file_name[i] >= '0' && file_name[i] <= '9'){
            count++;
        }
        if(file_name[i] == '.'){
            dot_index = i;
        }
    }
    if(count > 3 || dot_index == -1 || dot_index == 0 || dot_index == file_name.length()-1){
        return "No";
    }
    string pre_dot = file_name.substr(0, dot_index);
    string post_dot = file_name.substr(dot_index+1, file_name.length()-dot_index-1);
    if(pre_dot[0] < 'a' || pre_dot[0] > 'z' && pre_dot[0] < 'A' || pre_dot[0] > 'Z'){
        return "No";
    }
    if(post_dot != "txt" && post_dot != "exe" && post_dot != "dll"){
        return "No";
    }
    return "Yes";
}
int main(){
    string file_name = "example.txt";
    cout << file_name_check(file_name) << endl;
    return 0;
}
```

B:
The solution is to create a function `file_name_check` that takes a string representing a file's name, and returns "Yes" if the file's name is valid, and returns "No" otherwise. A file's name is considered to be valid if and only if all the following conditions are met:

1.  There should not be more than three digits ('0'-'9') in the file's name.
2.  The file's name contains exactly one dot (".")
3.  The substring before the dot should not be empty, and it starts with a letter from the latin alphabet ('a'-'z' and 'A'-'Z').
4.  The substring after the dot should be one of these: {"txt", "exe", "dll"}

Here is the solution:
```c
#include <iostream>
#include <string>

using namespace std;

string file_name_check(string file_name) {
    int count = 0;
    int dot_index = -1;
    for (int i = 0; i < file_name.length(); i++) {
        if (file_name[i] >= '0' && file_name[i] <= '9') {
            count++;
        }
        if (file