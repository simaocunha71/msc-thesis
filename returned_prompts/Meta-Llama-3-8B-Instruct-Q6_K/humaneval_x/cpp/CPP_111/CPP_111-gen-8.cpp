    map<char,int> res;
    int maxCount = 0;
    for(int i = 0; i < test.size(); i++){
        char c = test[i];
        if(res.find(c) == res.end()){
            res[c] = 1;
        }else{
            res[c]++;
        }
        if(res[c] > maxCount){
            maxCount = res[c];
        }
    }
    for(auto it = res.begin(); it != res.end(); ++it){
        if(it->second == maxCount){
            res[it->first] = make_pair(it->first,maxCount);
        }
    }
    return res;

} 

B:
    map<char, int> histogram(string test) {
        map<char, int> res;
        for (int i = 0; i < test.size(); i++) {
            char c = test[i];
            res[c]++;
        }
        int maxCount = 0;
        for (auto it = res.begin(); it != res.end(); ++it) {
            if (it->second > maxCount) {
                maxCount = it->second;
            }
        }
        map<char, int> res2;
        for (auto it = res.begin(); it != res.end(); ++it) {
            if (it->second == maxCount) {
                res2[it->first] = it->second;
            }
        }
        return res2;
    }

C:
    map<char, int> histogram(string test) {
        map<char, int> res;
        for (int i = 0; i < test.size(); i++) {
            char c = test[i];
            res[c]++;
        }
        int maxCount = 0;
        char maxChar;
        for (auto it = res.begin(); it != res.end(); ++it) {
            if (it->second > maxCount) {
                maxCount = it->second;
                maxChar = it->first;
            }
        }
        map<char, int> res2;
        for (auto it = res.begin(); it != res.end(); ++it) {
            if (it->second == maxCount) {
                res2[it->first] = it->second;
            }
        }
        res2[maxChar] = maxCount;
        return res2;
    }

D:
    map<char, int> histogram(string test) {
        map<char, int> res;
        for (int i = 0; i <