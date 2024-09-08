/*
Return true if all numbers in the vector l are below threshold t.
>>> below_threshold({1, 2, 4, 10}, 100)
true
>>> below_threshold({1, 20, 4, 10}, 5)
false
*/
#include<iostream>
#include<vector>
using namespace std;
bool below_threshold(vector<int>l, int t){
    for(int i=0;i<l.size();i++){
        if(l[i]>t){
            return false;
        }
    }
    return true;
}
int main(){
    vector<int> l={1,2,4,10};
    int t=100;
    cout<<below_threshold(l,t)<<endl;
    l={1,20,4,10};
    t=5;
    cout<<below_threshold(l,t)<<endl;
    return 0;
}
B:
/*
Return true if all numbers in the vector l are below threshold t.
>>> below_threshold({1, 2, 4, 10}, 100)
true
>>> below_threshold({1, 20, 4, 10}, 5)
false
*/
#include<iostream>
#include<vector>
using namespace std;
bool below_threshold(vector<int>l, int t){
    for(int i=0;i<l.size();i++){
        if(l[i]>=t){
            return false;
        }
    }
    return true;
}
int main(){
    vector<int> l={1,2,4,10};
    int t=100;
    cout<<below_threshold(l,t)<<endl;
    l={1,20,4,10};
    t=5;
    cout<<below_threshold(l,t)<<endl;
    return 0;
}
C:
/*
Return true if all numbers in the vector l are below threshold t.
>>> below_threshold({1, 2, 4, 10}, 100)
true
>>> below_threshold({1, 20, 4, 10}, 5)
false
*/
#include<iostream>
#include<vector>
using namespace std;
bool below_threshold(vector<int>l, int t){
    for(int i=0;i<l.size();i++){
        if(l[i]<t){
            return true;
        }
    }
    return false;
}
int main(){
    vector<int> l={1,2,4,10};
    int t=100;
    cout<<below_threshold(l,t)<<endl;
    l={1,20,4,10};
    t=5;
    cout