string res="";
for (int i=0;i<s.length();i++){
    if (s[i]>='a'&&s[i]<='z'){
        res+=((s[i]-97+2*2)%26+97);
    }
    else if (s[i]>='A'&&s[i]<='Z'){
        res+=((s[i]-65+2*2)%26+65);
    }
    else{
        res+=s[i];
    }
}
return res;
}