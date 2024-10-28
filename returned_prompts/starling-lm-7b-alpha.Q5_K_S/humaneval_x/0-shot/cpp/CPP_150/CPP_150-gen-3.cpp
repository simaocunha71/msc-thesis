#include <bits/stdc++.h>
using namespace std;

// This program should return the value of x if n is a prime number,
// and should return the value of y otherwise.

int x_or_y(int n, int x, int y) {
    if (n == 1)
        return y;
    else if (n == 2)
        return x;
    else if (n % 2 == 0)
        return y;
    else {
        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0)
                return y;
        }
        return x;
    }
}

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    cout << x_or_y(a, b, c);
}

















































































































































