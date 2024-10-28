
}
int main(){
    int n;
    scanf("%d",&n);
    vector<int> result = tri(n);
    for(int i = 1 ; i <= n ; i++)
        printf("%d ",result[i]);
    return 0;
}

*/
#include<iostream>
#include<vector>
using namespace std;

vector<int> tri(int n){
    vector<int> t(n+1);
    if(n>=0) t[1] = 3;
    for(int i=2; i<=n; i++){
        if(i%2 == 0) t[i] = 1 + i/2;
        else t[i] = t[i-1] + t[i-2] + t[i+1];
    }
    return t;
}

int main(){
    int n;
    cin >> n;
    vector<int> result = tri(n);
    for(int i = 1 ; i <= n ; i++)
        cout << result[i] << " ";
    return 0;
}

/*
Output:

3
3 8 2 8 

*/