    int maxVal = -1;
    int maxCount = 0;
    for(int i = 1; i <= *max_element(lst.begin(), lst.end()); i++){
        int count = 0;
        for(int j = 0; j < lst.size(); j++){
            if(lst[j] == i){
                count++;
            }
        }
        if(count >= i && i > 0){
            if(count > maxCount){
                maxCount = count;
                maxVal = i;
            }
        }
    }
    if(maxVal > 0){
        return maxVal;
    } else {
        return -1;
    }
}

int main() {
    vector<int> lst = {4, 1, 2, 2, 3, 1};
    printf("%d\n", search(lst));
    return 0;
}
B:
    int search(vector<int> lst) {
        int maxVal = -1;
        for (int i = 1; i <= *max_element(lst.begin(), lst.end()); i++) {
            if (count(lst.begin(), lst.end(), i) >= i) {
                if (i > maxVal) {
                    maxVal = i;
                }
            }
        }
        return maxVal > 0 ? maxVal : -1;
    }

int main() {
    vector<int> lst = {4, 1, 2, 2, 3, 1};
    cout << search(lst) << endl;
    return 0;
}
C:
    int search(vector<int> lst) {
        int maxVal = -1;
        for (int i = 1; i <= *max_element(lst.begin(), lst.end()); i++) {
            if (count(lst.begin(), lst.end(), i) >= i) {
                maxVal = i;
                break;
            }
        }
        return maxVal > 0 ? maxVal : -1;
    }

int main() {
    vector<int> lst = {4, 1, 2, 2, 3, 1};
    cout << search(lst) << endl;
    return 0;
}
D:
    int search(vector<int> lst) {
        int maxVal = -1;
        for (int i = 1; i <= *max_element(lst.begin(), lst.end()); i++) {
            if (count(lst.begin(), lst.end(), i) >= i) {
                maxVal = i;
            }
