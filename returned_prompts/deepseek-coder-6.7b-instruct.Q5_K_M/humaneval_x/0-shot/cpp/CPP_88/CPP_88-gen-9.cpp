    vector<int> sorted(array);
    if(array.size()==0){
        return array;
    }
    else{
        int sum = array[0] + array[array.size()-1];
        if(sum%2==0){
            sort(sorted.begin(), sorted.end(), greater<int>());
        }
        else{
            sort(sorted.begin(), sorted.end());
        }
        return sorted;
    }
}
int main(){
    vector<int> vec =