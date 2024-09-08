    map<char, int> result;
    if(test.empty()) return result;
    map<char, int>::iterator it;
    for(int i = 0; i < test.size(); i++){
        if(result.find(test[i]) == result.end()) {
            result[test[i]] = 1;
        }
        else {
            result[test[i]]++;
        }
    }
    int max = 0;
    for(it = result.begin(); it != result.end(); it++){
        if(it->second > max) max = it->second;
    }
    map<char, int> maxResult;
    for(it = result.begin(); it != result.end(); it++){
        if(it->second == max) maxResult[it->first] = it->second;
    }
    return maxResult;
}

int main() {
    string test = "a b c";
    map<char, int> result = histogram(test);
    for (map<char, int>::iterator it = result.begin(); it != result.end(); it++) {
        cout << it->first << " " << it->second << endl;
    }
    return 0;
}

