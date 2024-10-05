    int res=1;
    n=n%p;
    while(p>0){
        if(p&1)
            res=(res*n)%p;
        p=p>>1;
        n=(n*n)%p;
    }
    return res;
}

int main(){
    int n,p;
    scanf("%d %d",&n,&p);
    printf("%d\n",modp(n,p));
    return 0;
}

*/
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n, p;
    cin >> n >> p;
    cout << (int)pow(2, n) % p << "\n";
    return 0;
}

//Test/C++/modular_exponentiation/modular_exponentiation.cpp
#include <iostream>
#include <cmath>
using namespace std;

long long modulo_exponentiation(long long x, long long n, long long p) {
    long long res = 1;
    x = x % p;
    while (n > 0) {
        if (n & 1)
            res = (res * x) % p;
        n = n >> 1;
        x = (x * x) % p;
    }
    return res;
}

int main() {
    long long x, n, p;
    cin >> x >> n >> p;
    cout << modulo_exponentiation(x, n, p) << "\n";
    return 0;
}

//Test/C++/nth_root/nth_root.cpp
#include <iostream>
#include <cmath>
using namespace std;

double nth_root(int n, double x) {
    double res = exp(log(x) / n);
    return res;
}

int main() {
    int n;
    double x;
    cin >> n >> x;
    cout << nth_root(n, x) << "\n";
    return 