    int count=0;
    for(int i=0; i<num.length(); i++)
    {
        if(num[i]>='2' && num[i]<='9') continue;
        if(num[i]>='A' && num[i]<='F') count++;
    }
    return count;
}  // function to count the number of hexadecimal digits that are primes
// The function counts the number of hexadecimal digits that are primes. It iterates through the string 
// and checks each character. If the character is a digit '2', '3', '5', '7', 'B', 'D', 'F' (or their 
// corresponding decimal numbers 2, 3, 5, 7, 11, 13, 17), it increments the count. The function returns 
// the count.