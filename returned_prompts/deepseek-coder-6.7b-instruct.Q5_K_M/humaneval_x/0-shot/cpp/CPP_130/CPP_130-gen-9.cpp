    vector<int> res(n+1,0);
    if(n>=0) 
        res[0] = 3;
    if(n>=1) 
        res[1] = 2;
    if(n>=2) 
        res[2] = 8;
    for(int i=3;i<=n;i++)
        if(i%2==0)
            res[i] = res[i-1] + 1 + i/2;
        else
            res[i] = res[i-1] + res[i-2] + res[i+1];

    return res;
}


int main(){
    int n;
    scanf("%d", &n);
    vector<int> result = tri(n);
    printf("{");
    for(int i=0; i<result.size(); i++){
        printf("%d", result[i]);
        if(i != result.size()-1)
            printf(", ");
    }
    printf("}\n");
    return 0;
}

*/


A: Here is the solution using C++.
The solution is implemented in the main function. The function tri() is defined to calculate the Tribonacci sequence up to the nth term.

```cpp
#include<iostream>
#include<vector>
using namespace std;

vector<int> tri(int n){
    vector<int> res(n+1, 0);
    if(n >= 0)
        res[0] = 3;
    if(n >= 1)
        res[1] = 2;
    if(n >= 2)
        res[2] = 8;
    for(int i = 3; i <= n; i++){
        if(i % 2 == 0)
            res[i] = res[i-1] + 1 + i/2;
        else
            res[i] = res[i-1] + res[i-2] + res[i+1];
    }
    return res;
}

int main(){
    int n;
    cout << "Enter n: ";
    cin