vector<int> result=array;
if(array.size()==0){
    return result;
}
int sum=array[0]+array[array.size()-1];
if(sum%2==0){
    sort(result.begin(), result.end(), greater<int>());
}else{
    sort(result.begin(), result.end());
}
return result;
}
int main(){
vector<int> array={2, 4, 3, 0, 1, 5, 6};
vector<int> result=sort_array(array);
for(int i=0; i<result.size(); i++){
    printf("%d ", result[i]);
}
printf("\n");
return 0;
}
*/




































































































































