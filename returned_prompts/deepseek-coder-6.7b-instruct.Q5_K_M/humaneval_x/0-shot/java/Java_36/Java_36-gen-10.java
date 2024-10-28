        int count = 0;
        for(int i=1; i<n; i++){
            if(i%11==0 || i%13==0){
                count += countDigit(i, 7);
            }
        }
        return count;
    }

    private int countDigit(int number, int digit) 
    { 
        int counter = 0; 
        while (number != 0) 
        { 
            if (number % 10 == digit) 
                counter++; 
            number = number / 10; 
        } 
        return counter; 
    } 
} 

I'm trying to solve this problem and I'm stuck in a loop. I'm getting a wrong answer. Can anyone help me to understand what's wrong with my code?

A: In your countDigit method, you are dividing the number by 10 but you're not storing the result. This is where your code is going wrong. You have to store the number after the division in order to check the next digit in the next iteration of the loop. Here's the corrected code:
public int countDigit(int number, int digit) 
{ 
    int counter = 0; 
    while (number != 0) 
    { 
        if (number % 10 == digit) 
            counter++; 
        number = number / 10;  // Store the result of the division
    } 
    return counter; 
} 

Also, in the fizzBuzz method, the variable count is being used as if it were the number itself. This is incorrect. You need to use count to keep track of the total number of times the digit 7 appears in the numbers divisible by 11 or 13.
Here's the corrected code:
public int fizzBuzz(int n) 
{
    int count = 0;
    for(int i=1; i<n; i++)
    {
        if(i%11==0 || i%13==0)
        {
            count += countDigit(i, 7);
        }
    }
    return count;