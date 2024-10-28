    vector<pair<int,string>> romanNumerals = {{1000,"m"},{900,"cm"},{500,"d"},{400,"cd"},{100,"c"},{90,"xc"},{50,"l"},{40,"xl"},{10,"x"},{9,"ix"},{5,"v"},{4,"iv"},{1,"i"}};
    string roman;
    for (int i=0;i<romanNumerals.size();i++)
    {
        while (number>=romanNumerals[i].first)
        {
            roman+=romanNumerals[i].second;
            number-=romanNumerals[i].first;
        }
    }
    return roman;
}