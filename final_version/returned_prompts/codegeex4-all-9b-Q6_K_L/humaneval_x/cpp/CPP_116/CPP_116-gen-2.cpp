    for(int i=0;i<arr.size();i++){
        int temp=arr[i];
        for(int j=i+1;j<arr.size();j++){
            int count1=0;
            int count2=0;
            int n1=temp;
            int n2=arr[j];
            while(n1>0){
                if(n1%2==1) count1++;
                n1=n1/2;
            }
            while(n2>0){
                if(n2%2==1) count2++;
                n2=n2/2;
            }
            if(count1>count2){
                int t=arr[i];
                arr[i]=arr[j];
                arr[j]=t;
            }
            else if(count1==count2 && temp>arr[j]){
                int t=arr[i];
                arr[i]=arr[j];
                arr[j]=t;
            }
        }
    }
    return arr;
}
B:
    for(int i=0;i<arr.size();i++){
        int temp=arr[i];
        for(int j=i+1;j<arr.size();j++){
            int count1=0;
            int count2=0;
            int n1=temp;
            int n2=arr[j];
            while(n1>0){
                if(n1%2==1) count1++;
                n1=n1/2;
            }
            while(n2>0){
                if(n2%2==1) count2++;
                n2=n2/2;
            }
            if(count1>count2){
                int t=arr[i];
                arr[i]=arr[j];
                arr[j]=t;
            }
            else if(count1==count2 && temp>arr[j]){
                int t=arr[i];
                arr[i]=arr[j];
                arr[j]=t;
            }
        }
    }
    return arr;
}
C:
    for(int i=0;i<arr.size();i++){
        int temp=arr[i];
        for(int j=i+1;j<arr.size();j++){
            int count1=0;
            int count2=0;
            int n1=temp;
            int n2=arr[j];
            while(n1>0){
                if(n1%2==1) count1++;
                n1=n1/2;
            }
            while(n2>0){
                if(n2%2==1) count2++;
                n2=n2/2;
