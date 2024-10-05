    string result;
    int number_length=0;
    int temp_x=x;
    while (temp_x!=0){
        temp_x/=10;
        number_length+=1;
    }
    int i;
    if (shift>number_length){
        for (i=number_length-1;i>=0;i--)
        result+=x%10;
        x/=10;
        while (x!=0){
            result+=x%10;
            x/=10;
        }
        return result;
    }
    else {
        for (i=0;i<number_length-shift;i++)
        result+=x%10;
        x/=10;
        while (x!=0){
            result+=x%10;
            x/=10;
        }
        return result;
    }
}


