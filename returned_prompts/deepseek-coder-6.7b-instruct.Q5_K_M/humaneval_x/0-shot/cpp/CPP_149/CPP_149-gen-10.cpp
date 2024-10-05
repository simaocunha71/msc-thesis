    vector<string> vec;
    int i;

    for(i = 0; i < lst.size(); i++){
        if(lst[i].length() % 2 == 0){
            vec.push_back(lst[i]);
        }
    }

    sort(vec.begin(), vec.end(), [](const string &a, const string &b) {
        if (a.size() != b.size()) {
            return a.size() < b.size();
        }
        return a < b;
    });

    return vec;
}

int main() {
    vector<string> v = {"ab", "a", "aaa", "cd"};
    vector<string> res = sorted_list_sum(v);
    for (int i = 0; i < res.size(); i++) {
        printf("%s ", res[i].c_str());
    }
    return 0;
}
*/

//