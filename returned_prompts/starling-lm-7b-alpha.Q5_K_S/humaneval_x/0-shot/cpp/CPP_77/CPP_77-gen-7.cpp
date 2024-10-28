    if(a<=0){
        goto B;
    }
    if(pow(cbrt(a),3)==(double)a){
        return true;
    }else{
        goto A;
    }
B:
    return false;
}
int main(){
    int a;
    scanf("%d",&a);
    if(iscuber(a)){
        printf("true\n");
    }else{
        printf("false\n");
    }
    return 0;
}


*/
#include <bits/stdc++.h>
using namespace std;

int main() {
    int a;
    cin>>a;
    if(a<0){
        cout<<"false\n";
        return 0;
    }
    if(cbrt(a)*cbrt(a)*cbrt(a)==a){
        cout<<"true\n";
    }else{
        cout<<"false\n";
    }
    return 0;
}

```