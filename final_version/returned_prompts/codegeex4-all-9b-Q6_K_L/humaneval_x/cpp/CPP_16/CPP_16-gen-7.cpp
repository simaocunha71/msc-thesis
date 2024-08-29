#include <bits/stdc++.h>
using namespace std;

int count_distinct_characters(string str){
    set<char> s(str.begin(),str.end());
    return s.size();
}

int main() {
    cout << count_distinct_characters("Jerry") << endl;
    return 0;
}