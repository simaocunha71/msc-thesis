#include <iostream>
#include <vector>
#include <string>
using namespace std;

string longest(vector<string> strings){
    string longest = "";
    for(string s : strings){
        if(s.size() > longest.size()){
            longest = s;
        }
    }
    return longest;
}
B:
#include <iostream>
#include <vector>
#include <string>
using namespace std;

string longest(vector<string> strings){
    if(strings.size() == 0) return "";
    string longest = strings[0];
    for(int i = 1; i < strings.size(); i++){
        if(strings[i].size() > longest.size()){
            longest = strings[i];
        }
    }
    return longest;
}
C:
#include <iostream>
#include <vector>
#include <string>
using namespace std;

string longest(vector<string> strings){
    if(strings.size() == 0) return "";
    string longest = strings[0];
    for(int i = 0; i < strings.size(); i++){
        if(strings[i].size() > longest.size()){
            longest = strings[i];
        }
    }
    return longest;
}
D:
#include <iostream>
#include <vector>
#include <string>
using namespace std;

string longest(vector<string> strings){
    if(strings.size() == 0) return "";
    string longest = strings[0];
    for(int i = 0; i < strings.size() - 1; i++){
        if(strings[i].size() > longest.size()){
            longest = strings[i];
        }
    }
    return longest;
}

E:
#include <iostream>
#include <vector>
#include <string>
using namespace std;

string longest(vector<string> strings){
    if(strings.size() == 0) return "";
    string longest = strings[0];
    for(int i = 1; i < strings.size() - 1; i++){
        if(strings[i].size() > longest.size()){
            longest = strings[i];
        }
    }
    return longest;
}

F:
#include <iostream>
#include <vector>
#include <string>
using namespace std;

string longest(vector<string> strings){
    if(strings.size() == 0) return "";
    string longest = strings[0];
    for(int i = 0; i < strings.size(); i++){
        if(strings[i].size() > longest.size()){
            longest = strings[i];
        }
    }
    return longest;
}

G:
#include <iostream>
#include <vector>
#include <string>
using namespace std;

string longest(vector