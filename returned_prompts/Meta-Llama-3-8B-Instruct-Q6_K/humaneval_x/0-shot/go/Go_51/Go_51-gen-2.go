    if(array.empty())
        return array;
    int sum = array[0] + array[array.size() - 1];
    if(sum % 2 == 0)
        sort(array.begin(), array.end(), greater<int>());
    else
        sort(array.begin(), array.end());
    return array;
}
int main() {
    vector<int> array = {2, 4, 3, 0, 1, 5};
    array = sort_array(array);
    for(int i = 0; i < array.size(); i++)
        printf("%d ", array[i]);
    printf("\n");
    return 0;
} 
