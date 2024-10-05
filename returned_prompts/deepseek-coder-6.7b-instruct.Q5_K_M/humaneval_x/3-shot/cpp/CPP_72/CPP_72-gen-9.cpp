I'm sorry, but the code you posted seems to contain syntax errors. 

Here is the corrected version:

1:
bool has_close_elements(vector<float> numbers, float threshold){
    for  (int i=0; i<numbers.size()-1; i++){
        for  (int j=i+1; j<numbers.size(); j++){
            if  (abs(numbers[i]-numbers[j])<threshold)
                return true;
        }
    }
    return false;
}

2:
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    for  (int i=0; i<paren_string.length(); i++){
        chr=paren_string[i];
        if  (chr=='(')
        {
            level+=1;
            current_paren+=chr;
        }
        if  (chr==')')
        {
            level-=1;
            current_paren+=chr;
            if  (level==0){
                all_parens.push_back(current_paren);
                current_paren="";
             }
        }
    }
    return all_parens;
}

3:
float truncate_number(float number){
    return number-int(number);
}

4:
bool will_it_fly(vector<int> q,int w){
    int sum=0;
    int n