    int count = 0;
    for(int i=0;i<n.size();i++){
        int sum = 0;
        int temp = n[i];
        while(temp > 0){
            sum += temp%10;
            temp /= 10;
        }
        if(sum > 0) count++;
    }
    return count;
}

/*
Write a function called digits which takes a number as an argument and returns a
vector of the digits of that number in ascending order.
For example, digits(123) returns the vector [1, 2, 3].
>>> digits(0) == []
>>> digits(123) == [1, 2, 3]
>>> digits(100) == [1, 0]
*/
vector<int> digits(int n){
    vector<int> digits;
    while(n > 0){
        digits.push_back(n%10);
        n /= 10;
    }
    return digits;
}

/*
Write a function called sum_digits which takes a vector of integers as an argument and
returns the sum of all of the digits in the vector. For example, sum_digits([1, 2, 3]) returns 6.
>>> sum_digits([]) == 0
>>> sum_digits([1, 2, 3]) == 6
>>> sum_digits([1, 0, 1, 0]) == 2
*/
int sum_digits(vector<int> dig){
    int sum = 0;
    for(int i=0;i<dig.size();i++)
        sum += dig[i];
    return sum;
}

/*
Write a function called sum_vector which takes a vector of integers as an argument and returns the sum of all the integers in the vector.
For example, sum_vector([1, 2, 3]) returns 6.
>>> sum_vector([]) == 0
>>> sum_vector([1, 2, 3]) == 6
>>> sum_vector([1, 0,