    return l;
}
int main() {
    vector<int> l = {1, 2, 3};
    vector<int> r = incr_list(l);
    for (int i = 0; i < r.size(); i++) {
        printf("%d ", r[i]);
    }
    printf("\n");
    return 0;
}
