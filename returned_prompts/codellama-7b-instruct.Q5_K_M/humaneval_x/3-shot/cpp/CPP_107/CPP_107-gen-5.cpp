    vector<int> palindromes(2);
    int i;
    for (i=1;i<=n;i++)
    {
        if (i==0)
        continue;
        string number=to_string(i);
        int length=number.length();
        int half=length/2;
        if (length%2==0){
            int j;
            for (j=0;j<half;j++)
            if (number[j]!=number[length-1-j])
            continue A;
        }
        else{
            int j;
            for (j=0;j<half-1;j++)
            if (number[j]!=number[length-1-j])
            continue A;
        }
        if (length%2==0)
        palindromes[0]+=1;
        else
        palindromes[1]+=1;
    }
    return palindromes;
}


