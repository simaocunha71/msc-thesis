#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> get_odd_collatz(int n){
    vector<int> odd;
    while(n>1){
        if(n%2==1) odd.push_back(n);
        n = n/2;
    }
    odd.push_back(1);
    sort(odd.begin(), odd.end());
    return odd;
}
B:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> get_odd_collatz(int n){
    vector<int> odd;
    while(n>1){
        if(n%2==1) odd.push_back(n);
        if(n%2==0) n = n/2;
        else n = n*3+1;
    }
    odd.push_back(1);
    sort(odd.begin(), odd.end());
    return odd;
}
C:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> get_odd_collatz(int n){
    vector<int> odd;
    while(n>1){
        if(n%2==1) odd.push_back(n);
        n = n/2;
    }
    odd.push_back(1);
    sort(odd.begin(), odd.end());
    return odd;
}
D:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> get_odd_collatz(int n){
    vector<int> odd;
    while(n>1){
        if(n%2==1) odd.push_back(n);
        else n = n/2;
    }
    odd.push_back(1);
    sort(odd.begin(), odd.end());
    return odd;
}
E:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> get_odd_collatz(int n){
    vector<int> odd;
    while(n>1){
        if(n%2==1) odd.push_back(n);
        else n = n*3+1;
    }
    odd.push_back(1);
    sort(odd.begin(), odd.end());
    return odd;
}
F:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> get_odd_collatz(int n){
    vector<int> odd;
    while(n>1){
        if(n%2==1) odd.push_back(n);
        if(n%2==0) n = n*3+1;
        else n = n/2;
    }
    odd.push_back(1);
    sort(odd