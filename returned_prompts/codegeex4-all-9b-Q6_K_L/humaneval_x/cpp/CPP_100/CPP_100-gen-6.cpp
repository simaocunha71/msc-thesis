    if (n == 1)
        return {1};
    else if (n == 2)
        return {2, 4};
    else {
        vector<int> result = make_a_pile(n - 2);
        result.push_back(result.back() + 2);
        return result;
    }
}
