    return fmodf(number, 1.0);
}

int main(){
    float num = 3.5;
    printf("%f", truncate_number(num));
    return 0;
}

The function fmodf takes two arguments, the first one is the number to be decomposed, and the second one is the divisor (1.0 in this case). It returns the leftover part (decimals) of the number.

When the number is 3.5, the integer part is 3 and the decimal part is 0.5. So, fmodf(3.5, 1.0) will return 0.5.
*/

