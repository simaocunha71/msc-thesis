    int unitA = a % 10;
    int unitB = b % 10;
    return (unitA * unitB);
}

int main() {
    printf("%d\n", multiply(148, 412));
    printf("%d\n", multiply(19, 28));
    printf("%d\n", multiply(2020, 1851));
    printf("%d\n", multiply(14,-15));
    return 0;
}
