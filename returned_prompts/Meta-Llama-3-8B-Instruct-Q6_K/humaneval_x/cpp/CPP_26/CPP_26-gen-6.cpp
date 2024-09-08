    vector<int> result;
    for(auto x: numbers){
        if(find(result.begin(), result.end(), x) == result.end())
            result.push_back(x);
    }
    return result;
}
int main() {
    vector<int> numbers = {1, 2, 3, 2, 4};
    vector<int> result = remove_duplicates(numbers);
    for(auto x: result)
        printf("%d ", x);
    return 0;
}
