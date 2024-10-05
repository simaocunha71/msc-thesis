
#include<iostream>
#include<algorithm>
#include<set>
using namespace std;
set<int> common(vector<int> l1,vector<int> l2){
    set<int> l3;
    set<int> l4=l1;
    for(auto i:l2){
        if(l4.find(i)!=l4.end()){
            l3.insert(i);
            l4.erase(i);
        }
    }
    return l3;
}
int main(){
    vector<int> l1={1, 4, 3, 34, 653, 2, 5},l2={5, 7, 1, 5, 9, 653, 121};
    for(auto i:common(l1,l2))
        printf("%d ",i);
    return 0;
}















