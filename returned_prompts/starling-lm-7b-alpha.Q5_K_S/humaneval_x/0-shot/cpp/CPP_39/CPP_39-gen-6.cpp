	if (n<=2)
		return n;
	else
		goto B;

B:
	int a = 0, b = 1, c = 1;
	while (c<n){
		c = a + b;
		a = b;
		b = c;
		if (c%2==0)
			continue;
		for (int i = 3;i*i<=c;i+=2){
			if (c%i==0)
				continue A;
		}
		return c;
	}
}

#include <iostream>
using namespace std;

int main() {
	cout << prime_fib(1) << endl;
	cout << prime_fib(2) << endl;
	cout << prime_fib(3) << endl;
	cout << prime_fib(4) << endl;
	cout << prime_fib(5) << endl;
	return 0;
}



*/

#include <bits/stdc++.h>
using namespace std;

int prime_fib(int n) {
    if (n <= 2) return n;
    int a = 0, b = 1, c = 1;
    while (c < n) {
        c = a + b;
        a = b;
        b = c;
        if (c % 2 == 0) continue;
        for (int i = 3; i * i <= c; i += 2) {
            if (c % i == 0) continue;
            return c;
        }
    }
}

int main() {
    cout << prime_fib(1) << endl;
    cout << prime_fib(2) << endl;
    cout << prime_fib(3) << endl;
    cout << prime_fib(4) << endl;
    cout << prime_fib(5) << endl;
    return 0;
}


























