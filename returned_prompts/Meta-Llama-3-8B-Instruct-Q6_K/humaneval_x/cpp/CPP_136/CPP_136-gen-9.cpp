    vector<int> result;
    int largest_negative = 0;
    int smallest_positive = 0;
    
    for(int i = 0; i < lst.size(); i++){
        if(lst[i] < 0 && lst[i] > largest_negative){
            largest_negative = lst[i];
        }
        else if(lst[i] > 0 && lst[i] < smallest_positive){
            smallest_positive = lst[i];
        }
    }
    
    if(largest_negative == 0 && smallest_positive == 0){
        result.push_back(0);
        result.push_back(0);
    }
    else if(largest_negative == 0){
        result.push_back(0);
        result.push_back(smallest_positive);
    }
    else if(smallest_positive == 0){
        result.push_back(largest_negative);
        result.push_back(0);
    }
    else{
        result.push_back(largest_negative);
        result.push_back(smallest_positive);
    }
    
    return result;
}

int main(){
    vector<int> lst1 = {2, 4, 1, 3, 5, 7};
    vector<int> result1 = largest_smallest_integers(lst1);
    printf("Largest smallest integers for lst1: {%d, %d}\n", result1[0], result1[1]);
    
    vector<int> lst2 = {};
    vector<int> result2 = largest_smallest_integers(lst2);
    printf("Largest smallest integers for lst2: {%d, %d}\n", result2[0], result2[1]);
    
    vector<int> lst3 = {0};
    vector<int> result3 = largest_smallest_integers(lst3);
    printf("Largest smallest integers for lst3: {%d, %d}\n", result3[0], result3[1]);
    
    return 0;
}C:
}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C:}C