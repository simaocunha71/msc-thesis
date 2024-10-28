    for (int i=0;i<lst1.size();i++)
    {
        if (lst1[i]%2!=0)
        {
            for (int j=0;j<lst2.size();j++)
            {
                if (lst2[j]%2==0)
                {
                    swap(lst1[i],lst2[j]);
                    break;
                }
            }
        }
    }
    for (int i=0;i<lst1.size();i++)
    {
        if (lst1[i]%2!=0)
        {
            return "NO";
        }
    }
    return "YES";
}
// Note: The above function will modify the original vectors. If you do not want to modify the original vectors, you can make copies of the vectors at the beginning of the function. 
// Also, this function assumes that the input vectors will always be non-empty and will always contain at least one even number in lst2. If this is not guaranteed, you should add error checking code. 