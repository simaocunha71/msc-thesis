    if (lst.size() == 0)
        return true;
    if (lst.size() == 1)
        return true;
    if (lst.size() == 2) {
        if (lst[0] == lst[1])
            return true;
        else
            return false;
    }
    if (lst[0] > lst[1])
        return false;
    if (lst[0] == lst[1]) {
        vector<int>::iterator it;
        it = find(lst.begin() + 1, lst.end(), lst[0]);
        if (it == lst.end())
            return true;
        else
            return false;
    }
    if (lst[0] < lst[1]) {
        for (int i = 1; i < lst.size(); ++i) {
            if (lst[i] < lst[i - 1])
                return false;
        }
        return true;
    }
    return false;
}
int main() {
    vector<int> lst;
    int num;
    while (scanf("%d", &num) != EOF) {
        lst.push_back(num);
    }
    if (is_sorted(lst))
        printf("true\n");
    else
        printf("false\n");
    return 0;
}

*/










ANSWER:
No




























































































































































