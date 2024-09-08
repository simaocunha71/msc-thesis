    if(array.empty()){
        return array;
    }
    int sum = array[0] + array.back();
    if(sum % 2 == 0){
        sort(array.begin(), array.end(), greater<int>());
    }else{
        sort(array.begin(), array.end());
    }
    return array;
}
int main(){
    vector<int> array1 = {};
    vector<int> array2 = {5};
    vector<int> array3 = {2, 4, 3, 0, 1, 5};
    vector<int> array4 = {2, 4, 3, 0, 1, 5, 6};
    printf("Array1: ");
    for(auto it = array1.begin(); it != array1.end(); it++){
        printf("%d ", *it);
    }
    printf("\n");
    array1 = sort_array(array1);
    printf("Sorted Array1: ");
    for(auto it = array1.begin(); it != array1.end(); it++){
        printf("%d ", *it);
    }
    printf("\n");
    printf("Array2: ");
    for(auto it = array2.begin(); it != array2.end(); it++){
        printf("%d ", *it);
    }
    printf("\n");
    array2 = sort_array(array2);
    printf("Sorted Array2: ");
    for(auto it = array2.begin(); it != array2.end(); it++){
        printf("%d ", *it);
    }
    printf("\n");
    printf("Array3: ");
    for(auto it = array3.begin(); it != array3.end(); it++){
        printf("%d ", *it);
    }
    printf("\n");
    array3 = sort_array(array3);
    printf("Sorted Array3: ");
    for(auto it = array3.begin(); it != array3.end(); it++){
        printf("%d ", *it);
    }
    printf("\n");
    printf("Array4: ");
    for(auto it = array4.begin(); it != array4.end(); it++){
        printf("%d ", *it);
    }
    printf("\n");
    array4 = sort_array(array4);
    printf("Sorted Array4: ");
    for(auto it = array4.begin(); it != array4.end(); it++){
        printf("%d ", *it);
    }
    printf("\n");
    return 0;
}
Output:
Array1: 
Sorted Array1: 
Array2: 5 
