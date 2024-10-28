    if(a==0){
        return true;
    }
    if(sqrt(a)%1==0){
        return true;
    }
    else{
        goto A;
    }
}
int main(){
    int a;
    scanf("%d",&a);
    if(iscuber(a)){
        printf("true");
    }
    else{
        printf("false");
    }
    return 0;
}

*/

#include<iostream>
#include<cmath>
using namespace std;
bool iscube(int a){
    int sqr = int(pow(a,1.0/3.0));
    if(sqr*sqr*sqr==a){
        return true;
    }
    else{
        return false;
    }
}
int main(){
    int a;
    cin>>a;
    if(iscube(a)){
        cout<<"true";
    }
    else{
        cout<<"false";
    }
    return 0;
}






























```