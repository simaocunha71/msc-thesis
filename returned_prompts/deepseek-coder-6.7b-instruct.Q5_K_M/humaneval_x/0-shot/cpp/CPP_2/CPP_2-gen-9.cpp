    float intpart, fracpart;
    fracpart = modf(number, &intpart);
    return fracpart;
}

int main(){

B:
    float number;
    printf("Enter a positive floating point number: ");
    scanf("%f", &number);
    printf("Decimal part of the number is: %f\n", truncate_number(number));
    return 0;
}
*/

int main(void) {

    float number;
    printf("Enter a positive floating point number: ");
    scanf("%f", &number);
    printf("Decimal part of the number is: %f\n", truncate_number(number));
    return 0;
}
/*
C:
float truncate_number(float number){
    return number - (int)number;
}
*/

/*
D:
float truncate_number(float number){
    return number - floor(number);
}
*/

/*
E:
float truncate_number(float number){
    return number - (int)number;
}
*/

/*
F:
float truncate_number(float number){
    return number - floor(number);
}
*/

/*
G:
float truncate_number(float number){
    return number - floor(number);
}
*/

/*
H:
float truncate_number(float number){
    return number - (int)number;
}
*/

/*
I:
float truncate_number(float number){
    return number - floor(number);
}
*/

/*
J:
float truncate_number(float number){
    return number - (int)number;
}
*/

/*
K:
float truncate_number(float number){
    return number - floor(number);
}
*/

/*
L:
float truncate_number(float number){
    return number - (int)number;
}
*/

/*
M:
float truncate_number(float number){
    return number - floor(number);
}
*/

/*
N:
float truncate_number(float number){
   