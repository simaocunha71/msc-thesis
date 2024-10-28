    int a = x[0]-'0';
    int b = n[0]-'0';
    int c = x[2]-'0';
    int d = n[2]-'0';
    int e = x[4]-'0';
    int f = n[4]-'0';
    if(b*f!=c*d) return false;
    if((a*f+c*d)%(b*d)==0) return true;
    return false;
}



ANSWER:
No
*/

In this problem we need to check if the product of two fractions is a whole number. 

Here's how we can solve it:

1. First, we extract the numerator and denominator of each fraction. We can do this by using the substring function to get the numerator and denominator from the given strings. For example, if the fraction is "1/5", we can use the substring function to get the numerator "1" and the denominator "5".

2. Next, we calculate the product of the two fractions. We can do this by multiplying the numerators and the denominators separately, and then dividing the product of the numerators by the product of the denominators. For example, if the fraction is "1/5" and "5/1", we can calculate the product of the numerators as "1*5=5" and the product of the denominators as "5*1=5". Dividing the product of the numerators by the product of the denominators gives us the product of the fractions, which is "5/5=1".

3. Finally, we check if the product of the fractions is a whole number. We can do this by checking if the remainder of the division is zero. If the remainder is zero, then the product is a whole number and we return true. Otherwise, we return false.

Here's a step-by-step breakdown of the code:

1. We extract the numerator and denominator of each fraction using the substring function:
   int a = x[0]-'0';
   int b = n[0]-'0';
   int c = x[2]-'0';