    vector<int> res;
    set<int> s1(l1.begin(), l1.end());
    set<int> s2(l2.begin(), l2.end());
    set<int> s3;
    set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(),
                     inserter(s3, s3.begin()));
    for (int i = 0; i < s3.size(); i++) {
        res.push_back(s3[i]);
    }
    sort(res.begin(),res.end());
    return res;
}
int main() {
    vector<int> l1={1, 4, 3, 34, 653, 2, 5};
    vector<int> l2={5, 7, 1, 5, 9, 653, 121};
    vector<int> result = common(l1, l2);
    for (int i = 0; i < result.size(); i++) {
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}
B:
    vector<int> res;
    set<int> s1(l1.begin(), l1.end());
    set<int> s2(l2.begin(), l2.end());
    set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(),
                     inserter(res, res.begin()));
    return res;
}

C:
    vector<int> res;
    set<int> s1(l1.begin(), l1.end());
    set<int> s2(l2.begin(), l2.end());
    set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(),
                     inserter(res, res.begin()));
    sort(res.begin(),res.end());
    return res;
}

D:
    vector<int> res;
    set<int> s1(l1.begin(), l1.end());
    set<int> s2(l2.begin(), l2.end());
    set<int> s3;
    set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(),
                     inserter(s3, s3.begin()));
    for (int i = 0; i < s3.size(); i++) {
        res.push_back(s3[i]);
    }
    sort(res.begin(),res.end());
    return res;
}
E:
    vector<int> res;
    set<int> s1(l1.begin(), l1.end());
    set<int> s2(l2.begin(), l2.end