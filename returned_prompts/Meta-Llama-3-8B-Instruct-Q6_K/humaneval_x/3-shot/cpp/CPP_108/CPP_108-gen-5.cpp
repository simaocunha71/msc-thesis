    int count=0;
    int num;
    int i;
    for (i=0;i<n.size();i++)
    {
        num=n[i];
        int sum=0;
        int is_negative=0;
        if (num<0)
        {
            is_negative=1;
            num=-num;
        }
        while (num>0)
        {
            int digit=num%10;
            sum+=digit;
            num=num/10;
        }
        if (sum>0)
        {
            count++;
        }
    }
    return count;
} // This solution is not efficient as it converts each number to string, then sums the digits. It can be improved by performing the sum of digits directly without converting the number to string. The time complexity of this solution is O(n*m) where n is the size of the input vector and m is the maximum number of digits in a number. It can be improved to O(n) by directly summing the digits without converting the number to string.
} // It can be further improved by using the property that the sum of digits of a number is equal to the sum of the digits of the number divided by 10. This can be achieved by using a while loop to keep dividing the number by 10 and summing the remainder until the number becomes 0. The time complexity of this improved solution is O(n).