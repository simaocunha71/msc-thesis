    vector<int> val = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };
    vector<string> roman = {"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};
    string res = "";
    for(int i=0; i<13; i++){
        while(number >= val[i]){
            number -= val[i];
            res += roman[i];
        }
    }
    return res;
}


