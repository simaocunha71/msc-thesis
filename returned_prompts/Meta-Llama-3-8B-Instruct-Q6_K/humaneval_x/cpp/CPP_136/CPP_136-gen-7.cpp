    vector<int> result;
    if(lst.empty()){
        result.push_back(0);
        result.push_back(0);
    }
    else{
        int max_neg = INT_MIN;
        int min_pos = INT_MAX;
        for(int i = 0; i < lst.size(); i++){
            if(lst[i] < 0){
                if(lst[i] > max_neg){
                    max_neg = lst[i];
                }
            }
            else if(lst[i] > 0){
                if(lst[i] < min_pos){
                    min_pos = lst[i];
                }
            }
        }
        if(max_neg == INT_MIN){
            result.push_back(0);
        }
        else{
            result.push_back(max_neg);
        }
        if(min_pos == INT_MAX){
            result.push_back(0);
        }
        else{
            result.push_back(min_pos);
        }
    }
    return result;
}

int main(){
    printf("%d %d\n", largest_smallest_integers({2, 4, 1, 3, 5, 7}).at(0), largest_smallest_integers({2, 4, 1, 3, 5, 7}).at(1));
    return 0;
}

