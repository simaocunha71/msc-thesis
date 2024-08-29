#include <iostream>
#include <vector>
#include <string>
using namespace std;
vector<string> all_prefixes(string str){
    vector<string> prefixes;
    for(int i = 0; i < str.length(); i++){
        prefixes.push_back(str.substr(0, i+1));
    }
    return prefixes;
}

C:
#include <iostream>
#include <vector>
#include <string>
using namespace std;
vector<string> all_prefixes(string str){
    vector<string> prefixes;
    string prefix = "";
    for(int i = 0; i < str.length(); i++){
        prefix += str[i];
        prefixes.push_back(prefix);
    }
    return prefixes;
}

D:
#include <iostream>
#include <vector>
#include <string>
using namespace std;
vector<string> all_prefixes(string str){
    vector<string> prefixes;
    for(int i = 0; i <= str.length(); i++){
        prefixes.push_back(str.substr(0, i));
    }
    return prefixes;
}

E:
#include <iostream>
#include <vector>
#include <string>
using namespace std;
vector<string> all_prefixes(string str){
    vector<string> prefixes;
    for(int i = 1; i <= str.length(); i++){
        prefixes.push_back(str.substr(0, i));
    }
    return prefixes;
}

F:
#include <iostream>
#include <vector>
#include <string>
using namespace std;
vector<string> all_prefixes(string str){
    vector<string> prefixes;
    for(int i = 1; i < str.length(); i++){
        prefixes.push_back(str.substr(0, i));
    }
    return prefixes;
}

G:
#include <iostream>
#include <vector>
#include <string>
using namespace std;
vector<string> all_prefixes(string str){
    vector<string> prefixes;
    for(int i = 0; i < str.length(); i++){
        prefixes.push_back(str.substr(i, 1));
    }
    return prefixes;
}

H:
#include <iostream>
#include <vector>
#include <string>
using namespace std;
vector<string> all_prefixes(string str){
    vector<string> prefixes;
    for(int i = 0; i < str.length(); i++){
        prefixes.push_back(str.substr(0, i+1));
    }
    return prefixes;
}

I:
#include <iostream>
#include <vector>
#include <string>
using namespace std;
vector<string> all_prefixes(string str){
    vector<string> prefixes;
    for(int i = 0; i