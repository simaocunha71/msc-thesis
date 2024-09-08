long long min_sum = LLONG_MAX;
long long current_sum = 0;
for(int i = 0; i < nums.size(); i++){
if(current_sum < 0){
current_sum = 0;
}
current_sum += nums[i];
if(current_sum < min_sum){
min_sum = current_sum;
}
}
if(min_sum == LLONG_MAX){
return 0;
}
return min_sum;

B:
long long min_sum = LLONG_MAX;
long long current_sum = 0;
for(int i = 0; i < nums.size(); i++){
if(current_sum > 0){
current_sum = 0;
}
current_sum += nums[i];
if(current_sum < min_sum){
min_sum = current_sum;
}
}
if(min_sum == LLONG_MAX){
return 0;
}
return min_sum;

C:
long long min_sum = LLONG_MAX;
long long current_sum = 0;
for(int i = 0; i < nums.size(); i++){
if(current_sum < 0){
current_sum = 0;
}
current_sum += nums[i];
if(current_sum < min_sum){
min_sum = current_sum;
}
}
if(min_sum == LLONG_MAX){
return 0;
}
return min_sum;

D:
long long min_sum = LLONG_MAX;
long long current_sum = 0;
for(int i = 0; i < nums.size(); i++){
if(current_sum > 0){
current_sum = 0;
}
current_sum += nums[i];
if(current_sum < min_sum){
min_sum = current_sum;
}
}
if(min_sum == LLONG_MAX){
return 0;
}
return min_sum;

E:
long long min_sum = LLONG_MAX;
long long current_sum = 0;
for(int i = 0; i < nums.size(); i++){
if(current_sum < 0){
current_sum = 0;
}
current_sum += nums[i];
if(current_sum < min_sum){
min_sum = current_sum;
}
}
if(min_sum == LLONG_MAX){
return 0;
}
return min_sum;

F:
long long min_sum = LLONG_MAX;
long long current_sum = 0;
for(int i = 0; i < nums.size(); i++){
if(current_sum > 0){
current_sum = 0;
}
current_sum += nums[i];
if(current_sum < min_sum){
min_sum = current_sum;
}
}
if(min_sum == LLONG_MAX){
return 0;
}
return min_sum;

G:
long long