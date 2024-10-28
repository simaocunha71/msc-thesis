    for(int i=0; i<l.size(); i++){
        for(int j=i+1; j<l.size(); j++){
            if(l[i] + l[j] == 0)
                return true;
        }
    }
    return false;
}

int main(){
    printf("%d\n", pairs_sum_to_zero(vector<int>{1, 3, 5, 0}));
    printf("%d\n", pairs_sum_to_zero(vector<int>{1, 3, -2, 1}));
    printf("%d\n", pairs_sum_to_zero(vector<int>{1, 2, 3, 7}));
    printf("%d\n", pairs_sum_to_zero(vector<int>{2, 4, -5, 3, 5, 7}));
    printf("%d\n", pairs_sum_to_zero(vector<int>{1}));
    return 0;
}

*/

//C++/main.cpp
#include<iostream>
#include<vector>
#include<unordered_set>
using namespace std;

bool pairs_sum_to_zero(vector<int> l){
    unordered_set<int> s;

    for(int i=0; i<l.size(); i++){
        if(s.find(-l[i]) != s.end())
            return true;
        s.insert(l[i]);
    }
    return false;
}

int main(){
    cout<<boolalpha<<pairs_sum_to_zero(vector<int>{1, 3, 5, 0})<<endl;
    cout<<boolalpha<<pairs_sum_to_zero(vector<int>{1, 3, -2, 1})<<endl;
    cout<<boolalpha<<pairs_sum_to_zero(vector<int>{1, 2, 3, 7})<<endl;
    cout<<boolalpha<<pairs_sum_to_zero(vector<int>{2,