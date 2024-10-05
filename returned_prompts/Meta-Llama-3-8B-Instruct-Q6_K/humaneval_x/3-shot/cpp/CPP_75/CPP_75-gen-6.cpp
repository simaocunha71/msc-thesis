    bool flag=true;
    int i,prime_count=0;
    for (i=2;i<=a;i++)
    {
        if (a%i==0)
        {
            int count=0;
            for (int j=2;j<=i/2;j++)
            {
                if (i%j==0)
                count++;
            }
            if (count==0)
            {
                prime_count++;
                if (prime_count>3)
                {
                    flag=false;
                    break;
                }
            }
        }
    }
    return flag;
}  // This function is not efficient because it has to check each number from 2 to a. It could be improved by checking only numbers up to the square root of a.  // It's also not clear how to handle the case where a is a prime number itself.  // It would be better to check if a is divisible by any of the numbers from 2 to sqrt(a) and check if the divisor is a prime number.  // We can also use a function to check if a number is prime.  // Here is the improved version of the function:  //  bool is_multiply_prime(int a)  //  {  //      for (int i=2; i<=sqrt(a); i++)  //      {  //          if (a%i==0)  //          {  //              if (is_prime(i))  //              {  //                  int b=a/i;  //                  if (is_prime(b))  //                  {  //                      int c=a/(i*b);  //                      if (is_prime(c))  //                      {  //                          return true;  //                      }  //                  }  //              }  //          }  //      }  //      return false;  //  }  //  bool is_prime(int a)  //  {  //      if (a<2)  //          return false;  //      for (int i=2; i<=sqrt(a); i++)  //      {  //          if (a%i==0)  //              return false;  //      }  //      return true;  //  }  //  #include <cmath>  //  #include <iostream>  //  using namespace std;  //  bool is_multiply_prime(int a)  //  {  //      for (int i=2; i<=sqrt(a); i++)  //      {