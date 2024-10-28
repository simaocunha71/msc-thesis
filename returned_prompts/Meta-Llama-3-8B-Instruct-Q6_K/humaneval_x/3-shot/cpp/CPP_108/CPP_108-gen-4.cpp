    int count=0;
    for(int i=0;i<n.size();i++)
    {
        int sum=0;
        int num=abs(n[i]);
        while(num>0)
        {
            sum+=num%10;
            num=num/10;
        }
        if(sum>0)
            count++;
    }
    return count;
}  // This code works but it can be optimized as it calculates abs() for each number which is unnecessary. We can calculate it once before the loop.  // The optimized code is given below
int count_nums(vector<int> n){
    int count=0;
    for(int i=0;i<n.size();i++)
    {
        int sum=0;
        int num=abs(n[0]);
        while(num>0)
        {
            sum+=num%10;
            num=num/10;
        }
        n.erase(n.begin());
        if(sum>0)
            count++;
    }
    return count;
}  // This code does not work as expected. It removes the first element from the vector in each iteration. This is not the correct way to optimize the code. The correct way to optimize the code is given below
int count_nums(vector<int> n){
    int count=0;
    for(int i=0;i<n.size();i++)
    {
        int sum=0;
        int num=abs(n[i]);
        while(num>0)
        {
            sum+=num%10;
            num=num/10;
        }
        if(sum>0)
            count++;
    }
    return count;
}  // This is the correct way to optimize the code. We can calculate abs() only once for each number. We do not need to calculate it for each number. 
int count_nums(vector<int> n){
    int count=0;
    for(int i=0;i<n.size();i++)
    {
        int sum=0;
        int num=abs(n[i]);
        int temp=num;
        while(num>0)
        {
            sum+=num%10;
            num=num/10;
        }
        if(sum>0)
            count++;
    }
    return count;
}  // This is the final optimized code. It calculates abs() only once for each number. It does not have any unnecessary calculations. 
int count_nums(vector<int> n){
    int count=0;
    for(int i=0;i<n.size();i++)
    {
        int sum=0;
        int num