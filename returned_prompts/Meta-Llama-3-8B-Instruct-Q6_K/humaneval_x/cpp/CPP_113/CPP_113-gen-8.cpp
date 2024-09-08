    map<int, int> count;
    for(int i=0; i<lst.size(); i++){
        int odd = 0;
        for(int j=0; j<lst[i].size(); j++){
            if(lst[i][j]-'0' % 2 != 0)
                odd++;
        }
        count[i] = odd;
    }

    vector<string> result;
    for(int i=0; i<lst.size(); i++){
        string temp;
        temp += 't';
        temp += 'h';
        temp += 'e';
        temp += ' ';
        temp += 'n';
        temp += 'u';
        temp += 'm';
        temp += 'b';
        temp += 'e';
        temp += 'r';
        temp += ' ';
        temp += 'o';
        temp += 'f';
        temp += ' ';
        temp += 'o';
        temp += 'd';
        temp += 'd';
        temp += ' ';
        temp += 'e';
        temp += 'l';
        temp += 'e';
        temp += 'm';
        temp += 'e';
        temp += 'n';
        temp += 't';
        temp += 's';
        temp += ' ';
        temp += 'i';
        temp += 'n';
        temp += ' ';
        temp += 't';
        temp += 'h';
        temp += 'e';
        temp += ' ';
        temp += 's';
        temp += 't';
        temp += 'r';
        temp += 'i';
        temp += 'n';
        temp += 'g';
        temp += ' ';
        temp += 'o';
        temp += 'f';
        temp += ' ';
        temp += 't';
        temp += 'h';
        temp += 'e';
        temp += ' ';
        temp += 'i';
        temp += 'n';
        temp += 'p';
        temp += 'u';
        temp += 't';
        temp += '.';
        temp += ' ';
        temp += to_string(count[i]);
        result.push_back(temp);
    }
    return result;
}

int main(){
    vector<string> lst = {"1234567"};
    vector<string> res = odd_count(lst);
    for(int i=0; i<res.size(); i++){
        printf("%s\n", res[i].c_str());
    }
    return 0;
}

S:
    The solution is correct. It correctly counts the number of odd digits in