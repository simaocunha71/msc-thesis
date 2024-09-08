    float decimals = 0;
    decimals = number - floor(number);
    return decimals;
}
int main(){
    float number;
    scanf("%f",&number);
    printf("%f",truncate_number(number));
    return 0;
}
