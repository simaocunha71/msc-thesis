    string words[50];
    int i,j,count=0,flag;
    string result="";
    for(i=0;i<sentence.length();i++)
    {
        words[count]="";
        while(sentence[i] != ' ' && i<sentence.length())
        {
            words[count]+=sentence[i];
            i++;
        }
        count++;
    }
    for(i=0;i<count;i++)
    {
        if(words[i].length()>1)
        {
            flag=0;
            for(j=2;j<=words[i].length()/2;j++)
            if(words[i].length()%j==0)
            {
                flag=1;
                break;
            }
            if(flag==0)
            result+=words[i]+" ";
        }
    }
    if(result.length()>0)
    result.pop_back();
    return result;
}

