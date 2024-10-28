vector<string> v;
string planets[]={"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"};
int i,j;
for(i=0;i<planets.size();i++){
if(planets[i]==planet1){
for(j=i+1;j<8;j++){
v.push_back(planets[j]);
}
break;
}
}
if(v.size()==0){
return v;
}
for(i=0;i<v.size();i++){
if(v[i]==planet2){
v.erase(v.begin()+i);
break;
}
}
if(v.size()==0){
return v;
}
for(i=0;i<8;i++){
if(planets[i]==planet2){
v.push_back(planets[i]);
break;
}
}
return v;
}
int main(){
vector<string> v;
v=bf("Jupiter","Neptune");
for(int i=0;i<v.size();i++){
cout<<v[i]<<" ";
}
return 0;
}
