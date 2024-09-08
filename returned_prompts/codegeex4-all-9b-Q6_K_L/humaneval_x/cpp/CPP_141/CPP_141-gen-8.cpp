#include<stdio.h>
#include<string>
using namespace std;
string file_name_check(string file_name){
    string ans="No";
    int dot=0;
    int digit=0;
    if(file_name[0]>='A'&&file_name[0]<='Z'||file_name[0]>='a'&&file_name[0]<='z'){
        for(int i=0;i<file_name.length();i++){
            if(file_name[i]=='.'){
                dot++;
            }
            else if(file_name[i]>='0'&&file_name[i]<='9'){
                digit++;
            }
            else if(file_name[i]>'z'||file_name[i]<'a'&&file_name[i]>'Z'||file_name[i]<'A'){
                return "No";
            }
        }
        if(dot==1&&digit<=3&&file_name[file_name.length()-1]=='t'&&file_name[file_name.length()-2]=='x'&&file_name[file_name.length()-3]=='.'){
            ans="Yes";
        }
        if(dot==1&&digit<=3&&file_name[file_name.length()-1]=='e'&&file_name[file_name.length()-2]=='x'&&file_name[file_name.length()-3]=='.'){
            ans="Yes";
        }
        if(dot==1&&digit<=3&&file_name[file_name.length()-1]=='l'&&file_name[file_name.length()-2]=='l'&&file_name[file_name.length()-3]=='.'){
            ans="Yes";
        }
    }
    return ans;
}