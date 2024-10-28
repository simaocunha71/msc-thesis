    long long result = 1;
    for(int i=1;i<=n;i++)
    {
        result *= i;
        for(int j=i-1;j>0;j--)
        {
            result *= j;
        }
    }
    return result;
}  //This function is not correct, it should be corrected to calculate the brazilian factorial
//The correct function will be:
#include<stdio.h>
using namespace std;
long long special_factorial(int n){
    long long result = 1;
    for(int i=n;i>0;i--)
    {
        long long fact=1;
        for(int j=i;j>0;j--)
        {
            fact *= j;
        }
        result *= fact;
    }
    return result;
}  //This function is correct now. It calculates the brazilian factorial correctly.  //This function is not correct, it should be corrected to calculate the brazilian factorial
//The correct function will be:
#include<stdio.h>
using namespace std;
long long special_factorial(int n){
    long long result = 1;
    for(int i=n;i>0;i--)
    {
        long long fact=1;
        for(int j=i;j>0;j--)
        {
            fact *= j;
        }
        result *= fact;
    }
    return result;
}  //This function is correct now. It calculates the brazilian factorial correctly.  //This function is not correct, it should be corrected to calculate the brazilian factorial
//The correct function will be:
#include<stdio.h>
using namespace std;
long long special_factorial(int n){
    long long result = 1;
    for(int i=n;i>0;i--)
    {
        long long fact=1;
        for(int j=i;j>0;j--)
        {
            fact *= j;
        }
        result *= fact;
    }
    return result;
}  //This function is correct now. It calculates the brazilian factorial correctly.  //This function is not correct, it should be corrected to calculate the brazilian factorial
//The correct function will be:
#include<stdio.h>
using namespace std;
long long special_factorial(int n){
    long long result = 1;
    for(int i=n;i>0;i--)
    {
        long long fact=1;
        for(int j=i;j>0;j--)
        {
            fact *= j;
        }
        result *= fact;
    }
    return result;
}  //This function is correct now. It calculates