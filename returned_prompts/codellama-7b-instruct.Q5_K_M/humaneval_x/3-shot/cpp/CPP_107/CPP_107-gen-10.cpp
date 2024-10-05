    vector<int> nums_count;
    nums_count.push_back(0);
    nums_count.push_back(0);
    int i;
    for (i=1;i<n;i++)
    {
        if (is_palindrome(i))
        {
            if (i%2==0)
            {
                nums_count[0]+=1;
            }
            else
            {
                nums_count[1]+=1;
            }
        }
    }
    return nums_count;
}
bool is_palindrome(int num)
{
    char str[100];
    sprintf(str, "%d", num);
    int i=0;
    int j=strlen(str)-1;
    while (j>=i)
    {
        if (str[i]!=str[j])
        return false;
        i++;
        j--;
    }
    return true;
}


