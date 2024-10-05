    int max_prime=0;
    int sum=0;
    for (int i=0;i<lst.size();i++)
    {
        int num=lst[i];
        if (is_prime(num))
        {
            max_prime=num;
            sum=0;
            while (num>0)
            {
                sum+=num%10;
                num=num/10;
            }
        }
    }
    return sum;
}

bool is_prime(int num)
{
    if (num < 2) return false;
    for (int i = 2; i*i <= num; i++) {
        if (num % i == 0) return false;
    }
    return true;
}  // This function checks if a number is prime or not. It's used in the main function above.  // End of function is_prime().  // End of function skjkasdkd().  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of file.  // End of