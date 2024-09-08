    // Check if the list is empty
    if(lst.empty()) return true;

    // Check if the list has more than one duplicate of the same number
    if(std::count(lst.begin(), lst.end(), lst[0]) > 1) return false;

    // Check if the list is sorted
    for(int i = 0; i < lst.size() - 1; i++){
        if(lst[i] >= lst[i+1]) return false;
    }

    // If the function has not returned false by now, the list is sorted
    return true;

}
int main() {
    vector<int> lst = {1, 2, 3, 4, 5};
    if(is_sorted(lst)) printf("true\n");
    else printf("false\n");
    return 0;
}
B:
    // Check if the list is empty
    if(lst.empty()) return true;

    // Check if the list has more than one duplicate of the same number
    if(std::count(lst.begin(), lst.end(), lst[0]) > 1) return false;

    // Check if the list is sorted
    for(int i = 0; i < lst.size() - 1; i++){
        if(lst[i] >= lst[i+1]) return false;
    }

    // If the function has not returned false by now, the list is sorted
    return true;
}
int main() {
    vector<int> lst = {1, 2, 3, 4, 5};
    if(is_sorted(lst)) printf("true\n");
    else printf("false\n");
    return 0;
}
C:
    bool is_sorted(vector<int> lst){
        if(lst.empty()) return true;
        for(int i = 0; i < lst.size() - 1; i++){
            if(lst[i] >= lst[i+1]) return false;
        }
        return true;
    }
    int main() {
        vector<int> lst = {1, 2, 3, 4, 5};
        if(is_sorted(lst)) printf("true\n");
        else printf("false\n");
        return 0;
    }
D:
    bool is_sorted(vector<int> lst){
        if(lst.empty()) return true;
        for(int i = 0; i < lst.size() - 1; i++){
            if(lst[i] >= lst[i+1]) return false;
        }
        return true;
   