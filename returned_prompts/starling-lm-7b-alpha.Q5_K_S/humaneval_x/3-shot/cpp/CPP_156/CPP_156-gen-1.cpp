    vector<int> ints={1000,900,500,400,100,90,50,40,10,9,5,4,1};
    vector<string> strings={"m","cm","d","cd","c","xc","l","xl","x","ix","v","iv","i"};
    string roman="";

    for (int i=0;i<ints.size();i++)
    {
        while (number>=ints[i])
        {
            roman+=strings[i];
            number-=ints[i];
        }
    }
    return roman;
}

