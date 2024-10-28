    if(n<=3) return n>1;
    if(n%2==0) return false;
    if(n%3==0) return false;
    for(long long i=5;i*i<=n;i+=6){
        if(n%i==0) return false;
        if(n%(i+2)==0) return false;
    }
    return true;
}


/*
Return the sum of the digits in a given number.
>>> sum_digits(123)
6
>>> sum_digits(42)
6
>>> sum_digits(210)
3
>>> sum_digits(1201)
4
>>> sum_digits(102)
3
*/
int sum_digits(int n){
    int sum = 0;
    while(n>0){
        sum += n%10;
        n /= 10;
    }
    return sum;
}

/*
Return true if a given number is a power of two, otherwise return false.
>>> is_power_of_two(1)
true
>>> is_power_of_two(2)
true
>>> is_power_of_two(4)
true
>>> is_power_of_two(16)
true
>>> is_power_of_two(256)
true
>>> is_power_of_two(5)
false
>>> is_power_of_two(25)
false
*/
bool is_power_of_two(int n){
    while(n%2==0){
        n /= 2;
    }
    return n==1;
}

/*
Return the decimal representation of a given binary number.
>>> bin_to_dec(101)
5
>>> bin_to_dec(11010)
26
>>> bin_to_dec(10010010)
130
>>> bin_to_dec(1111)
15
>>> bin_to_dec(0)
0
*/
int bin_to_dec(int n){
   