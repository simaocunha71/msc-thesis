#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <iostream>
using namespace std;
vector<int> tri(int n){
    vector<int> res;
    if(n==0) return res;
    res.push_back(1);
    if(n==1) return res;
    res.push_back(3);
    if(n==2) return res;
    for(int i=2;i<=n;i++){
        res.push_back(res[i-2]+res[i-1]+res[i]);
    }
    return res;
}
int main(){
    int n;
    cin>>n;
    vector<int> res=tri(n);
    for(int i=0;i<n;i++){
        cout<<res[i]<<" ";
    }
    return 0;
}

B:
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <iostream>
using namespace std;
vector<int> tri(int n){
    vector<int> res;
    if(n==0) return res;
    res.push_back(1);
    if(n==1) return res;
    res.push_back(3);
    if(n==2) return res;
    for(int i=2;i<=n;i++){
        if(i%2==0){
            res.push_back(1+i/2);
        }
        else{
            res.push_back(res[i-2]+res[i-1]+res[i]);
        }
    }
    return res;
}
int main(){
    int n;
    cin>>n;
    vector<int> res=tri(n);
    for(int i=0;i<n;i++){
        cout<<res[i]<<" ";
    }
    return 0;
}

C:
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <iostream>
using namespace std;
vector<int> tri(int n){
    vector<int> res;
    if(n==0) return res;
    res.push_back(3);
    if(n==1) return res;
    res.push_back(1);
    if(n==2) return res;
    for(int i=2;i<=n;i++){
        res.push_back(res[i-2]+res[i-1]+res[i]);
    }
    return res;
}
int main(){
    int n;
    cin>>n;
    vector<int> res=tri(n);
    for(int i=0;i<n;i++){
        cout<<res[i]<<" ";
    }
    return 0;
}

D:
#include <stdio.h>
#include <stdlib.h>
