    if(n>m) return "-1";
    double avg = (double)(n+m)/2;
    int res = round(avg);
    string s = bitset<8>(res).to_string();
    while(s.length()<8) s = '0'+s;
    return s;
}

int main(){
    printf("%s\n",rounded_avg(1,5).c_str());
    printf("%s\n",rounded_avg(7,5).c_str());
    printf("%s\n",rounded_avg(10,20).c_str());
    printf("%s\n",rounded_avg(20,33).c_str());
    return 0;
}


ANSWER:
/*
11
-1
1111
11010
*/

EXPLANATION:
1. 1+5/2=3, round to nearest smaller integer, 3
2. 7+5/2=6, round to nearest smaller integer, -1
3. 10+20/2=15, round to nearest smaller integer, 11
4. 20+33/2=26.5, round to nearest smaller integer, 110

*/

*/

```
Here is how you can solve this problem programatically:

Step 1: Calculate the average of the two numbers. You can do this by adding the two numbers together and dividing the sum by 2. Since the average is a decimal, round the result down to the nearest whole number using the `round()` function. This will give you the average as an integer.

Step 2: Convert the integer average to a binary string. You can do this by using the `bitset` class from the `<bitset>` library. The `bitset` class allows you to represent an integer as a binary string. To convert the integer to a binary string, you can use the `to_string()` function. However, since the binary string may be shorter than 8 characters, you need to add leading zeros to make it 8 characters long. You can do this by concatenating a string of "0" with