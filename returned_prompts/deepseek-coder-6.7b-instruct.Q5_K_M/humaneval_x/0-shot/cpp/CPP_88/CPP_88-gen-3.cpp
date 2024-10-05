    if(array.size()==0) return array;

    int sum = array[0] + array[array.size()-1];

    if(sum % 2 == 0){
        sort(array.begin(), array.end(), greater<int>());
    }else{
        sort(array.begin(), array.end());
    }

    return array;
}

// Test Cases
int main(){
    // Test case 1
    vector<int> array1 = {5};
    array1 = sort_array(array1);
    for(int i=0; i<array1.size(); i++) printf("%d ",array1[i]);
    printf("\n");

   