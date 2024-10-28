    vector<int> depths;
    stringstream ss(paren_string);
    string paren_group;

    while(getline(ss, paren_group, ' ')){
        int count = 0;
        int max = 0;
        for(char& c : paren_group){
            if(c == '(') {
                count++;
                if(count > max)
                    max = count;
            }
            else if(c == ')'){
                count--;
            }
        }
        depths.push_back(max);
    }
    return depths;
}
int main(){
    vector<int> depths = parse_nested_parens("(()()) ((())) () ((())()())");
    for(int depth : depths){
        printf("%d ", depth);
    }
    return 0;
}
*/

I have removed the syntax error from the code. I also added the missing C++ library `<sstream>`.
*/

