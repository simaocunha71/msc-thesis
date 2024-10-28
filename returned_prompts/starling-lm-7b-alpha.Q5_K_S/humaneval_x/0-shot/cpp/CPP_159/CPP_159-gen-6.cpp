
#include<iostream>
#include<vector>
using namespace std;
vector<int> eat(int number,int need,int remaining){
    int sum = number + need;
    if(sum > remaining){
        return vector<int>{sum,0};
    }
    else{
        return vector<int>{sum,remaining-sum};
    }
}
int main(){
    vector<int> v;
    v = eat(5,6,10);
    cout<<v[0]<<" "<<v[1]<<endl;
    v = eat(4,8,9);
    cout<<v[0]<<" "<<v[1]<<endl;
    v = eat(1,10,10);
    cout<<v[0]<<" "<<v[1]<<endl;
    v = eat(2,11,5);
    cout<<v[0]<<" "<<v[1]<<endl;
}




















```
