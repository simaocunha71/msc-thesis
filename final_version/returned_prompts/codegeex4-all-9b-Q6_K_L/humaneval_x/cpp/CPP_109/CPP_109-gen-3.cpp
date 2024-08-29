    for(int i=0;i<arr.size();i++){
        int j=0;
        while(j<arr.size()-1){
            if(arr[j]>arr[j+1]){
                int temp=arr[j+1];
                arr[j+1]=arr[j];
                arr[j]=temp;
            }
            j++;
        }
    }
    for(int i=0;i<arr.size()-1;i++){
        if(arr[i]>arr[i+1]) goto A;
    }
    return true;

B:
    for(int i=0;i<arr.size();i++){
        int j=0;
        while(j<arr.size()-1){
            if(arr[j]>arr[j+1]){
                int temp=arr[j+1];
                arr[j+1]=arr[j];
                arr[j]=temp;
            }
            j++;
        }
    }
    for(int i=0;i<arr.size()-1;i++){
        if(arr[i]>arr[i+1]) goto B;
    }
    return true;

C:
    for(int i=0;i<arr.size();i++){
        int j=0;
        while(j<arr.size()-1){
            if(arr[j]>arr[j+1]){
                int temp=arr[j+1];
                arr[j+1]=arr[j];
                arr[j]=temp;
            }
            j++;
        }
    }
    for(int i=0;i<arr.size()-1;i++){
        if(arr[i]>arr[i+1]) goto C;
    }
    return true;
    
