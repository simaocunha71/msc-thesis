
vector<string> result;
string temp="";
for(int i=0;i<s.length();i++){
    if(s[i]==' '){
        int count=0;
        for(int j=0;j<temp.length();j++){
            if(temp[j]=='a'||temp[j]=='e'||temp[j]=='i'||temp[j]=='o'||temp[j]=='u'||temp[j]=='A'||temp[j]=='E'||temp[j]=='I'||temp[j]=='O'||temp[j]=='U'){
                continue;
            }
            else{
                count++;
            }
        }
        if(count==n){
            result.push_back(temp);
        }
        temp="";
    }
    else{
        temp+=s[i];
    }
}
int count=0;
for(int j=0;j<temp.length();j++){
    if(temp[j]=='a'||temp[j]=='e'||temp[j]=='i'||temp[j]=='o'||temp[j]=='u'||temp[j]=='A'||temp[j]=='E'||temp[j]=='I'||temp[j]=='O'||temp[j]=='U'){
        continue;
    }
    else{
        count++;
    }
}
if(count==n){
    result.push_back(temp);
}
return result;
}

*/


















































































































