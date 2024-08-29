vector<string> out;
for(string str:strings){
    if(str.find(prefix)==0){
        out.push_back(str);
    }
}
return out;
}