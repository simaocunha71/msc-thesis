    vector<string> all_odds;
    string result;
    int i;
    for (i=0;i<lst.size();i++)
    {
        int odd_count=0;
        for (int j=0;j<lst[i].length();j++)
        if (lst[i][j]-'0'%2==1) odd_count+=1;
        result="the number of odd elements ";
        result+=char(lst[i].length()+'0');
        result+="n the str";
        result+=char(lst[i].length()+'0');
        result+="ng ";
        result+=char(lst[i].length()+'0');
        result+="n the ";
        result+=char(lst[i].length()+'0');
        result+="nput.";
        all_odds.push_back(result);
    }
    return all_odds;
}




