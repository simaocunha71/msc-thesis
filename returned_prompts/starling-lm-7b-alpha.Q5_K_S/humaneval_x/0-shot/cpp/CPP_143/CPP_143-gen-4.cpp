    int len=sentence.size();
    if(len==0)
    {
        return "";
    }
    int i=0;
    while(i<len)
    {
        char ch=sentence[i];
        if(ch==' ')
        {
            i++;
            continue;
        }
        else
        {
            int j=i;
            int k=i;
            while(j<len)
            {
                if(sentence[j]==' ')
                {
                    break;
                }
                j++;
            }
            while(k<j)
            {
                if(sentence[k]==' ')
                {
                    break;
                }
                k++;
            }
            int len1=k-i;
            if(isPrime(len1))
            {
                string s="";
                while(i<j)
                {
                    s+=sentence[i];
                    i++;
                }
                return s;
            }
            i=j;
        }
    }
    return "";
}
bool isPrime(int num)
{
    if(num<=1)
    {
        return false;
    }
    for(int i=2;i<=num/2;i++)
    {
        if(num%i==0)
        {
            return false;
        }
    }
    return true;
}

*/






















































































































































