    if(n == 0){
        return 0;
    }
    if(n == 1){
        return 0;
    }
    if(n == 2){
        return 2;
    }
    if(n == 3){
        return 0;
    }

B:
    int fib_3 = 0;
    int fib_2 = 2;
    int fib_1 = 0;
    int fib_0 = 0;
    int fib_n = 0;

C:
    for(int i = 4; i <= n; i++){
        fib_n = fib_1 + fib_2 + fib_3 + fib_0;
        fib_0 = fib_1;
        fib_1 = fib_2;
        fib_2 = fib_3;
        fib_3 = fib_n;
    }

D:
    return fib_n;
}
int main() {
    printf("%d\n", fib4(5));
    printf("%d\n", fib4(6));
    printf("%d\n", fib4(7));
    return 0;
}
*/

*/

//