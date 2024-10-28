if(txt.length()==0)
return false;

for(int i=0; i<txt.length(); i++){
if(txt.at(i)==txt.at(txt.length()-1) && (i==txt.length()-1 || txt.at(i+1)!=' ')){
return true;
}
}
return false;
}

//B:

#include<stdio.h>
#include<string>
#include<cctype>
using namespace std;

bool check_if_last_char_is_a_letter(string txt) {
    if (txt.empty())
        return false;
    for (int i = 0; i < txt.size(); i++) {
        if (isalpha(txt.at(i)) && (i == txt.size() - 1 || txt.at(i + 1) != ' '))
            return true;
    }
    return false;
}

//C:

#include<stdio.h>
#include<string>
#include<cctype>
using namespace std;

bool check_if_last_char_is_a_letter(string txt) {
    if (txt.empty())
        return false;
    for (int i = 0; i < txt.size(); i++) {
        if (isalpha(txt.at(i)) && (i == txt.size() - 1 || txt.at(i + 1) != ' '))
            return true;
    }
    return false;
}

//D:

#include<stdio.h>
#include<string>
#include<cctype>
using namespace std;

bool check_if_last_char_is_a_letter(string txt) {
    if (txt.empty())
        return false;
    for (int i = 0; i < txt.size(); i++) {
        if (isalpha(txt.at(i)) && (i == txt.size() - 1 || txt.at(i + 1) != ' '))
            return true;
    }
    return false;
}

//E:

#