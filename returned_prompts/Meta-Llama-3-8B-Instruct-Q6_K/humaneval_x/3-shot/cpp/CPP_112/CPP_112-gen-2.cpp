    string result;
    for(int i=0;i<s.length();i++){
        bool found=false;
        for(int j=0;j<c.length();j++){
            if(s[i]==c[j]){
                found=true;
                break;
            }
        }
        if(!found){
            result+=s[i];
        }
    }
    string temp=result;
    reverse(temp.begin(),temp.end());
    if(result==temp){
        return {result,"True"};
    }else{
        return {result,"False"};
    }
}
