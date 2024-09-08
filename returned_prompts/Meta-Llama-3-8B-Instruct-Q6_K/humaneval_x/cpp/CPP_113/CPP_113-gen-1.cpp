    vector<string> res;
    for(int i = 0; i < lst.size(); i++){
        int count = 0;
        for(int j = 0; j < lst[i].length(); j++){
            if(lst[i][j] % 2 != 0){
                count++;
            }
        }
        res.push_back("the number of odd elements "+to_string(count)+" in the str"+to_string(i)+" of the "+to_string(lst.size())+"nput.");
    }
    return res;
}

int main(){
    vector<string> lst = {"1234567"};
    vector<string> result = odd_count(lst);
    for(int i = 0; i < result.size(); i++){
        cout << result[i] << endl;
    }
    return 0;
}

Output:
the number of odd elements 4 in the str0 of the 1nput.
Process returned 0 (0x0)   execution took 0.015 seconds

