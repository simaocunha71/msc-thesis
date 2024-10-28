vector<string> arr = {"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"};
vector<string> res;

for(int i = 0;i < arr.size();i++){
if(planet1 == arr[i]){
res.push_back(arr[i]);
if(i < arr.size() - 1){
for(int j = i + 1;j < arr.size();j++){
if(planet2 == arr[j]){
res.push_back(arr[j]);
break;
}
}
}
break;
}
}

for(int i = arr.size() - 2;i >= 0;i--){
if(planet1 == arr[i]){
res.push_back(arr[i]);
if(i > 0){
for(int j = i - 1;j >= 0;j--){
if(planet2 == arr[j]){
res.push_back(arr[j]);
break;
}
}
}
break;
}
}

for(int i = 0;i < arr.size();i++){
if(planet1 != arr[i] && planet2 != arr[i] && res.size() == 0){
res.push_back(arr[i]);
}
}
return res;
}

int main() {
    printf("%s\n", bf("Jupiter", "Neptune").data());
    printf("%s\n", bf("Earth", "Mercury").data());
    printf("%s\n", bf("Mercury", "Uranus").data());
}











































































































