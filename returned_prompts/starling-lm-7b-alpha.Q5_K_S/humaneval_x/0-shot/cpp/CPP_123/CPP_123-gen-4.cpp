    vector<int> ret;
    for(int i = n; i > 0; --i){
        if(i & 1){
            ret.push_back(i);
            if(i > 1)
                i = (i / 3) + 1;
        } else {
            i >>= 1;
        }
    }
    sort(ret.begin(), ret.end());
    return ret;
}

int main(){
    int n;
    scanf("%d", &n);
    vector<int> ret = get_odd_collatz(n);
    for(int i = 0; i < ret.size(); ++i)
        printf("%d ", ret[i]);
    puts("");
    return 0;
}

*/

#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<sstream>
#include<bitset>
#include<functional>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()

template<typename A, typename B> inline bool chmax(A &a, B b) { if (a<b) { a=b; return 1; } return 0; }
template<typename A, typename B> inline bool chmin(A &a, B b) { if (a>b) { a=b; return 1; } return 0; }

typedef long long ll;

const int INF = 1000000000;
const int MOD = 1000000007;
const double EPS = 1e-10;

int main() {
    int n