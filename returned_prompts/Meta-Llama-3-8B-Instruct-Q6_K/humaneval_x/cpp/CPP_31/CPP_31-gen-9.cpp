    if(n <= 1) {
        return false;
    }
    for(long long i = 2; i * i <= n; i++) {
        if(n % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    printf("%d\n", is_prime(6)); // false
    printf("%d\n", is_prime(101)); // true
    printf("%d\n", is_prime(11)); // true
    printf("%d\n", is_prime(13441)); // true
    printf("%d\n", is_prime(61)); // true
    printf("%d\n", is_prime(4)); // false
    printf("%d\n", is_prime(1)); // false
    return 0;
}
B:
    #include <iostream>
    using namespace std;

    bool is_prime(int n) {
        if(n <= 1) {
            return false;
        }
        for(int i = 2; i * i <= n; i++) {
            if(n % i == 0) {
                return false;
            }
        }
        return true;
    }

    int main() {
        cout << is_prime(6) << endl; // false
        cout << is_prime(101) << endl; // true
        cout << is_prime(11) << endl; // true
        cout << is_prime(13441) << endl; // true
        cout << is_prime(61) << endl; // true
        cout << is_prime(4) << endl; // false
        cout << is_prime(1) << endl; // false
        return 0;
    }
C:
    #include <iostream>
    using namespace std;

    bool is_prime(long long int n) {
        if(n <= 1) {
            return false;
        }
        for(long long int i = 2; i * i <= n; i++) {
            if(n % i == 0) {
                return false;
            }
        }
        return true;
    }

    int main() {
        cout << is_prime(6) << endl; // false
        cout << is_prime(101) << endl; // true
        cout << is_prime(11) << endl; // true
        cout << is_prime(13441) << endl; // true
        cout << is_prime(61) << endl; // true
        cout << is_prime