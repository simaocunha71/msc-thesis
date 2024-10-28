    if (b==0)
        return a;
    else
        return greatest_common_divisor(b, a%b);

}
int main(){
    int a, b;
    printf("Enter two integers: ");
    scanf("%d %d", &a, &b);
    printf("Greatest common divisor is: %d", greatest_common_divisor(a, b));
    return 0;
}

//C++ program to calculate the greatest common divisor of two integers using the Euclidean algorithm
//The Euclidean algorithm is a method of computing the greatest common divisor of two integers, the largest number that divides both of them without leaving a remainder.
//The algorithm is based on the principle that the greatest common divisor of two numbers does not change if the larger number is replaced by its difference with the smaller number.
