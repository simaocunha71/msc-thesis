
The first function has a logical error: it checks if two numbers are within the threshold of each other, but it doesn't check if the numbers are different (so it will always return true if the vector has 1 or 0 numbers). You should add a check that i != j. Like this:
bool has_close_elements(vector<float> numbers, float threshold){
    for (int i=0;i<numbers.size();i++)
        for (int j=i+1;j<numbers.size();j++)
            if (abs(numbers[i]-numbers[j])<threshold && i != j)
                return true;
    return false;
}

The second function is fine.

For the third one, there's no need to subtract the integer part from the number. You can use the modulo operator (%) to get the decimal part of the number. Like this:
float truncate_number(float number){
    return number - (int)number;
}

For the last one, you are calculating the numbers that start with 1, and then the numbers that end with 1. But you are missing the numbers that start and end with 1. You should add 1 to the result. Like this:
int starts_one_ends(int n){
    if (n==1) return 1;
    if (n==2) return 3;
    return 2*starts_one_ends(n-1)+3+1;
}