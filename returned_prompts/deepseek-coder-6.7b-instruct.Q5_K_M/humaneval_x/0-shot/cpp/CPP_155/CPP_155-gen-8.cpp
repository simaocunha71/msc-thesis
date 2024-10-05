    int even = 0, odd = 0;
    num = abs(num);
    while(num){
        if((num%10)%2 == 0)
            even++;
        else
            odd++;
        num = num/10;
    }
    return vector<int>{even, odd};
}
*/

// The above function is a C++ solution for the problem. In the function, we are first initializing the counters for even and odd digits to 0. 
// We then take the absolute value