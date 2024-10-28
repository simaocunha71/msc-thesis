    vector<int> even;
    int num = a;
    while(num < b){
        if(num%2 == 0){
            even.push_back(num);
        }
        num++;
    }
    if(b%2 == 0) even.push_back(b);
    return even;
}

int main(){
    vector<int> res = generate_integers(2, 8);
    for(int i = 0;i < res.size();i++)
        printf("%d ", res[i]);
    printf("\n");
    return 0;
}





*/
#include<bits/stdc++.h>
using namespace std;

vector<int> generate_integers(int a,int b){
    vector<int> even;
    for(int num = a;num < b;num++)
        if(num%2 == 0)