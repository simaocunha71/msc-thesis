    int sum = array[0] + array[array.size()-1];
    vector<int> copy = array;
    if(sum % 2 == 0) {
        sort(copy.begin(), copy.end(), greater<int>());
    }
    else {
        sort(copy.begin(), copy.end());
    }
    return copy;
}

int main()
{
    vector<int> vec = {2, 4, 3, 0, 1, 5, 6};
    vector<int> result = sort_array(vec);
    for(auto x: result) {
        printf("%d