    float decimal = modf(number, &number);
    return decimal;
}
int main() {
    float num = 3.5;
    float result = truncate_number(num);
    printf("%.2f\n", result);
    return 0;
}
