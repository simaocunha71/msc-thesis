    if(n==0){
        return "0";
    }
    else{
        char str[100];
        sprintf(str,"%d ",n);
        string s=string(str);
        string s1=string_sequence(n-1);
        return s+s1;
    }
}







/*
    Author: Jojohan
    Created at: 2021-05-21 21:40
*/

#include <bits/stdc++.h>
using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define RFOR(i, a, b) for (int i = (b)-1; i >= (a); i--)
#define REP(i, n) FOR(i, 0, n)
#define RREP(i, n) RFOR(i, 0, n)
#define ALL(x) (x).begin(), (x).end()

template<class T> inline bool chmax(T &a, T b) { if (a < b) { a = b; return 1; } return 0; }
template<class T> inline bool chmin(T &a, T b) { if (a > b) { a = b; return 1; } return 0; }

typedef long long int64;
typedef long double ld;

const int INF = 1<<30;
const int64 LINF = 1LL<<60;
const ld PI = acos(-1.0);
const ld EPS = 1e-10;

template<typename T> ostream &operator<<(ostream &os, const vector<T> &vec){
    os << "[";
    for (const auto &v : vec) {
    	os << v << ",";
    }
    os << "]";
    return os;
}

#define ARRAY_MAX 1000

typedef vector<int> vec;
typedef vector<vec> mat;

void solve