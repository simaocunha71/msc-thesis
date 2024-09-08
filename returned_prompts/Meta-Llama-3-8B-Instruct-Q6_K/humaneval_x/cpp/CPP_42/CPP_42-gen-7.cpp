    vector<int> result;
    for (int i = 0; i < l.size(); i++) {
        result.push_back(l[i] + 1);
    }
    return result;
}
int main() {
    vector<int> l = {1, 2, 3};
    vector<int> res = incr_list(l);
    for (int i = 0; i < res.size(); i++) {
        printf("%d ", res[i]);
    }
    printf("\n");
    return 0;
}

Output:
2 3 4
