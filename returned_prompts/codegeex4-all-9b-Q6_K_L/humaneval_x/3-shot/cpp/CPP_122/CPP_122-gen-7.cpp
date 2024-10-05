    int sum=0;
    for (int i=0;i<k;i++){
        if (arr[i]<10){
            sum+=arr[i];
        }
        else{
            int first_digit=arr[i]/10;
            sum+=first_digit;
        }
    }
    return sum;
}