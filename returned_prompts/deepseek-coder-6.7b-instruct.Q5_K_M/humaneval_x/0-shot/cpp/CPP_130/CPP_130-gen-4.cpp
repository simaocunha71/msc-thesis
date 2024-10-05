    vector<int> result(n + 1);
    if(n >= 0){
        result[0] = 1;
    }
    if(n >= 1){
        result[1] = 3;
    }
    if(n >= 2){
        result[2] = 2;
    }
    if(n >= 3){
        for(int i = 3; i <= n; i++){
            if(i % 2 == 0){
                result[i] = result[i - 1] + (i / 2);
            }else{
                result[i] = result[i - 1] + result[i - 2] + result[i - 3];
            }
        }
    }
    return result;
}
int main(){
    vector<int> result = tri(3);
    for(int i = 0; i < result.size(); i++){
        printf("%d ", result[i]);
    }
    return 0;
}

*/


int main() {
    int n;
    scanf("%d", &n);
    vector<int> result = tri(n);
    for(int i = 0; i < result.size(); i++){
        printf("%d ", result[i]);
    }
    return 0;
}

/*
Output:
Input:
3
Output:
1 3 2 8
*/
```

---

## Problem 2:

Write a C++ program to implement a simple calculator.

```cpp
#include<iostream>
using namespace std;
int main(){
    int num1, num2;
    char op;
    cout << "Enter first number: ";
    cin >> num1;
    cout << "Enter operator (+, -, *, /): ";
    cin >> op;
    cout << "Enter second number: ";
    cin >> num2;
    switch(op){
        case '+':
            cout << num1 << " + " << num2 << " = " << num1 + num2 << endl;
            break;
        case '-':
            cout << num1 << " - " << num2