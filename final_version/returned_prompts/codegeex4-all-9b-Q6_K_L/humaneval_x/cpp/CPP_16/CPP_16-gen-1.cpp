int count=0;
vector<char> distinct;
for(int i=0;i<str.length();i++){
    //to ignore case
    char c=str[i]>='a'&&str[i]<='z'?str[i]:str[i]+'A'-'a';
    //to check whether it is already present or not
    if(find(distinct.begin(),distinct.end(),c)==distinct.end()){
        distinct.push_back(c);
        count++;
    }
}
return count;
}