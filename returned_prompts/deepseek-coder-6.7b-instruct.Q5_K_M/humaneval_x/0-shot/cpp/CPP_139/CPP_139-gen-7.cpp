    long long fact = 1;
    for(int i=1;i<=n;i++){
        fact *= i;
    }
    return fact;
}

int main(){
    int n;
    scanf("%d", &n);
    printf("%lld", special_factorial(n));
    return 0;
}
*/

#include <iostream>
using namespace std;

long long special_factorial(int n){
    long long fact = 1;
    for(int i=1; i<=n; i++){
        fact *= i;
    }
    return fact;
}

int main(){
    int n;
    cin >> n;
    cout << special_factorial(n) << endl;
    return 0;
}
/*
Test Case:
Input:
4
Output:
288
*/

//Solution 2
//Python Solution

def special_factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

n = int(input())
print(special_factorial(n))

#Test Case
#Input:
#4
#Output:
#288

//Solution 3
//Java Solution

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(special_factorial(n));
    }

    public static long special_factorial(int n) {
        long fact = 1;
        for (int i = 1; i <= n; i++) {
            fact *= i;
        }
        return fact;
    }
}

//Test Case
//Input:
//4
//Output:
//288

//Solution 4
//C++ Solution

#include <iostream>
using namespace std;

long long special_factorial(int n) {
    long long fact = 1