vector<string> result;
for(int i=0;i<strings.size();i++){
    if(strings[i].substr(0, prefix.length()) == prefix){
        result.push_back(strings[i]);
    }
}
return result;
}