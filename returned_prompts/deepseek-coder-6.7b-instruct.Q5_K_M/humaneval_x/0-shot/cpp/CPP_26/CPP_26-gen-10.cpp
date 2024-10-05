    sort(numbers.begin(), numbers.end());
    for(int i = 0; i < numbers.size()-1; i++){
        if(numbers[i] == numbers[i+1]){
            numbers.erase(numbers.begin()+i);
            i--;
        }
    }
    return numbers;
}

int main(){
    vector<int> numbers = {1, 2, 3, 2, 4};
    vector<int> result = remove_duplicates(numbers);
    for(int i = 0; i < result.size(); i++){
        printf("%d ", result[i]);
    }
    return 0;
}
*/

*/

/*
