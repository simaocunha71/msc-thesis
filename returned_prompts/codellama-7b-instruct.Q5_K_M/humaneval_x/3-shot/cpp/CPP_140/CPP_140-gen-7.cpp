    int i;
    int count;
    string new_text;
    char chr;
    for (i=0;i<text.length();i++){
        chr=text[i];
        if (chr==' '){
            count=1;
            while ((i+count<text.length())&&(text[i+count]==' ')){
                count+=1;
            }
            if (count>1){
                new_text+=to_string(count-1);
                new_text+="-";
            }
            else{
                new_text+="_";
            }
            i+=count-1;
        }
        else{
            new_text+=chr;
        }
    }
    return new_text;
}


