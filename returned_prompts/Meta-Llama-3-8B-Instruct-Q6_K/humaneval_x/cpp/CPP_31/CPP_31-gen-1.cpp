    if(n<=1)
        return false;
    for(long long i=2;i*i<=n;i++){
        if(n%i == 0)
            return false;
    }
    return true;
}

int main(){
    printf("%d\n",(is_prime(6))?1:0); // 0
    printf("%d\n",(is_prime(101))?1:0); // 1
    printf("%d\n",(is_prime(11))?1:0); // 1
    printf("%d\n",(is_prime(13441))?1:0); // 1
    printf("%d\n",(is_prime(61))?1:0); // 1
    printf("%d\n",(is_prime(4))?1:0); // 0
    printf("%d\n",(is_prime(1))?1:0); // 0
    return 0;
}

B:
#include <iostream>
using namespace std;

bool is_prime(long long n) {
    if (n <= 1)
        return false;
    for (long long i = 2; i * i <= n; i++) {
        if (n % i == 0)
            return false;
    }
    return true;
}

int main() {
    cout << (is_prime(6) ? "true" : "false") << endl;  // false
    cout << (is_prime(101) ? "true" : "false") << endl; // true
    cout << (is_prime(11) ? "true" : "false") << endl;  // true
    cout << (is_prime(13441) ? "true" : "false") << endl; // true
    cout << (is_prime(61) ? "true" : "false") << endl;   // true
    cout << (is_prime(4) ? "true" : "false") << endl;    // false
    cout << (is_prime(1) ? "true" : "false") << endl;    // false
    return 0;
} 

C:
#include <iostream>
using namespace std;

bool is_prime(long long n) {
    if (n <= 1)
        return false;
    for (long long i = 2; i * i <= n; i++) {
        if (n % i == 0)
            return false;
    }
    return true;
}

int main() {
    cout << (is