    if(n<=1)
        return 0;
    else if(n==2)
        return 1;
    else {
        int a[3];
        a[0] = 0;
        a[1] = 0;
        a[2] = 1;
        for(int i=3; i<=n; i++){
            a[i % 3] = a[(i-1)%3] + a[(i-2)%3] + a[(i-3)%3];
        }
        return a[n%3];
    }
}

int main()
{
    int n;
    printf("Enter the value of n: ");
    scanf("%d",&n);
    printf("The %d-th element of the fibfib number sequence is: %d\n",n,fibfib(n));
    return 0;
}
B:
#include<stdio.h>
using namespace std;
int fibfib(int n) {
    if(n <= 1)
        return 0;
    else if(n == 2)
        return 1;
    else {
        int a = 0, b = 0, c = 1;
        for(int i = 3; i <= n; i++) {
            int temp = a + b + c;
            a = b;
            b = c;
            c = temp;
        }
        return c;
    }
}

int main() {
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    printf("The %d-th element of the fibfib number sequence is: %d\n", n, fibfib(n));
    return 0;
}

C:
#include <stdio.h>
#include <stdlib.h>

int fibfib(int n) {
    if(n <= 1)
        return 0;
    else if(n == 2)
        return 1;
    else {
        int *arr = (int*)malloc((n+1)*sizeof(int));
        arr[0] = 0;
        arr[1] = 0;
        arr[2] = 1;
        for(int i = 3; i <= n; i++) {
            arr[i] = arr[i-1] + arr[i-2] + arr[i-3];
        }
        int result = arr[n];
        free(arr);
        return result;
    }
}

int main() {
    int n;
    printf("Enter the value of n: ");
    scanf