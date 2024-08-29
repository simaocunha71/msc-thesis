    sort(arr.begin(),arr.end(),greater<int>());
    vector<int> result(arr.begin(),arr.begin()+k);
    return result;
}
int main(){
    vector<int> arr1 = {-3, -4, 5};
    vector<int> arr2 = {4, -4, 4};
    vector<int> arr3 = {-3, 2, 1, 2, -1, -2, 1};
    vector<int> arr4 = {4, -4, 4, 4, 2, 2};
    vector<int> arr5 = {-3, 2, 1, 2, -1, -2, 1, 3, 3, 3, 3, 3};
    printf("arr1 = ");
    for(int i = 0;i < arr1.size();i++){
        printf("%d ",arr1[i]);
    }
    printf("\n");
    printf("arr2 = ");
    for(int i = 0;i < arr2.size();i++){
        printf("%d ",arr2[i]);
    }
    printf("\n");
    printf("arr3 = ");
    for(int i = 0;i < arr3.size();i++){
        printf("%d ",arr3[i]);
    }
    printf("\n");
    printf("arr4 = ");
    for(int i = 0;i < arr4.size();i++){
        printf("%d ",arr4[i]);
    }
    printf("\n");
    printf("arr5 = ");
    for(int i = 0;i < arr5.size();i++){
        printf("%d ",arr5[i]);
    }
    printf("\n");
    vector<int> result1 = maximum(arr1,3);
    vector<int> result2 = maximum(arr2,2);
    vector<int> result3 = maximum(arr3,1);
    vector<int> result4 = maximum(arr4,2);
    vector<int> result5 = maximum(arr5,3);
    printf("result1 = ");
    for(int i = 0;i < result1.size();i++){
        printf("%d ",result1[i]);
    }
    printf("\n");
    printf("result2 = ");
    for(int i = 0;i < result2.size();i++){
        printf("%d ",result2[i]);
    }
    printf("\n");
    printf("result3 = ");
    for(int i = 0;i < result3.size();i