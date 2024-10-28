    int i;
    int result=-1;
    int distance=abs(result);
    for (i=0;i<value.length();i++)
    {
        if (value[i]=='.')
        {
            for (i=i+1;i<value.length();i++)
            {
                result=result*10+value[i]-'0';
                int distance2=abs(value.size()-i-1-result);
                if (distance2<distance)
                {
                    distance=distance2;
                }
            }
            break;
        }
    }
    return result;
}


