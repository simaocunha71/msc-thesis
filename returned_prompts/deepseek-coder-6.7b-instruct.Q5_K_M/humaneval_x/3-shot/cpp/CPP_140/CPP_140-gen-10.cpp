    string result="";
    bool space=false;
    for(int i=0; i<text.size(); i++){
        if(text[i]==' '){
            if(space){
                result+='-';
            }
            else{
                result+='_';
            }
            space=true;
        }
        else{
            result+=text[i];
            space=false;
        }
    }
    return result;
}


