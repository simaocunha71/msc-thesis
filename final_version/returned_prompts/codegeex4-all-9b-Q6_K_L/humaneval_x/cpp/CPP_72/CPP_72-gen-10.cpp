#include<stdio.h>
#include<math.h>
using namespace std;
#include<vector>
using namespace std;
bool will_it_fly(vector<int> q,int w){
    int sum=0;
    int n=q.size();
    for(int i=0;i<n;i++){
        sum+=q[i];
    }
    if(sum>w) return false;
    for(int i=0;i<n/2;i++){
        if(q[i]!=q[n-i-1]) return false;
    }
    return true;
}

B:
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
bool will_it_fly(vector<int> q,int w){
    int sum=0;
    int n=q.size();
    for(int i=0;i<n;i++){
        sum+=q[i];
    }
    if(sum>w) return false;
    for(int i=0;i<n/2;i++){
        if(q[i]!=q[n-i-1]) return false;
    }
    return true;
}

C:
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
bool will_it_fly(vector<int> q,int w){
    int sum=0;
    int n=q.size();
    for(int i=0;i<n;i++){
        sum+=q[i];
    }
    if(sum>w) return false;
    for(int i=0;i<n/2;i++){
        if(q[i]!=q[n-i-1]) return false;
    }
    return true;
}

D:
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
bool will_it_fly(vector<int> q,int w){
    int sum=0;
    int n=q.size();
    for(int i=0;i<n;i++){
        sum+=q[i];
    }
    if(sum>w) return false;
    for(int i=0;i<n/2;i++){
        if(q[i]!=q[n-i-1]) return false;
    }
    return true;
}

E:
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
bool will_it_fly(vector<int> q,int w){
    int sum=0;
    int n=q.size();
    for(int i=0;i<n;i++){
        sum+=q[i];
    }
    if(sum>w) return false;
    for(int i=0;i<n/2;i++){
        if(q[i]!=q[n-i-1]) return false;
    }
    return true;
}

F:
#include<stdio.h