    return number - (int)number;
}

int main(){
    float number;
    printf("Enter a floating point number: ");
    scanf("%f", &number);
    printf("The decimal part of the number is: %f", truncate_number(number));
    return 0;
}