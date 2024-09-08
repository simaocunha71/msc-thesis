    int integer_part = (int)number;
    float decimal_part = number - integer_part;
    return decimal_part;

}
int main()
{
    float num = 3.5;
    printf("%f\n",truncate_number(num));
    return 0;
}

