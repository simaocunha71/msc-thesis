    float result = fmod(number,1);
    float result1 = (int)number;
    if(result1 == number)
        return result;
    else
        number = result1;
    goto A;
}

int main(){
    float a;
    scanf("%f",&a);
    printf("%f",truncate_number(a));
}

