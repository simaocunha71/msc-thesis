    vector<int> res;
    if(a>b){
        for(int i=a;i>=b;i--){
            if(i%2==0){
                res.push_back(i);
            }
        }
    }
    else{
        for(int i=a;i<=b;i++){
            if(i%2==0){
                res.push_back(i);
            }
        }
    }
    return res;
}

int main(){
    int a,b;
    while(~scanf("%d%d",&a,&b)){
        vector<int> v = generate_integers(a,b);
        for(int i=0;i<v.size();i++){
            printf("%d ",v[i]);
        }
    }
}

*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> generate_integers(int a,int b){

    vector<int> res;
    if(a>b){
        for(int i=a;i>=b;i--){
            if(i%2==0){
                res.push_back(i);
            }
        }
    }
    else{
        for(int i=a;i<=b;i++){
            if(i%2==0){
                res.push_back(i);
            }
        }
    }
    return res;
}

int main(){
    int a,b;
    while(~scanf("%d%d",&a,&b)){
        vector<int> v = generate_integers(a,b);
        for(int i=0;i<v.size();i++){
            printf("%d ",v[i]);
        }
    }
}










































































