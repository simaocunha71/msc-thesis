    int numerator_x =stoi(x.substr(0,x.find('/')));
    int denominator_x =stoi(x.substr(x.find('/')+1));
    int numerator_n =stoi(n.substr(0,n.find('/')));
    int denominator_n =stoi(n.substr(n.find('/')+1));
    
    int numerator = numerator_x * denominator_n;
    int denominator = denominator_x * numerator_n;
    
    if(gcd(numerator,denominator) > 1)
        return false;
    else
        return true;
}

int gcd(int a, int b) {
    if (b == 0)
        return a;
    else
        return gcd(b, a % b);
} 
//gcd is a function to find the greatest common divisor of two numbers. It is implemented using Euclidean algorithm.
//This function is used to check if the simplified fraction is a whole number or not. If gcd is greater than 1, the fraction is not a whole number, so the function returns false. Otherwise, it returns true. 
