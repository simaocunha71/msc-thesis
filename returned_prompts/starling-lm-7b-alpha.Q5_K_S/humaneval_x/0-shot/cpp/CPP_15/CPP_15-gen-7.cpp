    if(array[0]>n)
        return -1;
    else if(array[0]==n)
        return 0;
    else if(array[array.size()-1]<=n)
        return array.size()-1;
    else{
        int l=0,r=array.size()-1,mid=(l+r)/2;
        while(l<r-1){
            if(array[mid]>n)
                r=mid;
            else if(array[mid]<=n)
                l=mid;
            mid=(l+r)/2;
        }
        if(array[mid]>n)
            return mid-1;
        else if(array[mid]<=n)
            return mid;
    }
}





/*
Return the index of the first element in the array that is smaller than the given number
>>> binary_search(nil, 0)
-1
>>> binary_search([0, 1, 2, 3], 0)
-1
>>> binary_search([0, 1, 2, 3], 1)
0
>>> binary_search([0, 1, 2, 3], 2)
1