    int n = arr.size();
    if(n == 0)
        return true;
    if(n == 1)
        return true;
    if(n == 2)
        return arr[0] < arr[1];
    
    // if(arr[0] < arr[n-1]){
    //     arr[n-1] = arr[0];
    //     arr[0] = 0;
    //     goto A;
    // }
    // if(arr[1] < arr[n-2]){
    //     arr[n-2] = arr[1];
    //     arr[1] = 0;
    //     goto A;
    // }
    // if(arr[2] < arr[n-3]){
    //     arr[n-3] = arr[2];
    //     arr[2] = 0;
    //     goto A;
    // }
    // if(arr[3] < arr[n-4]){
    //     arr[n-4] = arr[3];
    //     arr[3] = 0;
    //     goto A;
    // }
    // if(arr[4] < arr[n-5]){
    //     arr[n-5] = arr[4];
    //     arr[4] = 0;
    //     goto A;
    // }
    // if(arr[5] < arr[n-6]){
    //     arr[n-6] = arr[5];
    //     arr[5] = 0;
    //     goto A;
    // }
    // if(arr[6] < arr[n-7]){
    //     arr[n-7] = arr[6];
    //     arr[6] = 0;
    //     goto A;
    // }
    // if(arr[7] < arr[n-8]){
    //     arr[n-8] = arr[7];
    //     arr[7] = 0;
    //     goto A;
    // }
    // if(