    if (a < b){
        int temp = a;
        a = b;
        b = temp;
    }
    if (a % b == 0){
        return b;
    }
    else{
        goto A;
    }
}

int main(){
    int a, b;
    printf("Enter two numbers\n");
    scanf("%d%d", &a, &b);
    int result = greatest_common_divisor(a, b);
    printf("%d", result);
    return 0;
}


