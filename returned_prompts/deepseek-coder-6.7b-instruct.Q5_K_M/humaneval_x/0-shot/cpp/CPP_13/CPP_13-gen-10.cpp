    if (b == 0)
        return a;
    return greatest_common_divisor(b, a % b);
}

int main(){
    int a = 25, b = 15;
    printf("%d", greatest_common_divisor(a, b));
    return 0;
}

*/

#include <iostream>
using namespace std;

int greatest_common_divisor(int a, int b) {
    if (b == 0)
        return a;
    return greatest_common_divisor(b, a % b);
}

int main() {
    int a = 25, b = 15;
    cout << greatest_common_divisor(a, b) << endl;
    return 0;
}

/*
