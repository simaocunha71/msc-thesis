    vector<int> sorted(array.size());
    for(int i=0; i<array.size(); i++){
        sorted[i] = array[i];
    }
    sort(sorted.begin(), sorted.end());

    if(array.size() == 0 || array.size() == 1)
        return sorted;

    int sum = 0;
    for(int i = 0; i<array.size(); i++){
        sum += array[i];
    }
    if(sum % 2 == 0){
        sort(sorted.rbegin(), sorted.rend());
    }

    return sorted;
}

int main() {

    vector<int> array = {2, 4, 3, 0, 1, 5, 6};
    vector<int> sorted = sort_array(array);
    for(int i=0; i<sorted.size(); i++){
        printf("%d ", sorted[i]);
    }
    return 0;
}

