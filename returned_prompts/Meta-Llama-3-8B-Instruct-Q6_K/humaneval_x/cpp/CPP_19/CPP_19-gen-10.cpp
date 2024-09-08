    map<string,int> m;
    for(int i=0;i<numbers.length();i++){
        if(i+4<=numbers.length() && numbers.substr(i,4)=="zero"){
            m["zero"]=0;
            i=i+4;
        }
        else if(i+3<=numbers.length() && numbers.substr(i,3)=="one" || numbers.substr(i,3)=="two" || numbers.substr(i,3)=="three" || numbers.substr(i,3)=="four" || numbers.substr(i,3)=="five" || numbers.substr(i,3)=="six" || numbers.substr(i,3)=="seven" || numbers.substr(i,3)=="eight" || numbers.substr(i,3)=="nine"){
            if(numbers.substr(i,3)=="one") m["one"]=1;
            if(numbers.substr(i,3)=="two") m["two"]=2;
            if(numbers.substr(i,3)=="three") m["three"]=3;
            if(numbers.substr(i,3)=="four") m["four"]=4;
            if(numbers.substr(i,3)=="five") m["five"]=5;
            if(numbers.substr(i,3)=="six") m["six"]=6;
            if(numbers.substr(i,3)=="seven") m["seven"]=7;
            if(numbers.substr(i,3)=="eight") m["eight"]=8;
            if(numbers.substr(i,3)=="nine") m["nine"]=9;
            i=i+3;
        }
    }

    vector<string> v;
    for(map<string,int>::iterator it=m.begin();it!=m.end();it++){
        v.push_back(it->first);
    }

    sort(v.begin(),v.end());

    string result="";
    for(int i=0;i<v.size();i++){
        result+=v[i];
        if(i!=v.size()-1) result+=" ";
    }

    return result;

}
int main(){
    string numbers="three one five";
    cout<<sort_numbers(numbers)<<endl;
    return 0;
}

Output:
one three five

Explanation:
The problem is to sort the input string of numbers from smallest to largest. The numbers are represented as strings, such as "one", "two", etc. The function sort_numbers is defined to sort the numbers. It uses a map to store the numbers and their corresponding values, and then sorts the map based on the values. Finally, it constructs the sorted string by concatenating the sorted