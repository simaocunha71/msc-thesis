    vector<string> result;
    string tmp;
    map<char,int> count_map;
    for (int i=0;i<lst.size();i++)
    {
        tmp="the number of odd elements ";
        tmp+=to_string(lst[i].length());
        tmp+="n the str";
        tmp+=to_string(i+1);
        tmp+="ng ";
        tmp+=to_string(i+1);
        tmp+=" of the ";
        tmp+="nput.";
        int count=0;
        for (int j=0;j<lst[i].length();j++)
        {
            if (lst[i][j]-'0'%2==1)
            count+=1;
        }
        tmp+=" "+to_string(count);
        result.push_back(tmp);
    }
    return result;
}


