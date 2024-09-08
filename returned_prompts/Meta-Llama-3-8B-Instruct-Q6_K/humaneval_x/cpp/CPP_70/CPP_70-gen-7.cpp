    vector<int> result;
    vector<int> temp = lst;
    sort(temp.begin(), temp.end());
    int min_index = 0;
    int max_index = temp.size() - 1;
    while(!temp.empty()){
        result.push_back(temp[min_index]);
        temp.erase(temp.begin() + min_index);
        if(temp.empty()) break;
        result.push_back(temp[max_index]);
        temp.erase(temp.begin() + max_index);
        max_index--;
        if(max_index == -1) break;
        min_index++;
    }
    return result;
}
int main() {
    vector<int> lst = {1, 2, 3, 4};
    vector<int> result = strange_sort_list(lst);
    for(int i = 0; i < result.size(); i++) {
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}
