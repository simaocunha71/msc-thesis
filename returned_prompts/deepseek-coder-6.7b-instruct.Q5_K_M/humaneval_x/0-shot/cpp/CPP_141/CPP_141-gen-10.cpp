    int i = 0, count = 0;
    while(file_name[i]){
        if(file_name[i] >= '0' && file_name[i] <= '9')
            count++;
        i++;
    }
    if(count > 3)
        return "No";
    i = 0;
    int dot = 0, alpha = 0;
    while(file_name[i]){
        if(file_name[i] == '.')
            dot++;
        if((file_name[i] >= 'a' && file_name[i] <= 'z') || (file_name[i] >= 'A' && file_name[i] <= 'Z'))
            alpha++;
        i++;
    }
    if(dot != 1 || alpha == 0)
        return "No";
    string ext = file_name.substr(file_name.find_last_of(".") + 1);
    if(ext != "txt" && ext != "exe" && ext != "dll")
        return "No";
    return "Yes";
}
int main() {
   printf("%s", file_name_check("example.txt").c_str());
   printf("%s", file_name_check("1example.dll").c_str());
   return 0;
}
*/

// Code: Ends

// Code: Starts
// 
// 