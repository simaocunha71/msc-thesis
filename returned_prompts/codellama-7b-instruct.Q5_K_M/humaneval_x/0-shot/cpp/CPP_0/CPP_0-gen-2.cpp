    for(int i=0; i<numbers.size()-1; i++){
        for(int j=i+1; j<numbers.size(); j++){
            if(fabs(numbers[i]-numbers[j])<threshold) return true;
        }
    }
    return false;
}
int main(){
    vector<float> numbers = {1.0, 2.0, 3.0};
    cout<<has_close_elements(numbers, 0.5)<<endl;
    vector<float> numbers1 = {1.0, 2.8, 3.0, 4.0, 5.0, 2.0};
    cout<<has_close_elements(numbers1, 0.3)<<endl;
    return 0;
}
