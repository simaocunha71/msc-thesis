    if(a==0||a<0)
        return true;
    int x=pow(a,1.0/3.0);
    if(pow(x,3)==a)
        return true;
    else{
        a--;
        goto A;
    }
}
int main(){
    int a;
    scanf("%d",&a);
    printf("%d\n",iscuber(a));
    return 0;
}





*/
#include <bits/stdc++.h>
using namespace std;

// macro
#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define RFOR(i, a, b) for (int i = (b) - 1; i >= (a); i--)
#define REP(i, n) for (int i = 0; i < (n); i++)
#define RREP(i, n) for (int i = (n) - 1; i >= 0; i--)
#define ALL(a) (a).begin(), (a).end()
#define SZ(a) (int)(a).size()
#define EXIST(s, e) ((s).find(e) != (s).end())
#define SORT(c) sort((c).begin(), (c).end())
#define RSORT(c) sort((c).rbegin(), (c).rend())

// typedef
typedef long long LL;
typedef vector<int> VI;
typedef vector<LL> VL;
typedef vector<VI> VVI;
typedef vector<VL> VVL;
typedef pair<int, int> PII;
typedef pair<LL, LL> PL;

// constants
const int inf = 1e9 + 7;
const LL INF = 1e18 + 7;
const double PI = acos(-1.0);

// clear memory
void clearMemory() { freeMemory(); }

// input
int ni() { int x; scanf("%d", &x); return x; }
LL nl() { LL