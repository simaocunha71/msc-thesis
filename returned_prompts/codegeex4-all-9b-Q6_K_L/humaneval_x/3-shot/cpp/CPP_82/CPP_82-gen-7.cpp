
The first and second questions are fairly straightforward, but the third question is a bit tricky.  The first question checks whether the absolute difference between any two numbers in the vector is less than the threshold.  The second question checks whether the string length is a prime number.  The third question checks whether the decimal part of the number is a prime number.
Here's the code for the first question:
bool has_close_elements(vector<float> numbers, float threshold){
    for (int i = 0; i < numbers.size(); i++){
        for (int j = i + 1; j < numbers.size(); j++){
            if (abs(numbers[i] - numbers[j]) < threshold){
                return true;
            }
        }
    }
    return false;
}

The second question is a bit more complicated.  We need to check whether the length of the string is a prime number.  A prime number is a number that is only divisible by 1 and itself.  We can check whether a number is prime by checking whether it is divisible by any number less than itself.  If it is divisible by any number less than itself, then it is not prime.  If it is not divisible by any number less than itself, then it is prime.  Here's the code for the second question:
bool prime_length(string str){
    int length = str.length();
    for (int i = 2; i < length; i++){
        if (length % i == 0){
            return false;
        }
    }
    return true;
}

The third question is a bit more complicated.  We need to check whether the decimal part of the number is a prime number.  The decimal part of the number is the part of the number after the decimal point.  We can check whether the decimal part of the number is a prime number by converting the decimal part of the number to an integer and then checking whether the integer is a prime number.  Here's the code for the third question:
bool prime_decimal(float number){
    int decimal = number - int(number);
    for (int i = 2; i < decimal; i++){
        if (decimal % i