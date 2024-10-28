    int count = 0;
    int dot = 0;
    for(int i = 0; i < file_name.size(); i++){
        if(isdigit(file_name[i])) count++;
        if(file_name[i] == '.') dot++;
    }
    if(count > 3 || dot != 1) return "No";
    if(!isalpha(file_name[0])) return "No";
    string extension = file_name.substr(file_name.find('.') + 1);
    if(extension != "txt" && extension != "exe" && extension != "dll") return "No";
    return "Yes";
}

int main(){
    printf(file_name_check("example.txt").c_str());
    printf(file_name_check("1example.dll").c_str());
    return 0;
}

This program works by counting the number of digits and dots in the filename, then checks if the count of digits is greater than 3 or if there is not exactly one dot. If either of these conditions is true, it returns "No". It then checks if the first character is a letter. If it is not, it returns "No". Finally, it checks if the extension is one of the allowed extensions (txt, exe, dll). If it is not, it returns "No". If all of these conditions are met, it returns "Yes".

*/

// S:
/*
This solution works by counting the number of digits and dots in the filename, then checking if the count of digits is greater than 3 or if there is not exactly one dot. If either of these conditions is true, it immediately returns "No". It then checks if the first character is a letter. If it is not, it returns "No". Finally, it checks if the extension is one of the allowed extensions (txt, exe, dll). If it is not, it returns "No". If all of these conditions are met, it returns "Yes".
*/

// T:
/*
This solution has a time complexity of O(n), where n is the length of the filename. This is because it iterates over the filename once to count the digits and dots, and then again