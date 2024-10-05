    string temp;
    int i,j;
    for(i=0;i<b.length();i++){
        temp=b.substr(i)+b.substr(0,i);
        for(j=0;j<=a.length()-temp.length();j++){
            if(a.substr(j,temp.length())==temp)
                return true;
        }
    }
    return false;
}


