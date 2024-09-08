vector<string> all_prefixes(string str){
    vector<string> all_prefixes;
    for(int i=0;i<str.length();i++){
        all_prefixes.push_back(str.substr(0,i+1));
    }
    return all_prefixes;
}

C:
#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> all_prefixes(const string& str){
    vector<string> prefixes;
    for (int i = 0; i <= str.size(); i++) {
        prefixes.push_back(str.substr(0, i));
    }
    return prefixes;
}

int main() {
    vector<string> result = all_prefixes("abc");
    for (const string& prefix : result) {
        cout << prefix << endl;
    }
    return 0;
}

D:
#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> all_prefixes(const string& str){
    vector<string> prefixes;
    for (int i = 1; i <= str.size(); i++) {
        prefixes.push_back(str.substr(0, i));
    }
    return prefixes;
}

int main() {
    vector<string> result = all_prefixes("abc");
    for (const string& prefix : result) {
        cout << prefix << endl;
    }
    return 0;
}

E:
#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> all_prefixes(const string& str){
    vector<string> prefixes;
    for (int i = 0; i < str.size(); i++) {
        prefixes.push_back(str.substr(i, str.size()));
    }
    return prefixes;
}

int main() {
    vector<string> result = all_prefixes("abc");
    for (const string& prefix : result) {
        cout << prefix << endl;
    }
    return 0;
}

F:
#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> all_prefixes(const string& str){
    vector<string> prefixes;
    for (int i = 0; i < str.size(); i++) {
        prefixes.push_back(str.substr(i, str.size() - i));
    }
    return prefixes;
}

int main() {
    vector<string> result = all_prefixes("abc");
    for (const string& prefix : result) {
        cout << prefix << endl;
    }
    return 0;
}

G:
#include <iostream>
#include <