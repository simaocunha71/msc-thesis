    if(lst.size()<2){
        return NULL;
    }
    sort(lst.begin(), lst.end());
    for(int i = 1; i < lst.size(); i++){
        if(lst[i] != lst[0]){
            return lst[i];
        }
    }
    return NULL;
}

int main(){
    vector<int> v1 = {1, 2, 3, 4, 5};
    vector<int> v2 = {5, 1, 4, 3, 2};
    vector<int> v3 = {};
    vector<int> v4 = {1, 1};

    printf("%d\n", next_smallest(v1));
    printf("%d\n", next_smallest(v2));
    printf("%d\n", next_smallest(v3));
    printf("%d\n", next_smallest(v4));
    return 0;
}

*/

// C++

/*
