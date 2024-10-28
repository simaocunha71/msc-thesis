    for(int i=n/2; i>=1; i--){
        if(n%i==0){
            return i;
        }
    }
}
int main() {
    int n;
    printf("Enter the number: ");
    scanf("%d",&n);
    printf("Largest divisor is: %d", largest_divisor(n));
    return 0;
}

*/

#include <iostream>
using namespace std;

int largest_divisor(int n) {
    for (int i = n / 2; i >= 1; i--) {
        if (n % i == 0) {
            return i;
        }
    }
}

int main() {
    int n;
    cout << "Enter the number: ";
    cin >> n;
    cout << "Largest divisor is: " << largest_divisor(n) << endl;
    return 0;
}

//C++/Program 5/main.cpp
/*
