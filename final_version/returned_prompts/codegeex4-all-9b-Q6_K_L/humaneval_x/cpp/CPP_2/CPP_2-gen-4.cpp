    int a=(int)number;
    float b=number-a;
    printf("%f\n",b);
    return b;
}

int main(){
    float x;
    scanf("%f",&x);
    truncate_number(x);
    return 0;
}