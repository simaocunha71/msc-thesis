    vector<string> roman_numbers={"m","cm","d","cd","c","xc","l","xl","x","ix","v","iv","i"};
    vector<int> roman_num_vals={1000,900,500,400,100,90,50,40,10,9,5,4,1};
    string roman_number;
    int i;
    int num=number;
    for (i=0;i<roman_num_vals.size();i++)
    {
        while (num>=roman_num_vals[i])
        {
            num-=roman_num_vals[i];
            roman_number+=roman_numbers[i];
        }
    }
    return roman_number;
}




