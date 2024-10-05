    int len = str.length();
    if (len <= 1) return false;
    if (len == 2 || len == 3) return true;
    if (len % 2 == 0 || len % 3 == 0) return false;
    for (int i = 5; i * i <= len; i += 6)
        if (len % i == 0 || len % (i + 2) == 0)
            return false;
    return true;
}

int main(){
    printf("%d\n", prime_length("Hello"));
    printf("%d\n", prime_length("abcdcba"));
    printf("%d\n", prime_length("kittens"));
    printf("%d\n", prime_length("orange"));
    return 0;
}
*/

//C++/C++-Programs/prime_length.cpp
#include<iostream>
#include<string>
using namespace std;

bool isPrime(int num) {
    if (num <= 1) return false;
    if (num == 2 || num == 3) return true;
    if (num % 2 == 0 || num % 3 == 0) return false;
    for (int i = 5; i * i <= num; i += 6)
        if (num % i == 0 || num % (i + 2) == 0)
            return false;
    return true;
}

bool prime_length(string str) {
    return isPrime(str.length());
}

int main() {
    cout << boolalpha << prime_length("Hello") << endl;
    cout << boolalpha << prime_length("abcdcba") << endl;
    cout << boolalpha << prime_length("kittens") << endl;
    cout << boolalpha << prime_length("orange") << endl;
    return 0;
}

//C++/C++-Programs/prime_length_py.cpp
#include<iostream>
#include<string>
using namespace std;

bool isPrime(int num) {
    if (num <= 1) return false;
    if (num == 2 || num == 3) return true