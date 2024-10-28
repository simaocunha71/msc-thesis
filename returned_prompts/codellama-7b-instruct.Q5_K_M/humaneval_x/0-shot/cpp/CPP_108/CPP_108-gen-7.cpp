    return 0;
}
int main(){
    vector<int> nums;
    int num;
    printf("Please enter the number of elements: ");
    scanf("%d", &num);
    for(int i = 0; i < num; i++){
        printf("Please enter the elements: ");
        scanf("%d", &num);
        nums.push_back(num);
    }
    printf("Number of elements with a sum of digits > 0 is: %d", count_nums(nums));
    return 0;
}
