    int res = 0, cnt = 0;
    for(int i = 1; i <= 9; i++) res++;
    for(int i = 1; i < 10; i++){
        for(int j = 0; j < i; j++){
            for(int k = 0; k < 10; k++){
                cnt++;
                if(k == 1 || i == 1) res++;
            }
        }
    }
    return res;
}

int main(){
    int n;
    printf("Enter a positive integer n: ");
    scanf("%d", &n);
    printf("The number of n-digit positive integers that start or end with 1 is: %d\n", starts_one_ends(n));
    return 0;
}

B:
#include <iostream>
using namespace std;

int countNumbersWithOne(int n) {
    int res = 0;
    // Count numbers that start with 1
    for (int i = 1; i < (1 << (n - 1)); i++) {
        res++;
    }
    // Count numbers that end with 1
    for (int i = 1; i <= (1 << (n - 1)); i++) {
        res++;
    }
    return res;
}

int main() {
    int n;
    cout << "Enter a positive integer n: ";
    cin >> n;
    cout << "The number of n-digit positive integers that start or end with 1 is: " << countNumbersWithOne(n) << endl;
    return 0;
}

C:
#include <iostream>
using namespace std;

int countNumbersWithOne(int n) {
    int res = 0;
    // Count numbers that start with 1
    for (int i = 1; i < (1 << (n - 1)); i++) {
        res++;
    }
    // Count numbers that end with 1
    for (int i = 1; i <= (1 << (n - 1)); i++) {
        res++;
    }
    return res;
}

int main() {
    int n;
    cout << "Enter a positive integer n: ";
    cin >> n;
    cout << "The number of n-digit positive integers that start or end with 1 is: " << countNumbersWithOne(n) << endl;
    return 0;
}

D:
#include <iostream>
using namespace std;

int countNumbersWithOne(int