    vector<string> result;
    map<int, int> m;
    for(int i=0; i<lst.size(); i++){
        string s = lst[i];
        int count = 0;
        for(int j=0; j<s.length(); j++){
            if((s[j] - '0') % 2 != 0)
                count++;
        }
        m[i] = count;
    }
    for(int i=0; i<lst.size(); i++){
        string s = "the number of odd elements in the string i of the input.";
        while(s.find('i') != string::npos)
            s.replace(s.find('i'), 1, to_string(m[i]));
        result.push_back(s);
    }
    return result;
}

*/

#include<bits/stdc++.h>
using namespace std;

vector<string> odd_count(vector<string> lst){
    vector<string> result;
    for(auto &s : lst){
        int count = 0;
        for(auto &c : s)
            if((c - '0') % 2 != 0)
                count++;
        string r = "the number of odd elements in the string " 
                    + to_string(count) + " of the input.";
        result.push_back(r);
    }
    return result;
}

int main(){
    vector<string> v = {"3","11111111"};
    vector<string> res = odd_count(v);
    for(auto &s : res)
        cout<< s <<endl;
    return 0;
}

Output:
the number of odd elements in the string 1 of the input.
the number of odd elements in the string 8 of the input.
*/

In this solution, we iterate over each string in the input list. For each string, we count the number of odd digits and store this count in a map. Then we create a new string for each input string, replacing 'i'