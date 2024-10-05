    return 0.5;
}

int main(){
    float number;
    float result;
    printf("Enter a positive floating point number:\n");
    scanf("%f", &number);
    result = truncate_number(number);
    printf("The decimal part of the number is: %f\n", result);
    return 0;
}

