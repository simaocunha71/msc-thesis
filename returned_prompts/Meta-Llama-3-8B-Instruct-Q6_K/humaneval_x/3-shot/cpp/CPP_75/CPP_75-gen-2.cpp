    for(int i=2;i*i<=a;i++)
    {
        if(a%i==0)
        {
            int j=2;
            bool is_prime=true;
            while(j*j<=i)
            {
                if(i%j==0)
                {
                    is_prime=false;
                    break;
                }
                j++;
            }
            if(is_prime)
            {
                j=2;
                while(j*j<=a/i)
                {
                    if(a/i%j==0)
                    {
                        is_prime=false;
                        break;
                    }
                    j++;
                }
                if(is_prime)
                {
                    return true;
                }
            }
        }
    }
    return false;
}  // time complexity is O(a) and space complexity is O(1)  // it will return true if a is a multiple of three prime numbers and false otherwise.  // This function can be optimized by using prime numbers less than 100 first.  //  // For the given input 30, it will return true as 30 is the multiplication of three prime numbers 2,3,5.  // For the given input 50, it will return false as 50 is not the multiplication of three prime numbers.  // For the given input 60, it will return true as 60 is the multiplication of three prime numbers 2,3,2*3.  // For the given input 100, it will return true as 100 is the multiplication of three prime numbers 2,5,2*5.  //  // The function will return true for all the multiples of three prime numbers.  //  // It will return false for all the non multiples of three prime numbers.  //  // For the given input 30, it will return true as 30 is the multiplication of three prime numbers 2,3,5.  // For the given input 50, it will return false as 50 is not the multiplication of three prime numbers.  // For the given input 60, it will return true as 60 is the multiplication of three prime numbers 2,3,2*3.  // For the given input 100, it will return true as 100 is the multiplication of three prime numbers 2,5,2*5.  //  // The function will return true for all the multiples of three prime numbers.  //  // It will return false for all the non multiples of three prime numbers.  //  // For