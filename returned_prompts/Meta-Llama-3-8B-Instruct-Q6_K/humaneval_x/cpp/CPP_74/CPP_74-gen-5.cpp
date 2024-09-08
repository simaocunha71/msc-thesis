    int count1 = 0;
    int count2 = 0;
    for(auto str : lst1){
        count1 += str.length();
    }
    for(auto str : lst2){
        count2 += str.length();
    }

    if(count1 < count2){
        return lst1;
    }else if(count1 > count2){
        return lst2;
    }else{
        return lst1;
    }
}
int main(){
    vector<string> v1 = {"hi", "admin"};
    vector<string> v2 = {"hI", "Hi"};
    vector<string> result = total_match(v1,v2);
    for(auto str : result){
        cout<<str<<" ";
    }
    return 0;
}
B:
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<string> total_match(vector<string> lst1, vector<string> lst2) {
    int count1 = 0, count2 = 0;
    for (const auto& str : lst1) {
        count1 += str.length();
    }
    for (const auto& str : lst2) {
        count2 += str.length();
    }
    
    if (count1 < count2) {
        return lst1;
    } else if (count1 > count2) {
        return lst2;
    } else {
        return lst1;
    }
}

int main() {
    vector<string> v1 = {"hi", "admin"};
    vector<string> v2 = {"hI", "Hi"};
    vector<string> result = total_match(v1, v2);
    
    for (const auto& str : result) {
        cout << str << " ";
    }
    
    return 0;
}
C:
#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> total_match(vector<string> lst1, vector<string> lst2) {
    int sum1 = 0, sum2 = 0;
    for (auto& str : lst1) {
        sum1 += str.length();
    }
    for (auto& str : lst2) {
        sum2 += str.length();
    }
    
    if (sum1 < sum2) {
        return lst1;
    } else if (sum1 > sum2) {
        return lst2;
    } else {
        return lst1;
    }
}

int main() {
    vector<string> v