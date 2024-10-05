    vector<string> v;
    vector<string> v1;
    map<string,string> m;
    map<string,string>::iterator it;
    for(int i = 0;i < lst.size();i++){
        int c = 0;
        for(int j = 0;j < lst[i].size();j++){
            if((lst[i][j] - '0') % 2 == 1)c++;
        }
        string s = "the number of odd elements ";
        string s1 = "";
        for(int j = 0;j < lst[i].size();j++) s1 += lst[i][j];
        s += to_string(c);
        s += " in the ";
        for(int j = 0;j < lst[i].size();j++) s += lst[i][j];
        s += " of the ";
        for(int j = 0;j < lst[i].size();j++) s += lst[i][j];
        s += ".";
        v1.push_back(s);
        m.insert(pair<string,string>(s1,s));
    }
    for(it = m.begin();it != m.end();it++) v.push_back(it->second);
    return v;
}
int main(){
    vector<string> lst;
    lst.push_back("1234567");
    lst.push_back("3");
    lst.push_back("11111111");
    vector<string> v = odd_count(lst);
    for(int i = 0;i < v.size();i++) printf("%s\n",v[i].c_str());
    return 0;
}

*/

#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

vector<string> odd_count(vector<string> lst) {
    map<string, string> m;
    for (string s : lst) {
        int c = 0