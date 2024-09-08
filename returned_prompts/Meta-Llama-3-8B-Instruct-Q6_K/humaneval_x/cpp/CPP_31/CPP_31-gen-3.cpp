    if(n <= 1) return false;
    if(n <= 3) return true;
    if(n % 2 == 0 || n % 3 == 0) return false;
    long long i = 5;
    while(i * i <= n){
        if(n % i == 0 || n % (i + 2) == 0) return false;
        i += 6;
    }
    return true;
}
int main(){
    printf("%d\n",is_prime(6));
    printf("%d\n",is_prime(101));
    printf("%d\n",is_prime(11));
    printf("%d\n",is_prime(13441));
    printf("%d\n",is_prime(61));
    printf("%d\n",is_prime(4));
    printf("%d\n",is_prime(1));
    return 0;
}
B:
    // Write your code here
    #include<iostream>
    using namespace std;
    bool is_prime(long long n){
        if(n <= 1) return false;
        if(n <= 3) return true;
        if(n % 2 == 0 || n % 3 == 0) return false;
        long long i = 5;
        while(i * i <= n){
            if(n % i == 0 || n % (i + 2) == 0) return false;
            i += 6;
        }
        return true;
    }
    int main(){
        cout << boolalpha;
        cout << is_prime(6) << endl;
        cout << is_prime(101) << endl;
        cout << is_prime(11) << endl;
        cout << is_prime(13441) << endl;
        cout << is_prime(61) << endl;
        cout << is_prime(4) << endl;
        cout << is_prime(1) << endl;
        return 0;
    }
C:
    // Write your code here
    #include<iostream>
    using namespace std;
    bool is_prime(long long n){
        if(n <= 1) return false;
        if(n <= 3) return true;
        if(n % 2 == 0 || n % 3 == 0) return false;
        long long i = 5;
        while(i * i <= n){
            if(n % i == 0 || n % (i + 2) == 0) return false;
            i += 6;
