    int sum=0;
    for (int i=0;i<lst.size();i++)
    {
        if ((i+1)%3==0)
            sum+=pow(lst[i],2);
        else if ((i+1)%4==0 && (i+1)%3!=0)
            sum+=pow(lst[i],3);
    }
    return sum;
}
// The function pow() is from the cmath library which is included by default in C++. It is used to calculate the power of a number. In this case, it is used to square and cube the numbers in the list. The modulus operator % is used to check if the index i is a multiple of 3 or 4. The sum of all the squared and cubed numbers is then returned.