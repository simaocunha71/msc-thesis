    vector<int> result;
    set<int> s1(l1.begin(), l1.end());
    set<int> s2(l2.begin(), l2.end());

    set<int> intersection;
    set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(),
                      inserter(intersection, intersection.begin()));

    vector<int> result2(intersection.begin(), intersection.end());
    sort(result2.begin(), result2.end());

    return result2;
}

int main() {
    vector<int> a = {1, 4, 3, 34, 653, 2, 5};
    vector<int> b = {5, 7, 1, 5, 9, 653, 121};

    vector<int> result = common(a, b);

    for(int i=0; i<result.size(); i++)
    {
        printf("%d ", result[i]);
    }
    return 0;
}
Output:
1 5 653

