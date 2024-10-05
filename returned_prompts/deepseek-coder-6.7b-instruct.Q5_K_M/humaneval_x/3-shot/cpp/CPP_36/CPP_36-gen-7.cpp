    int count=0;
    for (int i=11; i<n; i++){
        if (i%11==0 || i%13==0){
            int temp=i;
            while(temp){
                if (temp%10==7) count++;
                temp /= 10;
            }
        }
    }
    return count;
}

