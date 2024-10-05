    if(b == 0){
        return a;
    }
    return greatest_common_divisor(b, a % b);
}

int main(){
    int a, b;
    printf("Enter two integers: ");
    scanf("%d %d", &a, &b);
    printf("GCD of %d and %d is %d", a, b, greatest_common_divisor(a, b));
    return 0;
}
*/

