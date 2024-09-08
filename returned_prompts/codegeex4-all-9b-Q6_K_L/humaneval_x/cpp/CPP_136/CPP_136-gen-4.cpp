#include<stdio.h>
#include<vector>
#include<math.h>
using namespace std;
vector<int> largest_smallest_integers(vector<int> lst){
    vector<int> res(2);
    int maxn = 0, minp = 0;
    for(auto x: lst){
        if(x < 0) maxn = max(maxn, x);
        else if(x > 0) minp = min(minp, x);
    }
    res[0] = maxn;
    res[1] = minp;
    return res;
}

B:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> largest_smallest_integers(vector<int> lst){
    vector<int> res(2);
    int maxn = 0, minp = 0;
    for(auto x: lst){
        if(x < 0) maxn = max(maxn, x);
        else if(x > 0) minp = min(minp, x);
    }
    res[0] = maxn;
    res[1] = minp;
    return res;
}

C:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> largest_smallest_integers(vector<int> lst){
    vector<int> res(2);
    int maxn = 0, minp = 0;
    for(auto x: lst){
        if(x < 0) maxn = max(maxn, x);
        else if(x > 0) minp = min(minp, x);
    }
    res[0] = maxn;
    res[1] = minp;
    return res;
}

D:
#include<stdio.h>
#include<vector>
#include<math.h>
using namespace std;
vector<int> largest_smallest_integers(vector<int> lst){
    vector<int> res(2);
    int maxn = 0, minp = 0;
    for(auto x: lst){
        if(x < 0) maxn = max(maxn, x);
        else if(x > 0) minp = min(minp, x);
    }
    res[0] = maxn;
    res[1] = minp;
    return res;
}

E:
#include<stdio.h>
#include<vector>
#include<math.h>
using namespace std;
vector<int> largest_smallest_integers(vector<int> lst){
    vector<int> res(2);
    int maxn = 0, minp = 0