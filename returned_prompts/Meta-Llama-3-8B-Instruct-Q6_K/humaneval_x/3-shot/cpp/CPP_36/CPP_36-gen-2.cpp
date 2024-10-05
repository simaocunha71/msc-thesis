    int count=0;
    for (int i=1;i<n;i++)
    {
        if ((i%11==0)||(i%13==0))
        {
            int num=i;
            while (num>0)
            {
                if (num%10==7)
                {
                    count++;
                }
                num=num/10;
            }
        }
    }
    return count;
}
// or
int fizz_buzz(int n){
    int count=0;
    for (int i=1;i<n;i++)
    {
        if ((i%11==0)||(i%13==0))
        {
            string str=to_string(i);
            count+=count_if(str.begin(), str.end(), [](char c){ return c == '7'; });
        }
    }
    return count;
}  // using stl's count_if function. 
// or
int fizz_buzz(int n){
    int count=0;
    for (int i=1;i<n;i++)
    {
        if ((i%11==0)||(i%13==0))
        {
            count+=count_seven(i);
        }
    }
    return count;
}  // defining a separate function to count 7's. 

int count_seven(int num)
{
    int count=0;
    while (num>0)
    {
        if (num%10==7)
        {
            count++;
        }
        num=num/10;
    }
    return count;
} 
// or 
int fizz_buzz(int n){
    int count=0;
    for (int i=1;i<n;i++)
    {
        if ((i%11==0)||(i%13==0))
        {
            string str=to_string(i);
            count+=count_seven(str);
        }
    }
    return count;
}  // defining a separate function to count 7's in a string. 
int count_seven(string str)
{
    int count=0;
    for (char c : str)
    {
        if (c == '7')
        {
            count++;
        }
    }
    return count;
}  // or 
int fizz_buzz(int n){
    int count=0;
    for (int i=1;i<n;i++)
    {
        if ((i%11==0)||(i%13==0))
        {
            count+=count_seven(to_string(i));
        }
    }
    return count;
}  // using to_string