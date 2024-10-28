    string temp[100], temp2[100];
    int i=0, j, k=0;
    int count=0;
    while(s[i]!='\0'){
        if (s[i]==' '){
            temp[count]=temp2[k];
            k=0;
            count++;
        }
        else{
            temp2[k]=s[i];
            k++;
        }
        i++;
    }
    temp[count]=temp2[k];
    sort(temp, temp+count);
    k=0;
    i=0;
    while(temp[i]!='\0'){
        s[i]=temp[i];
        i++;
    }
    return s;
}






