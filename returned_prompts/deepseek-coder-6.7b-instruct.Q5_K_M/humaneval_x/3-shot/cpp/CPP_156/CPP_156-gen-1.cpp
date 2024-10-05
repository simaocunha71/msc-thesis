    string roman[] = {"m","cm","d","cd","c","xc","l","xl","x","ix","v","iv","i"};
    int value[] = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
    string result;
    for (int i=0; i<13; i++)
    {
        while (number>=value[i])
        {
            number -= value[i];
            result += roman[i];
        }
    }
    return result;
}


