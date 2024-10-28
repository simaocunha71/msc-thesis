float integer = (int)number;
float decimals = number - integer;
float result;
if(decimals > 0){
    while(decimals > 0 && decimals < 1){
        decimals *= 10;
        integer++;
    }
    result = decimals - (int)decimals;
}
else{
    result = 0;
}
return result;
}
int main()
{
    float number;
    scanf("%f", &number);
    printf("%.1f", truncate_number(number));
    return 0;
}
