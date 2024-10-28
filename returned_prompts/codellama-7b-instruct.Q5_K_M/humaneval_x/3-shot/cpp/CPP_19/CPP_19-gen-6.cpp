    map<string,int> my_map;
    string temp;
    int i;
    for (i=0;i<numbers.length();i++)
    {
        temp=numbers[i];
        my_map[temp]+=1;
    }
    string final_ans="";
    for (auto it=my_map.begin();it!=my_map.end();it++)
    {
        final_ans+=it->first;
        final_ans+=" ";
    }
    return final_ans;
}

