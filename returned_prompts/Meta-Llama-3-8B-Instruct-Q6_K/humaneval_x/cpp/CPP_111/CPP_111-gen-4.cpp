    map<char,int> countMap;
    int maxCount = 0;
    for (int i = 0; i < test.length(); i++) {
        char c = test[i];
        if (countMap.find(c) == countMap.end()) {
            countMap[c] = 1;
        } else {
            countMap[c]++;
        }
        if (countMap[c] > maxCount) {
            maxCount = countMap[c];
        }
    }
    map<char,int> result;
    for (map<char,int>::iterator it = countMap.begin(); it != countMap.end(); it++) {
        if (it->second == maxCount) {
            result[it->first] = it->second;
        }
    }
    return result;
}
int main()
{
    string test = "a b c";
    map<char,int> result = histogram(test);
    for (map<char,int>::iterator it = result.begin(); it != result.end(); it++) {
        printf("(%c, %d)\n", it->first, it->second);
    }
    return 0;
}
