    if(x<=0)
        return false;
    int base = (int)pow(n, (int)log(x) / log(n));
    if(base * n == x)
        return true;
    else
        return false;
}

int main()
{
    printf("%d\n", is_simple_power(1, 4));
    printf("%d\n", is_simple_power(2, 2));
    printf("%d\n", is_simple_power(8, 2));
    printf("%d\n", is_simple_power(3, 2));
    printf("%d\n", is_simple_power(3, 1));
    printf("%d\n", is_simple_power(5, 3));
    return 0;
}
//test cases
//1: is_simple_power(1, 4) => true
//2: is_simple_power(2, 2) => true
//3: is_simple_power(8, 2) => true
//4: is_simple_power(3, 2) => false
//5: is_simple_power(3, 1) => false
//6: is_simple_power(5, 3) => false
//7: is_simple_power(64, 4) => true
//8: is_simple_power(81, 3) => true
//9: is_simple_power(100, 10) => true
//10: is_simple_power(12, 2) => false
//11: is_simple_power(9, 3) => true
//12: is_simple_power(25, 5) => true
//13: is_simple_power(16, 4) => true
//14: is_simple_power(36, 6) => true
//15: is_simple_power(49, 7) => true
//16: is_simple_power(64, 8) => true
//17: is_simple_power(1, 1) => true
//18: is_simple_power(0, 2) => false
//19: is_simple_power(2, 1) => false
//20: is_simple_power(1, 0) => false
//21: is_simple_power(1, 3) => false
//22: is_simple_power(2, 3) => false
//23: is_simple_power(3, 3) => false
//24: is_simple_power(4, 2) =>