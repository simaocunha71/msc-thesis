    double num = stod(value);
    return (int)round(num);
}



int main(){
    printf("%d\n", closest_integer("10"));
    printf("%d\n", closest_integer("15.3"));
    printf("%d\n", closest_integer("14.5"));
    printf("%d\n", closest_integer("-14.5"));
    return 0;
}



R:

This program will convert a string to double and then round it to the nearest integer. If the number is equidistant between two integers, it will round it away from zero.

The closest_integer function will return the closest integer to the given string number. 

The main function will test the closest_integer function by passing in different string numbers and print out the returned integer.

*/

// Code:

/*

