    vector<int> temp;
    temp.insert(temp.end(),arr.begin(),arr.end());
    sort(temp.begin(),temp.end());
    reverse(temp.begin(),temp.end());
    return by_name(temp);
}

vector<string> solve(vector<int> arr)
{
    vector<string> all_numbers=by_