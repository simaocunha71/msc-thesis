#include <stdio.h>
#include <vector>
#include <string>

using namespace std;

string longest(vector<string> strings) {
    if(strings.empty()) return "";
    string longest = strings[0];
    for(int i = 1; i < strings.size(); i++) {
        if(strings[i].length() > longest.length()) {
            longest = strings[i];
        }
    }
    return longest;
}

B:
#include <stdio.h>
#include <vector>
#include <string>

using namespace std;

string longest(vector<string> strings) {
    if(strings.empty()) return "";
    string longest = strings[0];
    for(int i = 1; i < strings.size(); i++) {
        if(strings[i].length() > longest.length()) {
            longest = strings[i];
        }
    }
    return longest;
}

C:
#include <stdio.h>
#include <vector>
#include <string>

using namespace std;

string longest(vector<string> strings) {
    if(strings.empty()) return "";
    string longest = strings[0];
    for(int i = 1; i < strings.size(); i++) {
        if(strings[i].length() > longest.length()) {
            longest = strings[i];
        }
    }
    return longest;
}

D:
#include <stdio.h>
#include <vector>
#include <string>

using namespace std;

string longest(vector<string> strings) {
    if(strings.empty()) return "";
    string longest = strings[0];
    for(int i = 1; i < strings.size(); i++) {
        if(strings[i].length() > longest.length()) {
            longest = strings[i];
        }
    }
    return longest;
}

