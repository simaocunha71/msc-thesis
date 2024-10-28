    if(n<=0)
        return 0;
    else if(n==1)
        return 1;
    else 
        return fib(n-1)+fib(n-2);
}
int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d",&n);
    printf("Fibonacci number is: %d",fib(n));
    return 0;
}

*/

#include <iostream>
#include <vector>
using namespace std;

int fib(int n) {
    vector<int> fibs{0, 1};
    
    for (int i = 2; i <= n; i++)
        fibs.push_back(fibs[i-1] + fibs[i-2]);
    
    return fibs[n];
}

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    cout << "Fibonacci number is: " << fib(n) << endl;
    return 0;
}

// 2. Write a program in C++ to find the largest element in an array.
/*
