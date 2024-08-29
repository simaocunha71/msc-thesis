/*Write your code here*/
    return false;
}
int main()
{
    int size;
    scanf("%d",&size);
    vector<int> arr(size);
    for(int i=0;i<size;i++){
        scanf("%d",&arr[i]);
    }
    bool result=move_one_ball(arr);
    if(result==true){
        printf("true\n");
    }
    else{
        printf("false\n");
    }
    return 0;
}

