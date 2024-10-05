    double log_base = log((double)x) / log((double)n);
    return (abs(log_base - round(log_base)) < 1e-9);
}
// or
bool is_simple_power(int x,int n){
    double log_base = log((double)x) / log((double)n);
    return round(log_base) == log_base;
}
// or
bool is_simple_power(int x,int n){
    int power = (int)log((double)x) / log((double)n);
    return pow(n, power) == x;
}
// or
bool is_simple_power(int x,int n){
    double power = pow(n, ceil(log((double)x) / log((double)n)));
    return power == x;
}  // this one is not correct
// or
bool is_simple_power(int x,int n){
    double power = pow(n, floor(log((double)x) / log((double)n)));
    return power == x;
}
// or
bool is_simple_power(int x,int n){
    double power = pow(n, round(log((double)x) / log((double)n)));
    return power == x;
}  // this one is not correct

// The above solutions are not correct, because the problem statement does not specify whether the 
// power must be an integer or not. The solution should be able to handle non-integer powers.

// The correct solution is:
bool is_simple_power(int x,int n){
    if (x <= 0 || n <= 0)
        return false;

    double base = pow(n, 1.0 / log(n) * log(x));
    return base == x;
}

// This function first checks if the input numbers are positive. If not, it immediately returns false.
// Then it calculates the base of the power using the property of logarithms. Finally, it checks if the calculated base is equal to the input number. If it is, the function returns true; otherwise, it returns false. This function can handle non-integer powers.  // This function can handle non-integer powers.