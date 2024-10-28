    int count = 0;
    for(int i = 2; i <= a; i++){
        if(a % i == 0){
            while(a % i == 0){
                a = a / i;
            }
            count++;
        }
    }
    if(count == 3){
        return true;
    }
    else{
        return false;
    }
}

int main()
{
    printf("%d", is_multiply_prime(30));
    return 0;
}

*/

int main() {
    int num;
    cout << "Enter a number: ";
    cin >> num;
    if (is_multiply_prime(num)) {
        cout << "True";
    } else {
        cout << "False";
    }
    return 0;
}

This program will return true if a number is a multiplication of 3 prime numbers and false otherwise.
*/


#include<bits/stdc++.h>
using namespace std;

bool is_multiply_prime(int a){
    int count = 0;
    for(int i = 2; i <= a; i++){
        if(a % i == 0){
            while(a % i == 0){
                a = a / i;
            }
            count++;
        }
    }
    if(count == 3){
        return true;
    }
    else{
        return false;
    }
}

int main()
{
    int num;
    cout << "Enter a number: ";
    cin >> num;
    if (is_multiply_prime(num)) {
        cout << "True";
    } else {
        cout << "False";
    }
    return 0;
}


*/

/*
