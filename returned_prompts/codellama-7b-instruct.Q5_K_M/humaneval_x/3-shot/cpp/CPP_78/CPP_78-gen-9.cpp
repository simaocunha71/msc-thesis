    int i;
    int count=0;
    int prime[10] = {2,3,5,7,11,13,17,19,23,29};
    int hex[16] = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};
    for (i=0;i<num.length();i++)
    {
        if (hex[num[i]]<=7){
            count++;
        }
    }
    return count;
}




