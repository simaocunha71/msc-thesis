    vector<string> ans;
    map <char,int> odd;
    odd['1']=1;
    odd['3']=1;
    odd['5']=1;
    odd['7']=1;
    odd['9']=1;
    for (int i=0;i<lst.size();i++)
    {
        int count=0;
        for (int j=0;j<lst[i].length();j++)
        if (odd.find(lst[i][j])!=odd.end())
        count+=1;
        ans.push_back("the number of odd elements "+to_string(count)+"n the str"+to_string(count)+"ng "+to_string(count)+" of the "+to_string(count)+"nput.");
    }
    return ans;
}

