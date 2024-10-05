    int count = 0;
    int dot_pos = -1;
    for(int i=0; file_name[i] != '\0'; i++){
        if(file_name[i] >= '0' && file_name[i] <= '9'){
            count++;
        }
        if(file_name[i] == '.'){
            dot_pos = i;
        }
    }
    if(count > 3 || dot_pos == -1){
        return "No";
    }
    if(!((file_name[0] >= 'a' && file_name[0] <= 'z') || (file_name[0] >= 'A' && file_name[0] <= 'Z'))){
        return "No";
    }
    string extension = file_name.substr(dot_pos + 1);
    if(extension != "txt" && extension != "exe" && extension != "dll"){
        return "No";
    }
    return "Yes";
}
int main(){
    string fn;
    printf("Enter file name: ");
    getline(cin, fn);
    cout<<file_name_check(fn)<<endl;
}

Explanation:
In this code, we first count the number of digits in the file name and check if there is a dot in the file name. If the count of digits is more than 3 or there is no dot in the file name, we return "No" immediately. 
Next, we check if the first character of the file name is a letter from the latin alphabet. If not, we return "No". 
Finally, we extract the substring after the dot and check if it is one of the required extensions ("txt", "exe", "dll"). If not, we return "No". If all the checks pass, we return "Yes", indicating that the file name is valid.
*/

/*
The function file_name_check() takes a string file_name as its argument, which represents the name of the file. This string is then analyzed to determine if it meets all the conditions specified in the problem statement.

The count variable is used to keep track of the number of digits in