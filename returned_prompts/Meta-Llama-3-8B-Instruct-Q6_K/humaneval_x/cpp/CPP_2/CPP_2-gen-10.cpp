    int int_part;
    float dec_part;
    int_part = (int)number;
    dec_part = number - int_part;
    return dec_part;
}

int main()
{
    float num = 3.5;
    float result = truncate_number(num);
    printf("Decimal part: %f\n",result);
    return 0;
}

B:
    float truncate_number(float number) {
        return number - floor(number);
    }

C:
    float truncate_number(float number) {
        return number - (int)number;
    }

D:
    float truncate_number(float number) {
        int int_part = (int)number;
        return number - int_part;
    }
Answer: C:
Explanation: The most straightforward way to get the decimal part of a number is to subtract the integer part from the number. The integer part can be obtained by casting the number to an integer. So, the solution is to subtract the integer part from the number. In C, the cast to integer is done using the (int) operator.
The code in option C:
```c
float truncate_number(float number) {
    float dec_part;
    float int_part = (int)number;
    dec_part = number - int_part;
    return dec_part;
}
```
is correct and will give the expected result. The code in options A and D are also correct but they are more verbose than option C. Option B is not correct because it uses the floor function which is not the same as the integer part. It will truncate the number to the nearest integer, not just remove the integer part.