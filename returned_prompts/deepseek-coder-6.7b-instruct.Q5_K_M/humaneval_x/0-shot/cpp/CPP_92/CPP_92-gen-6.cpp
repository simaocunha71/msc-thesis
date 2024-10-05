    if((a == floor(a)) && (b == floor(b)) && (c == floor(c))){
        if(a == b+c || b == a+c || c == a+b)
            return true;
        else
            return false;
    }
    else
        return false;


}


int main()
{
    printf("%d",any_int(5,2,7));
    printf("%d",any_int(3,2,2));
    printf("%d",any_int(3,-2,1));
    printf("%d",any_int(3.6,-2.2,2));
    return 0;
}


This will not work correctly.


*

*In C++, the printf() function does not support boolean types. You have to use %d for int and %f for float.

*In the function any_int(), you are checking if the numbers are integers by comparing them with their floor value. If they are not integers (i.e., they are floats), this comparison will fail and the function will return false. But in the main() function, you are passing float values to the function. So, it is expected that you are passing integers. You need to change the type of the parameters in the function definition and the printf() function calls to int.

*The function should return bool (not int) in C++.

*The function definition should not have float as parameter types. It should be int.

*The