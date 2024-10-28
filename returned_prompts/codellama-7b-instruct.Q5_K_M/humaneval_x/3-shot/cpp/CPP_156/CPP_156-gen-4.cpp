    vector<string> roman={"i","v","x","l","c","d","m"};
    vector<int> values={1,5,10,50,100,500,1000};
    string mini_roman;
    int i;
    for (i=0;i<values.size();i++)
    while (number>=values[i])
    {
        mini_roman+=roman[i];
        number-=values[i];
    }
    return mini_roman;
}



