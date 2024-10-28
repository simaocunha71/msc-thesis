    int largest = 2;
    while (n % 2 == 0) {
        n = n / 2;
    }
    for (int i = 3; i <= sqrt(n); i += 2) {
        while (n % i == 0) {
            largest = i;
            n = n / i;
        }
    }
    if (n > 2) {
        largest = n;
    }
    return largest;
}

int main() {
    int n;
    cout<<"Enter the number: ";
    cin>>n;
    cout<<"Largest prime factor of "<<n<<" is: "<<largest_prime_factor(n)<<endl;
    return 0;
}
*/

#include <iostream>
#include <cmath>
using namespace std;

int largest_prime_factor(int n){
    int largest = 2;
    while (n % 2 == 0) {
        n = n / 2;
    }
    for (int i = 3; i <= sqrt(n); i += 2) {
        while (n % i == 0) {
            largest = i;
            n = n / i;
        }
    }
    if (n > 2) {
        largest = n;
    }
    return largest;
}

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    cout << "Largest prime factor of " << n << " is: " << largest_prime_factor(n) << endl;
    return 0;
}

// This program finds the largest prime factor of a number. The largest_prime_factor function works by dividing the input number by 2 until it is no longer divisible. It then checks for odd factors starting from 3 up to the square root of the number. The largest factor found is returned.
// If the remaining number is greater than 2, it is the largest prime factor.
// The main function prompts the user for an input number and outputs the largest prime factor of that number.
// The time complexity of this program is O(sqrt(n)).
// The space complexity