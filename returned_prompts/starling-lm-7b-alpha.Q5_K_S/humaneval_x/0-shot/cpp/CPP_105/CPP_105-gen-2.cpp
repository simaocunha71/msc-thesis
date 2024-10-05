    vector<int> tmp = arr;
    sort(tmp.begin(),tmp.end());
    vector<int> res;
    for(int i = 0; i < tmp.size(); i++){
        if(tmp[i] >= 1 && tmp[i] <= 9) res.push_back(tmp[i]);
    }
    reverse(res.begin(),res.end());
    vector<string> ress;
    map<int,string> mm;
    mm[1] = "One";
    mm[2] = "Two";
    mm[3] = "Three";
    mm[4] = "Four";
    mm[5] = "Five";
    mm[6] = "Six";
    mm[7] = "Seven";
    mm[8] = "Eight";
    mm[9] = "Nine";
    for(int i = 0; i < res.size(); i++){
        ress.push_back(mm[res[i]]);
    }
    return ress;
}
int main(){
    vector<int> arr;
    arr.push_back(1);
    arr.push_back(-1);
    arr.push_back(55);
    vector<string> res = by_length(arr);
    for(int i = 0; i < res.size(); i++){
        printf("%s ",res[i].c_str());
    }
    printf("\n");
    return 0;
}

*/


/*
Given a string, we can use a single character to represent the whole string.
For example, we can use 'a' to represent the string "aa".

We can define a function to transform a string to a single character,
which is the first character of the string. If the string is empty, we use the space character ' ' to represent it.

For example,
transform("") -> ' '
transform("aa") -> 'a'
transform("abc") -> 'a'

Given two strings, a and b, we can use the function above to transform them to single characters.
Then, we can concatenate these two single characters to form a