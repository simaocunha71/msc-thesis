    vector<string> roman_nums;
    roman_nums.push_back("m");
    roman_nums.push_back("cm");
    roman_nums.push_back("d");
    roman_nums.push_back("cd");
    roman_nums.push_back("c");
    roman_nums.push_back("xc");
    roman_nums.push_back("l");
    roman_nums.push_back("xl");
    roman_nums.push_back("x");
    roman_nums.push_back("ix");
    roman_nums.push_back("v");
    roman_nums.push_back("iv");
    roman_nums.push_back("i");
    int i;
    string roman_num;
    while (number>0){
        for (i=0;i<roman_nums.size();i++){
            if (number>=roman_nums.at(i).length()){
                number-=roman_nums.at(i).length();
                roman_num=roman_nums.at(i);
            }
        }
    }
    return roman_num;
}


