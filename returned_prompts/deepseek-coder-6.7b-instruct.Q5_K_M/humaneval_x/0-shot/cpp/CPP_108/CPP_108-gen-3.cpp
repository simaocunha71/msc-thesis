    int count = 0;
    for(int i=0; i<n.size(); i++){
        int sum = 0;
        if(n[i]<0){
            int first_digit = -1*(n[i]/10);
            int remaining = n[i]%10;
            sum = first_digit + remaining;
        }
        else{
            int first_digit = n[i]/10;
            int remaining = n[i]%10;
            sum = first_digit + remaining;
        }
        if(sum>0){
            count++;
        }
    }
    return count;
}


/*
