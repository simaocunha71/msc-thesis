    int size = arr.size();
    if(size==0) return {};
    int smallest_even = 10001, index = -1;
    for(int i=0; i<size; i++){
        if(arr[i] % 2 == 0 && arr[i] < smallest_even){
            smallest_even = arr[i];
            index = i;
        }
    }
    if(index == -1) return {};
    return {smallest_even, index};
}

int main(){
    vector<