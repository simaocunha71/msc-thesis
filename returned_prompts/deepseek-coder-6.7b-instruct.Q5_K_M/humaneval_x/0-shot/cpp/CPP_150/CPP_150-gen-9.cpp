    if(n == 2){
        return x;
    }else{
        return y;
    }
}

int main() {
    printf("%d\n", x_or_y(7, 34, 12)); // should print 34
    printf("%d\n", x_or_y(15, 8, 5)); // should print 5
    return 0;
}

*/


#include <iostream>
using namespace std;

bool isPrime(int n){
    if(n<=1){
        return false;
    }
    for(int i=2; i*i<=n; i++){
        if(n%i==0){
            return false;
        }
    }
    return true;
}

int x_or_y(int x,int y, int n){
    return (isPrime(n)) ? x : y;
}

int main() {
    cout << x_or_y(7, 34, 12) << endl; // should print 34
    cout << x_or_y(15, 8, 5) << endl; // should print 5
    return 0;
}





















































































































































































































