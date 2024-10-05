#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string exchange(vector<int> lst1,vector<int> lst2){
    int even_c = 0;
    for(int i=0;i<lst1.size();i++){
        if(lst1[i] % 2 == 0)even_c++;
    }
    if(even_c == lst1.size())return "YES";
    for(int i=0;i<lst1.size();i++){
        for(int j=0;j<lst2.size();j++){
            if(lst1[i] % 2 != 0 && lst2[j] % 2 == 0){
                lst1[i] = lst2[j];
                goto A;
            }
        }
    }
    return "NO";
}

int main(){
    vector<int> lst1 = {1, 2, 3, 4};
    vector<int> lst2