    string result="";
    for(int i=0;i<message.length();i++){
        if (message[i]=='a'||message[i]=='e'||message[i]=='i'||message[i]=='o'||message[i]=='u'){
            result+=(char)(message[i]+2);
        }
        else if (message[i]=='A'||message[i]=='E'||message[i]=='I'||message[i]=='O'||message[i]=='U'){
            result+=(char)(message[i]+2);
        }
        else if (message[i]==' '){
            result+=' ';
        }
        else{
            result+=(char)(message[i]-32);
        }
    }
    return result;
}


