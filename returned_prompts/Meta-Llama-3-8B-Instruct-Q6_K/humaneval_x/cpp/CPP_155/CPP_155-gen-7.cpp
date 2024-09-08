    vector<int> result;
    string str = to_string(num);
    int even_count = 0, odd_count = 0;
    for(int i=0; i<str.length(); i++){
        if(str[i]%2 == 0){
            even_count++;
        }else{
            odd_count++;
        }
    }
    result.push_back(even_count);
    result.push_back(odd_count);
    return result;
}

int main(){
    int num;
    cout<<"Enter a number: ";
    cin>>num;
    vector<int> result = even_odd_count(num);
    cout<<"Number of even digits: "<<result[0]<<endl;
    cout<<"Number of odd digits: "<<result[1]<<endl;
    return 0;
}*/



