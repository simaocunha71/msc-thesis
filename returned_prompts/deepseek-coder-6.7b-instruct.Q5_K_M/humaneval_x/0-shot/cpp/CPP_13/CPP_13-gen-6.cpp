    while(b){
        int t = b;
        b = a % b;
        a = t;
    }
    return a;
}

int main(){
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d", greatest_common_divisor(a, b));
    return 0;
}

This code finds the greatest common divisor of two integers a and b by using Euclid's algorithm.

The algorithm is as follows:

1. Divide the bigger number by the smaller number, and take the remainder.
2. Replace the larger number with the smaller number and the smaller number with the remainder.
3. Repeat the process until the remainder is zero.
4. The last non-zero remainder is the greatest common divisor.
*/

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d", greatest_common_divisor(a, b));
    return 0;
}

This code finds the greatest common divisor of two integers a and b by using Euclid's algorithm.

The algorithm is as follows:

1. Divide the bigger number by the smaller number, and take the remainder.
2. Replace the larger number with the smaller number and the smaller number with the remainder.
3. Repeat the process until the remainder is zero.
4. The last non-zero remainder is the greatest common divisor.
*/

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d", greatest_common_divisor(a, b));
    return 0;
}

The code first takes two integers a and b as input. Then it prints the greatest common divisor of a and b using the greatest_common_divisor function.

The greatest_common_divisor function uses Euclid's algorithm to find the greatest common divisor of a and b. The algorithm is as follows:

1. Divide the bigger number by the smaller number, and take the remainder.
2. Replace the larger number with the smaller number and the smaller number with the remainder.
3