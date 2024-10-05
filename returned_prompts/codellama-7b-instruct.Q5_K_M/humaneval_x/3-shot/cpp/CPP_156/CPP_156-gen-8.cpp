    vector<string> roman_nums;
    roman_nums.push_back("I");
    roman_nums.push_back("V");
    roman_nums.push_back("X");
    roman_nums.push_back("L");
    roman_nums.push_back("C");
    roman_nums.push_back("D");
    roman_nums.push_back("M");
    string roman_num;
    int i=0;
    while(number>0){
        if (number-roman_nums[i*10]>=0){
            number-=roman_nums[i*10];
            roman_num+=(roman_nums[i]);
        }
        else{
            if (number-roman_nums[i*5]>=0){
                number-=roman_nums[i*5];
                roman_num+=(roman_nums[i+1]);
            }
            else{
                if (number-roman_nums[i]>=0){
                    number-=roman_nums[i];
                    roman_num+=(roman_nums[i+2]);
                }
                else{
                    i+=1;
                }
            }
        }
    }
    return roman_num;
}



