    if (n < 8)
        return false;
    if (n % 2 == 0)
        return true;
    if (n % 4 != 0)
        return false;
    if (is_equal_to_sum_even(n / 4))
        return true;
    return false;
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%s\n", is_equal_to_sum_even(n) ? "true" : "false");
    return 0;
}





*/


/*












*/



































































































