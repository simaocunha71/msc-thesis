    int integer_part;
    float decimal_part;
    integer_part = floor(number);
    decimal_part = number - integer_part;
    return decimal_part;
}

int main(){
    float number = 3.5;
    float result = truncate_number(number);
    printf("The decimal part is: %f", result);
    return 0;
}

C:
#include <stdio.h>
#include <math.h>

float truncate_number(float number) {
    int integer_part;
    float decimal_part;

    integer_part = floor(number);
    decimal_part = number - integer_part;

    return decimal_part;
}

int main() {
    float number = 3.5;
    float result = truncate_number(number);
    printf("The decimal part is: %f\n", result);
    return 0;
}
C++:
#include <iostream>
#include <cmath>

float truncate_number(float number) {
    int integer_part;
    float decimal_part;

    integer_part = std::floor(number);
    decimal_part = number - integer_part;

    return decimal_part;
}

int main() {
    float number = 3.5;
    float result = truncate_number(number);
    std::cout << "The decimal part is: " << result << std::endl;
    return 0;
}

Python:
def truncate_number(number):
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part

number = 3.5
result = truncate_number(number)
print("The decimal part is:", result)

Java:
public class Main {
    public static float truncateNumber(float number) {
        int integerPart;
        float decimalPart;

        integerPart = (int) Math.floor(number);
        decimalPart = number - integerPart;

        return decimalPart;
    }

    public static void main(String[] args) {
        float number = 3.5f;
        float result = truncateNumber(number);
        System.out.println("The decimal part is: " + result);
    }
}
C#:
using System;

public class Program {
    public static float TruncateNumber(float number) {
        int integerPart;
        float decimalPart;

        integerPart = (int)Math.Floor(number);
        decimalPart = number - integerPart;

        return decimalPart;
    }

    public static void Main(string[] args) {
        float number = 3.5f;
        float result = TruncateNumber(number);
        Console.WriteLine("The decimal part is: " + result);
    }
}

Go