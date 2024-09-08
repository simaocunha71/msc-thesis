    int integer_part = (int)number; // convert the float to int
    float decimal_part = number - integer_part; // calculate the decimal part
    return decimal_part; // return the decimal part

}

int main() {
    float number = 3.5;
    float decimal_part = truncate_number(number);
    printf("The decimal part of the number is %f\n", decimal_part);
    return 0;
}

