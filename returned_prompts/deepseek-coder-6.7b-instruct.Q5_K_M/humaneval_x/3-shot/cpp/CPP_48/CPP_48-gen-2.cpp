    int i;
    int j=text.length()-1;
    for(i=0;i<j;i++,j--){
        if(text[i] != text[j]){
            return false;
        }
    }
    return true;
}


