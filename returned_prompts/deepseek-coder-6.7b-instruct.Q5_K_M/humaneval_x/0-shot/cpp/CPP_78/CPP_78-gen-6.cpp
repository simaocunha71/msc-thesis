/*
We convert each hexadecimal digit to decimal and check if it's prime or not.
If it is, we increment the count.
*/

    int count = 0;
    int len = num.size();
    int dec;
    for(int i=0; i<len; i++){
        if(isdigit(num[i]))
            dec = num[i] - '0';
        else
            dec = 10 + num[i] - 'A';
        if(dec == 2 || dec == 3 || dec == 5 || dec == 7 || dec == 11 || dec == 13 || dec == 17)
            count++;
    }
    return count;
}
int main()
{
    string num;
    printf("Enter a hexadecimal number: ");
    cin >> num;
    int count = hex_key(num);
    printf("The number of hexadecimal digits that are primes: %d\n", count);
    return 0;
}

*/

/*
In the above code, we first declare an integer "count" to hold the number of 
prime hexadecimal digits. We then convert each hexadecimal digit to decimal 
and check if it's prime or not. If it is, we increment the count. Finally, 
we return the count.
*/

// 