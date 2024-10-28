    vector<string> res;
    for (int i = 0; i < lst.size(); i++) {
        string tmp = "";
        int count = 0;
        for (int j = 0; j < lst[i].size(); j++) {
            if ((lst[i][j] - '0') % 2 != 0)
                count++;
        }
        tmp += to_string(count);
        string str = "the number of odd elements in the string " + tmp + " of the input.";
        res.push_back(str);
    }
    return res;
}

int main() {
    vector<string> v1 = {"3","11111111"};
    vector<string> result = odd_count(v1);
    for(int i = 0; i < result.size(); i++)
        printf("%s\n", result[i].c_str());
    return 0;
}
