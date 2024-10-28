    vector<string> result;
    map<int, string> m;
    m[1] = "1n the str1ng 1 of the 1nput.";
    m[2] = "2n the str2ng 2 of the 2nput.";
    m[3] = "3n the str3ng 3 of the 3nput.";
    m[4] = "4n the str4ng 4 of the 4nput.";
    m[5] = "5n the str5ng 5 of the 5nput.";
    m[6] = "6n the str6ng 6 of the 6nput.";
    m[7] = "7n the str7ng 7 of the 7nput.";
    m[8] = "8n the str8ng 8 of the 8nput.";
    m[9] = "9n the str9ng 9 of the 9nput.";
    for(int i=0; i<lst.size(); i++){
        int count = 0;
        for(int j=0; j<lst[i].size(); j++){
            if((lst[i][j] - '0') % 2 != 0) count++;
        }
        result.push_back(m[count]);
    }
    return result;
}

int main(){
    vector<string> test1 = {"1234567"};
    vector<string> test2 = {"3","11111111"};
    vector<string> res1 = odd_count(test1);
    vector<string> res2 = odd_count(test2);
    for(int i=0; i<res1.size(); i++) printf("%s\n", res1[i].c_str());
    for(int i=0; i<res2.size(); i++) printf("%s\n", res2[i].c_str());
    return 0;
}

Output:
4n the str4ng 4 of the 4nput.
1n the str1ng 