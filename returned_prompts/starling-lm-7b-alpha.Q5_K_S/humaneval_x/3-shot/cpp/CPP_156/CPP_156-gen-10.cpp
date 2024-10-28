    vector<string> hundreds={"c","cc","cd","d","cm"};
    vector<string> tens={"x","xx","xc"};
    vector<string> ones={"i","ii","ij","v"};
    vector<string> fives={"v","vi","vii","viii","ix"};
    vector<string> zeroes={"","","","","",
                           "",
                           "","","","",
                           "",
                           "",
                           "",
                           "",
                           "","","","","",
                           "",
                           "",
                           "",
                           "",
                           "",
                           ""};

    string result="";
    int h=number/100;
    int t=(number%100)/10;
    int o=number%10;
    result+=hundreds[h]+tens[t]+ones[o]+zeroes[o];
    return result;
}


