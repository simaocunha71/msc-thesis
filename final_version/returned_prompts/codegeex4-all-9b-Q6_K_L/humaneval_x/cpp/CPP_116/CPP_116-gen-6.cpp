vector<int> out={};
sort(arr.begin(), arr.end());
for(int i=0;i<arr.size();i++){
int count=0;
int num=arr[i];
while(num!=0){
num=num&(num-1);
count++;
}
out.push_back(count);
}
return out;
}

B:
vector<int> sort_array(vector<int> arr){
sort(arr.begin(), arr.end());
vector<int> out={};
for(int i=0;i<arr.size();i++){
int count=0;
int num=arr[i];
while(num!=0){
num=num&(num-1);
count++;
}
out.push_back(count);
}
return out;
}

C:
vector<int> sort_array(vector<int> arr){
vector<int> out={};
for(int i=0;i<arr.size();i++){
int count=0;
int num=arr[i];
while(num!=0){
num=num&(num-1);
count++;
}
out.push_back(count);
}
sort(out.begin(),out.end());
return out;
}

D:
vector<int> sort_array(vector<int> arr){
vector<int> out={};
for(int i=0;i<arr.size();i++){
int count=0;
int num=arr[i];
while(num!=0){
num=num&(num-1);
count++;
}
out.push_back(count);
}
sort(arr.begin(), arr.end());
return out;
}

E:
vector<int> sort_array(vector<int> arr){
vector<int> out={};
for(int i=0;i<arr.size();i++){
int count=0;
int num=arr[i];
while(num!=0){
num=num&(num-1);
count++;
}
out.push_back(count);
}
sort(out.begin(), out.end());
sort(arr.begin(), arr.end());
return arr;
}

F:
vector<int> sort_array(vector<int> arr){
vector<int> out={};
for(int i=0;i<arr.size();i++){
int count=0;
int num=arr[i];
while(num!=0){
num=num&(num-1);
count++;
}
out.push_back(count);
}
sort(out.begin(), out.end());
sort(arr.begin(), arr.end());
return out;
}

G:
vector<int> sort_array(vector<int> arr){
vector<int> out={};
for(int i=0;i<arr.size();i++){
int count=0;
int num=arr[i];
while(num!=0){
num=num&(num-1);
count++;
}
out.push_back(count);
}
sort(out.begin(), out.end());
sort(arr.begin