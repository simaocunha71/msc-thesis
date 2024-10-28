    return 0.0;
}
int main(){
    float number;
    printf("Enter a positive floating point number: ");
    scanf("%f", &number);
    printf("The decimal part of the number is: %f", truncate_number(number));
    return 0;
}

