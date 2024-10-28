    return (find(lst.begin(), lst.end(), lst[0]) == lst.begin() &&
            find(lst.begin(), lst.end(), lst[lst.size() - 1]) == lst.end() - 1 &&
            equal(lst.begin() + 1, lst.end() - 1, lst.begin() + 2)
    );
}


