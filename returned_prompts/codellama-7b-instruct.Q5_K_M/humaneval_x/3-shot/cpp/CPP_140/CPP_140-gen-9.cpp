    int i;
    int count=0;
    for (i=0;i<text.length();i++)
    if (text[i]==' '){
        count+=1;
        if (count==2)
        text.replace(i,1,"-");
        else
        text.replace(i,1,"_");
    }
    return text;
}


