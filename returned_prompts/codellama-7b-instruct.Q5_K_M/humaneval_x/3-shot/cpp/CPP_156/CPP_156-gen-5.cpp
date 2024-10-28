    vector<string> mini_roman = {"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};
    vector<int> mini_num = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    int num_len = mini_num.size();
    string result = "";
    while (number>0)
    {
        for (int i=0;i<num_len;i++)
        {
            while (number>=mini_num[i])
            {
                number-=mini_num[i];
                result+=mini_roman[i];
            }
        }
    }
    return result;
}



