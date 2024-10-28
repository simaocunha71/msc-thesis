    //your code here
}

int main(){
    vector<int> arr = {5, 0, 3, 0, 4, 2};
    vector<int> result = pluck(arr);
    for(auto i: result){
        printf("%d ", i);
    }
    printf("\n");
    return 0;
}
