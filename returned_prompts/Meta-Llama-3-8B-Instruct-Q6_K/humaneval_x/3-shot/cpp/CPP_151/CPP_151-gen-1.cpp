    long long sum=0;
    for (float num:lst)
    {
        if (num>0 && floor(num)==num)//num is positive and integer
        {
            sum += pow(num,2);
        }
    }
    return sum;
}#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
long long double_the_difference(vector<float> lst){
    long long sum=0;
    for (float num:lst)
    {
        if (num>0 && floor(num)==num)//num is positive and integer
        {
            if (num%2!=0)//num is odd
            {
                sum += pow(num,2);
            }
        }
    }
    return sum;
}
