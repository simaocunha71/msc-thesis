    string result;
    int i=0,j=0;
    while(i<a.length() && j<b.length()){
        if(a[i]==b[j]){
            i++;
            j++;
        }
        else{
            result.push_back(a[i]^b[j]);
            i++;
            j++;
        }
    }
    while(i<a.length()){
        result.push_back(a[i]^'0');
        i++;
    }
    while(j<b.length()){
        result.push_back(b[j]^'0');
        j++;
    }
    return result;
}

