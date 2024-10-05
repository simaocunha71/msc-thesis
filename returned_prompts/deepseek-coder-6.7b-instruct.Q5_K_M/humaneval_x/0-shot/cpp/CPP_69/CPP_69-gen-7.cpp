    int n = lst.size();
    int max_val = -1;
    int freq[n + 1];
    for (int i = 0; i <= n; i++) {
        freq[i] = 0;
    }
    for (int i = 0; i < n; i++) {
        freq[lst[i]]++;
        if (lst[i] > max_val) {
            max_val = lst[i];
        }
    }
    for (int i = max_val; i > 0; i--) {
        if (freq[i] >= i) {
            return i;
        }
    }
    return -1;
}

int main(){
    vector<int> lst{4, 1, 2, 2, 3, 1};
    printf("%d\n",search(lst));
    lst = {1, 2, 2, 3, 3, 3, 4, 4, 4};
    printf("%d\n",search(lst));
    lst = {5, 5, 4, 4, 4};
    printf("%d\n",search(lst));
    return 0;
}
*/
















































































































































































































