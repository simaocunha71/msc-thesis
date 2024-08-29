vector<float> odd;
vector<float> even;
for(int i=0;i<l.size();i++){
if(i%2==1){
odd.push_back(l[i]);
}
else{
even.push_back(l[i]);
}
}
sort(odd.begin(),odd.end());
sort(even.begin(),even.end());
vector<float> r;
for(int i=0;i<l.size();i++){
if(i%2==1){
r.push_back(odd[i]);
}
else{
r.push_back(even[i]);
}
}
return r;
}
int main(){
vector<float> l={1,2,3,4,5,6};
vector<float> r=sort_even(l);
for(int i=0;i<r.size();i++){
printf("%f ",r[i]);
}
return 0;
}
输出：
1.000000 2.000000 3.000000 4.000000 5.000000 6.000000
