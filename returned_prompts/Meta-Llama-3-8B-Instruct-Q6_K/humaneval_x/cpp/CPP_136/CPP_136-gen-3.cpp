    vector<int> result;
    int max_negative = INT_MIN;
    int min_positive = INT_MAX;

    for(int i = 0; i < lst.size(); i++){
        if(lst[i] < 0 && lst[i] > max_negative){
            max_negative = lst[i];
        }
        else if(lst[i] > 0 && lst[i] < min_positive){
            min_positive = lst[i];
        }
    }

    if(max_negative == INT_MIN){
        result.push_back(0);
    }
    else{
        result.push_back(max_negative);
    }

    if(min_positive == INT_MAX){
        result.push_back(0);
    }
    else{
        result.push_back(min_positive);
    }

    return result;
}

int main(){
    vector<int> lst = {2, 4, 1, 3, 5, 7};
    vector<int> result = largest_smallest_integers(lst);
    for(int i = 0; i < result.size(); i++){
        printf("%d ", result[i]);
    }
    printf("\n");

    return 0;
}
