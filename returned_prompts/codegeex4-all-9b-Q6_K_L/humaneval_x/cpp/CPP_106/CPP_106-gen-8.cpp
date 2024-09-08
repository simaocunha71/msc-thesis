vector<int> ans;
    for(int i=1;i<=n;i++){
        if(i%2==0){
            int fact=1;
            for(int j=1;j<=i;j++){
                fact*=j;
            }
            ans.push_back(fact);
        }
        else{
            int sum=0;
            for(int j=1;j<=i;j++){
                sum+=j;
            }
            ans.push_back(sum);
        }
    }
    return ans;
}

B:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> f(int n){

vector<int> ans;
    for(int i=1;i<=n;i++){
        if(i%2==0){
            int fact=1;
            for(int j=1;j<=i;j++){
                fact*=j;
            }
            ans.push_back(fact);
        }
        else{
            int sum=0;
            for(int j=1;j<=i;j++){
                sum+=j;
            }
            ans.push_back(sum);
        }
    }
    return ans;
}

C:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> f(int n){

    vector<int> ans;
    for(int i=1;i<=n;i++){
        if(i%2==0){
            int fact=1;
            for(int j=1;j<=i;j++){
                fact*=j;
            }
            ans.push_back(fact);
        }
        else{
            int sum=0;
            for(int j=1;j<=i;j++){
                sum+=j;
            }
            ans.push_back(sum);
        }
    }
    return ans;
}

D:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> f(int n){

    vector<int> ans;
    for(int i=1;i<=n;i++){
        if(i%2==0){
            int fact=1;
            for(int j=1;j<=i;j++){
                fact*=j;
            }
            ans.push_back(fact);
        }
        else{
            int sum=0;
            for(int j=1;j<=i;j++){
                sum+=j;
            }
            ans.push_back(sum);
        }
    }
    return ans;
}
请问哪个选项是正确的？

选项C是正确的。

以下是选项C的代码：

```cpp
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> f(int n){

    vector<int> ans;
    for(int i=1;i<=