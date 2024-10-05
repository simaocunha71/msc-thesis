    int sum=0;
    int product=1;
    for(int i:numbers)
    {
        sum+=i;
        product*=i;
    }
    return vector<int>{sum,product};
}  // 0 and 1 are not included in sum and product if the vector is empty. This is not in the problem statement. 
vector<int> sum_product(vector<int> numbers)
{
    int sum=0;
    int product=1;
    for(int i:numbers)
    {
        sum+=i;
        product*=i;
    }
    return vector<int>{sum,product};
}
vector<int> sum_product(vector<int> numbers)
{
    int sum=accumulate(numbers.begin(),numbers.end(),0);
    int product=1;
    for(int i:numbers)
    {
        product*=i;
    }
    return vector<int>{sum,product};
}  // This is the correct solution. It uses accumulate function to calculate the sum in a single line.  // It also correctly handles the case when the input vector is empty. 
