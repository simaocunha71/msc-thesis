    if(a+b==c||b+c==a||c+a==b&&(int)a==a&&(int)b==b&&(int)c==c)
        return true;
    else
        return false;



*/
#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    cout << any_int(a, b, c);
    return 0;
}

```