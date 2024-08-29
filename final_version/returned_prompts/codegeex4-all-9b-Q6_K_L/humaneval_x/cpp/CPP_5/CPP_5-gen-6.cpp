#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> intersperse(vector<int> numbers, int delimeter){
    if(numbers.empty())
        return numbers;
    for(int i=1; i<numbers.size(); i++)
        numbers.insert(numbers.begin()+i*2, delimeter);
    return numbers;
}
int main(){
    vector<int> a = {1, 2, 3};
    vector<int> b = intersperse(a, 4);
    for(int i=0; i<b.size(); i++)
        cout<<b[i]<<" ";
    cout<<endl;
}