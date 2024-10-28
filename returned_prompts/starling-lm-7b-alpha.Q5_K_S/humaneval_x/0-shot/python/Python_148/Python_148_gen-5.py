
def bf(planet1, planet2):
    planet_order = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planet_order or planet2 not in planet_order:
        return ()
    i1 = planet_order.index(planet1)
    i2 = planet_order.index(planet2)
    if i1 > i2:
        i1, i2 = i2, i1
    return tuple(planet_order[i1+1:i2])




# Made By Mostafa_Khaled









```
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;





```;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

```

#include <bits/stdc++.h>
using namespace std;
#define int long long
#define all(v) (v).begin(),(v).end()
#define rep(i,n) for(int i=0;i<(int)(n);++i)
#define reps(i,a,b) for(int i=a;i<(int)(b);++i)
#define defi(n) int n;cin>>n;
#define defii(n,m) int n,m;cin>>n>>m;
#define defiii(n,m,k) int n,m,k;cin>>n>>m>>k;
#define defiv(n,m,v) int n,m,v;cin>>n>>m>>v;
#