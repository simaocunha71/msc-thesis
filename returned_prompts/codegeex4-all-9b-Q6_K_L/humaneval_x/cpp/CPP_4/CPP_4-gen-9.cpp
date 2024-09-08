    float sum=0;
    int len=numbers.size();
    for(int i=0;i<len;i++){
        sum+=numbers[i];
    }
    float mean=sum/len;
    float sum2=0;
    for(int i=0;i<len;i++){
        sum2+=abs(numbers[i]-mean);
    }
    float mad=sum2