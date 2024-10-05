    map<string,int> number_map;
    string result;
    string num;
    int i;
    for (i=0;i<numbers.length();i++)
    {
        num=numbers[i];
        if (number_map.find(num)==number_map.end())
        {
            number_map[num]=1;
            result=result+num;
        }
    }
    return result;
}


