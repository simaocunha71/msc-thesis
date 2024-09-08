    int numerator_x = atoi(strtok(x.c_str(),"/"));
    int denominator_x = atoi(strtok(NULL,"/"));
    int numerator_n = atoi(strtok(n.c_str(),"/"));
    int denominator_n = atoi(strtok(NULL,"/"));

    int numerator = numerator_x * denominator_n;
    int denominator = denominator_x * numerator_n;

    if(denominator == 0) {
        return false;
    }
    int gcd = gcd_func(numerator, denominator);

    return ((numerator / gcd) % (denominator / gcd) == 0);

}
int gcd_func(int a, int b) {
    if (b == 0)
        return a;
    return gcd_func(b, a % b);
}
int main() {
    printf("%d\n", simplify("1/5", "5/1")); // true
    printf("%d\n", simplify("1/6", "2/1")); // false
    printf("%d\n", simplify("7/10", "10/2")); // false
    return 0;
}
