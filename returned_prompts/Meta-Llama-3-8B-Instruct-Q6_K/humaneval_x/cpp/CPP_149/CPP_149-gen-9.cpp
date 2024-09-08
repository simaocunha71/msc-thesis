    vector<string> result;
    for(int i=0; i<lst.size(); i++){
        if(lst[i].size() % 2 == 0){
            result.push_back(lst[i]);
        }
    }
    sort(result.begin(), result.end(), [](const string& a, const string& b){
        if(a.size() == b.size()){
            return a < b;
        }
        return a.size() < b.size();
    });
    return result;
}
int main() {
    vector<string> lst = {"aa", "a", "aaa"};
    vector<string> result = sorted_list_sum(lst);
    for(const auto& item: result){
        printf("%s\n", item.c_str());
    }
    return 0;
}

