    int value_int = atoi(value.c_str());
    if (value_int > 0)
    {
        if (value_int % 2 != 0)
        {
            if ((value_int + 1) % 2 == 0)
            {
                value_int++;
            }
        }
        else if ((value_int + 1) % 2 != 0)
        {
            value_int++;
        }
    }
    else if (value_int < 0)
    {
        if (value_int % 2 != 0)
        {
            if ((value_int - 1) % 2 == 0)
            {
                value_int--;
            }
        }
        else if ((value_int - 1) % 2 != 0)
        {
            value_int--;
        }
    }
    return value_int;
}



*/




/*
The function should return the closest integer to the given number,
considering both positive and negative numbers.

Examples
>>> closest_integer("1.3")
1
>>> closest_integer("-1.3")
-2

Note:
If the given number is equidistant from two integers, round it away from zero.
For example closest_integer("1.5") should return 2 and closest_integer("-1.5") should return -2.
*/


/*
The function should return the closest integer to the given number,
considering both positive and negative numbers.

Examples
>>> closest_integer("1.3")
1
>>> closest_integer("-1.3")
-2

Note:
If the given number is equidistant from two integers, round it away from zero.
For example closest_integer("1.5") should return 2 and closest_integer("-1.5") should return -2.
*/







int main(void){
    string value = "1.3";
    int result = closest_integer(value);
    printf("%d\n",result);
    return 0;
}







