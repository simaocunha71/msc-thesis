        int n=arr.size();
        if(n==0)return true;
        int max=arr.get(0);
        int maxInd=0;
        for(int i=1;i<n;i++){
            if(arr.get(i)>max){
                maxInd=i;
                max=arr.get(i);
            }
        }
        for(int i=0;i<n;i++){
            if(arr.get(i)==max)continue;
            arr.set(i,arr.get(i)+arr.get(maxInd));
            arr.set(maxInd,arr.get(i)-arr.get(maxInd));
            arr.set(i,arr.get(i)-arr.get(maxInd));
        }
        arr.set(n-1,arr.get(n-1)-arr.get(maxInd));
        arr.set(maxInd,arr.get(maxInd)+arr.get(n-1));
        arr.set(n-1,arr.get(n-1)+arr.get(maxInd));
        return isNonDecreasing(arr);
    }

    private boolean isNonDecreasing(List<Integer> arr){
        int n=arr.size();
        for(int i=0;i<n-1;i++){
            if(arr.get(i)>arr.get(i+1))return false;
        }
        return true;
    }
}

