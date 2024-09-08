    map<char, int> result;
    for(int i = 0; i < test.length(); i++){
        char c = test[i];
        if(result.find(c) == result.end()){
            result[c] = 1;
        }else{
            result[c]++;
        }
    }
    int max = 0;
    for(auto it = result.begin(); it != result.end(); it++){
        if(it->second > max){
            max = it->second;
        }
    }
    for(auto it = result.begin(); it != result.end(); it++){
        if(it->second == max){
            cout << "{" << it->first << "," << it->second << "}" << endl;
        }
    }
    return result;
}

int main(){
    string test = "a b c";
    map<char, int> result = histogram(test);
    return 0;
}
Output:

{
a, 1}
{
b, 1}
{
c, 1}

