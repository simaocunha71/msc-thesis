    vector<int> ans;
    for(int i = 0; i < lst.size(); i++) {
        if(lst[i] < 0 && (ans.size() == 0 || lst[i] > ans[0])) {
            ans.push_back(lst[i]);
        }
    }

    for(int i = 0; i < lst.size(); i++) {
        if(lst[i] > 0 && (ans.size() == 0 || lst[i] < ans[0])) {
            ans.push_back(lst[i]);
        }
    }
    if(ans.size() == 0) {
        ans.push_back(0);
        ans.push_back(0);
    }
    return ans;

}

int main() {
    vector<int> a = {2, 4, 1, 3, 5, 7};
    vector<int> b = {};
    vector<int> c = {0};
    printf("%s\n", largest_smallest_integers(a).empty() ? "true" : "false");
    printf("%s\n", largest_smallest_integers(b).empty() ? "true" : "false");
    printf("%s\n", largest_smallest_integers(c).empty() ? "true" : "false");
    return 0;
}















































































































































































