    int sum = 0;
    while(N > 0){
        sum += N % 2;
        N /= 2;
    }
    return to_string(sum);
}

int main()
{
    int N;
    printf("Enter a positive integer: ");
    scanf("%d", &N);
    printf("%s\n", solve(N).c_str());
    return 0;
}

C:
#include <stdio.h>
#include <string.h>

char *solve(int N) {
    char *result = (char *)malloc(33 * sizeof(char)); // 32 for the binary and 1 for the null
    int sum = 0;
    while(N > 0) {
        sum += N % 2;
        N /= 2;
    }
    sprintf(result, "%d", sum);
    return result;
}

int main() {
    int N;
    printf("Enter a positive integer: ");
    scanf("%d", &N);
    printf("%s\n", solve(N));
    return 0;
}

D:
#include <stdio.h>
#include <string.h>

char *solve(int N) {
    char *result = (char *)malloc(33 * sizeof(char)); // 32 for the binary and 1 for the null
    int sum = 0;
    while(N > 0) {
        sum += N % 2;
        N /= 2;
    }
    sprintf(result, "%d", sum);
    return result;
}

int main() {
    int N;
    printf("Enter a positive integer: ");
    scanf("%d", &N);
    printf("%s\n", solve(N));
    return 0;
}
*/



C++:
```cpp
#include <iostream>
#include <string>
using namespace std;

string solve(int N) {
    int sum = 0;
    while(N > 0) {
        sum += N % 2;
        N /= 2;
    }
    return to_string(sum);
}

int main() {
    int N;
    cout << "Enter a positive integer: ";
    cin >> N;
    cout << solve(N) << endl;
    return 0;
}
```



Explanation:

1.  The task is to write a program that takes a positive integer as input and returns the sum of its digits in binary.
2.  The program uses a while loop to iterate through the digits of the input number, adding each digit to a running total.
3.  The total is then converted