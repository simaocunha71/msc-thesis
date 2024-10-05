    if(a%b==0)
        return b;
    else
        a=b;
        goto A;
}

int main(){
    printf("greatest common divisor of 3 and 5 is %d\n", greatest_common_divisor(3, 5));
    printf("greatest common divisor of 25 and 15 is %d\n", greatest_common_divisor(25, 15));
    return 0;
}
