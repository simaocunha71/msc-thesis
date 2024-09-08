    if(array.empty()) return array;
    int sum = array[0] + array[array.size()-1];
    vector<int> result = array;
    if(sum % 2 == 0){
        sort(result.begin(), result.end(), greater<int>());
    }
    else{
        sort(result.begin(), result.end());
    }
    return result;
}

int main(){
    vector<int> test = {2, 4, 3, 0, 1, 5};
    vector<int> result = sort_array(test);
    for(int i : result){
        printf("%d ", i);
    }
    return 0;
}

