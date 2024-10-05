    if(n == 0) return 1;
    if(n == 1) return n;
    int h = n/2;
    int res = modp(h,p);
    res = res * res;
    res %= p;
    if(n%2 == 1) res *= n;
    res %= p;
    return res;
}

/*
Return 2^n modulo p (be aware of numerics).
>>> modp(3, 5)
3
>>> modp(1101, 101)
2
>>> modp(0, 101)
1
>>> modp(3, 11)
8
>>> modp(100, 101)
1
*/

int main() {

    int n,p;
    int h;
    int res;
    scanf("%d%d",&n,&p);
    res = modp(n,p);
    printf("%d\n",res);
    return 0;
}
















*/

#include <bits/stdc++.h>
using namespace std;

#define int long long

int mod(int n, int p) {
	if (n == 0) return 1;
	if (n == 1) return n;
	int h = n / 2;
	int res = mod(h, p);
	res = res * res;
	res %= p;
	if (n % 2 == 1) res *= n;
	res %= p;
	return res;
}

signed main() {
	int n, p;
	cin >> n >> p;
	cout << mod(n, p) << endl;
	return 0;
}


```