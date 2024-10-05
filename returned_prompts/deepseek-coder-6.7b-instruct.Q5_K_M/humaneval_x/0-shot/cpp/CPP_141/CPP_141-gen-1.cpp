// Checking if there are more than 3 digits in the file's name.
    for(int i=0; i<file_name.size(); i++)
    {
        if(isdigit(file_name[i])){
            int count=0;
            while(isdigit(file_name[i])){
                i++;
                count++;
                if(count>3)
                    return "No";
            }
        }
    }

// Checking if there is exactly one dot in the file's name.
    int dot_count=0;
    for(int i=0; i<file_name.size(); i++)
    {
        if(file_name[i]=='.')
            dot_count++;
    }
    if(dot_count==0 || dot_count>1)
        return "No";

// Checking if the file's name starts with a letter from latin alphapet.
    if(!isalpha(file_name[0]))
        return "No";

// Checking if the substring after the dot is one of these: {"txt", "exe", "dll"}.
    string extn = file_name.substr(file_name.find_last_of(".") + 1);
    if(extn != "txt" && extn != "exe" && extn != "dll")
        return "No";

    return "Yes";
}

int main()
{
    cout<<file_name_check("example.txt")<<endl;
    cout<<file_name_check("1example.dll")<<endl;
    return 0;
}

*/

//Exercise_3/main.cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include "file_name_check.h"

using namespace std;

int main() {
    vector<string> files = {"example.txt", "1example.dll", "exam2ple.exe", "ex4mple.dll"};
    int valid_count = 0;
