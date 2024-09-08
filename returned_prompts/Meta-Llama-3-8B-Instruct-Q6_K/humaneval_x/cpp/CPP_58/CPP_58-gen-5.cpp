    vector<int> common_elements;

    set<int> s1(l1.begin(), l1.end());
    set<int> s2(l2.begin(), l2.end());

    set<int> intersection;

    set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(),
                     inserter(intersection, intersection.begin()));

    for (int i : intersection)
        common_elements.push_back(i);

    sort(common_elements.begin(), common_elements.end());

    return common_elements;
}

int main() {
    vector<int> l1 = {1, 4, 3, 34, 653, 2, 5};
    vector<int> l2 = {5, 7, 1, 5, 9, 653, 121};
    vector<int> result = common(l1, l2);
    for (int i : result) {
        printf("%d ", i);
    }
    printf("\n");

    l1 = {5, 3, 2, 8};
    l2 = {3, 2};
    result = common(l1, l2);
    for (int i : result) {
        printf("%d ", i);
    }
    printf("\n");

    return 0;
}
B:
    vector<int> l1 = {1, 4, 3, 34, 653, 2, 5};
    vector<int> l2 = {5, 7, 1, 5, 9, 653, 121};
    vector<int> result = common(l1, l2);
    for (int i : result) {
        printf("%d ", i);
    }
    printf("\n");

    l1 = {5, 3, 2, 8};
    l2 = {3, 2};
    result = common(l1, l2);
    for (int i : result) {
        printf("%d ", i);
    }
    printf("\n");

    return 0;
}
C:
    vector<int> l1 = {1, 4, 3, 34, 653, 2, 5};
    vector<int> l2 = {5, 7, 1, 5, 9, 653, 121};
    vector<int> result = common(l1, l2);
    for (int i : result) {
        printf("%d ", i);
    }
    printf("\