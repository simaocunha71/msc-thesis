    vector<int> result;
    sort(numbers.begin(), numbers.end());
    for(int i = 0; i < numbers.size()-1; i++){
        if(numbers[i] != numbers[i+1]){
            result.push_back(numbers[i]);
        }
    }
    result.push_back(numbers[numbers.size()-1]);
    return result;
}

int main(){
    vector<int> v = {1, 2, 3, 2, 4};
    vector<int> v2 = remove_duplicates(v);
    for(int i = 0; i < v2.size(); i++){
        printf("%d ", v2[i]);
    }
    printf("\n");
    return 0;
}
E:
1 3 4 
