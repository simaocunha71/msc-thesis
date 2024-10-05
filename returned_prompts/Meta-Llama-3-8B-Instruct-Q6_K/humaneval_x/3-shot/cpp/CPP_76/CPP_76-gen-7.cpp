    double y=pow(n,round(log(x)/log(n)));
    return y==x;
}
//This function checks if x is a simple power of n.
//First, it calculates the power of n that is closest to x.
//Then it checks if this power is equal to x.
//If it is, the function returns true, otherwise it returns false.
//The use of double instead of int is necessary because log(x)/log(n) may not be an integer.
//For example, log(8)/log(2) is 3.0, not 3. This is why we use round() to get the closest integer.
//Also, the use of pow() with double argument is necessary because the result of log(x)/log(n) may not be an integer.
//For example, pow(2,3.0) is 8.0, not 8. This is why we use round() to get the closest integer.
//This function uses the properties of logarithms to calculate the power of n that is closest to x.
//It then checks if this power is equal to x.
//If it is, the function returns true, otherwise it returns false.