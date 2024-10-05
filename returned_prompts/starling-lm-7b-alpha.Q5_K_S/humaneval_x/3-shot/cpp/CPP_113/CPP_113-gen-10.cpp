    vector<string> res;
    map<string, string> m;
    int i;
    for (i=0;i<lst.size();i++)
    {
        int count=0;
        for (int j=0;j<lst[i].length();j++)
        {
            if (lst[i][j]-'0'%2==1)
            {
            count+=1;
            }
        }
        string temp="the number of odd elements ";
        string temp_str="";
        for (int j=0;j<lst[i].length();j++)
        {
            if (lst[i][j]=='4')
            {
            temp_str+='4';
            }
            else
            {
            temp_str+='n';
            }
        }
        temp+=temp_str;
        temp+=", ";
        temp+=to_string(i);
        temp+=" of the ";
        temp+=to_string(i+1);
        temp+="nput.";
        res.push_back(temp);
    }
    return res;
}



