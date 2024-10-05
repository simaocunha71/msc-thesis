     int i = 0, j = 0, count = 0;
     string valid_ext[] = {"txt", "exe", "dll"};
     string valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
     for (i = 0; i < file_name.size(); i++){
         if (isdigit(file_name[i])){
             count++;
         }
         if (file_name[i] == '.'){
             j = i;
         }
     }
     if (count > 3 || j == 0 || (file_name.substr(j+1) != valid_ext[0] && file_name.substr(j+1) != valid_ext[1] && file_name.substr(j+1) != valid_ext[2])){
         return "No";
     }
     if (valid_chars.find(file_name[0]) == string::npos){
         return "No";
     }
     return "Yes";
}

*/
#include <stdio.h>
#include <string.h>
#include <ctype.h>

char* file_name_check(char* file_name) {
    int i = 0, j = 0, count = 0;
    char* valid_ext[] = {"txt", "exe", "dll"};
    char valid_chars[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    for (i = 0; i < strlen(file_name); i++){
        if (isdigit(file_name[i])){
            count++;
        }
        if (file_name[i] == '.'){
            j = i;
        }
    }
    if (count > 3 || j == 0 || (strcmp(file_name+j+1, valid_ext[0]) != 0 && strcmp(file_name+j+1, valid_ext[1]) != 0