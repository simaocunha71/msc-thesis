    vector<int> a;
    if (lst.size() == 0) {
        a.push_back(0);
        a.push_back(0);
        return a;
    }
    int max = -1;
    int min = 1000000000;
    for (int i = 0; i < lst.size(); i++) {
        if (lst[i] < 0 && lst[i] > max) {
            max = lst[i];
        }
        if (lst[i] > 0 && lst[i] < min) {
            min = lst[i];
        }
    }
    vector<int> b;
    b.push_back(max);
    b.push_back(min);
    return b;
}

int main(int argc, char** argv) {
    vector<int> a;
    a.push_back(2);
    a.push_back(4);
    a.push_back(1);
    a.push_back(3);
    a.push_back(5);
    a.push_back(7);
    printf("%d %d\n", largest_smallest_integers(a)[0], largest_smallest_integers(a)[1]);
    return 0;
}
