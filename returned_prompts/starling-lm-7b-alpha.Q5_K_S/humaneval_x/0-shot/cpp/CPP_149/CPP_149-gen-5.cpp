    vector<string> result = lst;
    sort(result.begin(), result.end());
    vector<string> odd_len;
    for(int i = 0; i < result.size(); i++){
        if(result[i].size() % 2 != 0){
            odd_len.push_back(result[i]);
        }
    }
    result.erase(remove_if(result.begin(), result.end(), [&](string str){return odd_len.count(str);}), result.end());
    sort(result.begin(), result.end(), [](string a, string b){return a.length() < b.length();});
    return result;
}

vector<string> vector_sort(vector<string> lst){
    vector<string> result = lst;
    sort(result.begin(), result.end());
    vector<string> odd_len;
    for(int i = 0; i < result.size(); i++){
        if(result[i].size() % 2 != 0){
            odd_len.push_back(result[i]);
        }
    }
    result.erase(remove_if(result.begin(), result.end(), [&](string str){return odd_len.count(str);}), result.end());
    sort(result.begin(), result.end(), [](string a, string b){return a.length() < b.length();});
    return result;
}

int main(){
    vector<string> lst = {"aa", "a", "aaa"};
    vector<string> result = sorted_list_sum(lst);
    printf("%s\n", result[0].c_str());
    return 0;
}






































































































