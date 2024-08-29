string longest;
int max=0;
for(int i=0;i<strings.size();i++){
    if(strings[i].size()>max){
        max=strings[i].size();
        longest=strings[i];
    }
}
return longest;
}

