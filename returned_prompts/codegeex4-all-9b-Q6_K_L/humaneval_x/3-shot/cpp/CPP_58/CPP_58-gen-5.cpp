    vector<int> all_parens;
    all_parens.insert(all_parens.end(),l1.begin(),l1.end());
    all_parens.insert(all_parens.end(),l2.begin(),l2.end());
    sort(all_parens.begin(),all_parens.end());
    all_parens.erase(unique(all_parens.begin(), all_parens.end()), all_parens.end());
    return all_parens;
}

