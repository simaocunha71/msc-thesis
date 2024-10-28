    int count = 0, dot_position = -1;
    for(int i=0; i<file_name.length(); i++){
        if(file_name[i] >= '0' && file_name[i] <= '9'){
            count++;
        }
        if(file_name[i] == '.'){
            dot_position = i;
        }
    }
    if(count > 3 || dot_position == -1 || !(file_name[0] >= 'a' && file_name[0] <= 'z' || file_name[0] >= 'A' && file_name[0] <= 'Z') || dot_position == 0)
        return "No";
    string ext = file_name.substr(dot_position + 1);
    if(ext != "txt" && ext != "exe" && ext != "dll"){
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

*/

*/






















































































































































































































