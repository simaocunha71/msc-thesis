vector<string> vec;
for(auto c:s){
if(c==' ') continue;
else if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u') continue;
else{
vec.push_back(c);
}
}
for(auto c:s){
if(c==' ') continue;
else if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u') continue;
else{
vec.push_back(c);
}
}
return vec;
}

