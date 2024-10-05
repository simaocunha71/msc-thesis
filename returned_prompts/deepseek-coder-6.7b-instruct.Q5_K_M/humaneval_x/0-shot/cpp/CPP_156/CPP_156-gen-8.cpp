    // Define roman numerals
    vector<int> val = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    vector<string> roman = {"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};

    string res = "";

    for(int i=0; i<val.size(); i++) {
        while(number >= val[i]) {
            number -= val[i];
            res += roman[i];
        }
    }

    return res;
}

int main() {
    int num;
    scanf("%d", &num);
    printf("%s", int_to_mini_roman(num).c_str());
    return 0;
}
*/

//main.cpp
/*
