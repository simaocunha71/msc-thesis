
In your has_close_elements function, you don't need to check if the difference is less than the threshold, just if it is zero. This is because the threshold is the maximum allowed difference between numbers, and if the difference is zero, it's obviously not less than the threshold. So the function can be simplified to:
bool has_close_elements(vector<float> numbers, float threshold){
    for (int i=0;i<numbers.size();i++)
        for (int j=i+1;j<numbers.size();j++)
            if (numbers[i]==numbers[j])
                return true;
    return false;
}

In your separate_paren_groups function, you don't need to check if the level is zero before adding the current_paren to the vector of parentheses. This is because you are adding the current_paren to the vector after you have finished processing the entire string, so it will always be the last group of parentheses. So the function can be simplified to:
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    for (int i=0;i<paren_string.length();i++){
        chr=paren_string[i];
        if (chr=='('){
            level+=1;
            current_paren+=chr;
        }
        if (chr==')'){
            level-=1;
            current_paren+=chr;
        }
        if (level==0){
            all_parens.push_back(current_paren);
            current_paren="";
        }
    }
    return all_parens;
}

In your truncate_number function, you don't need to use the abs function, because the difference between a number and its integer part is always positive. So the function can be simplified to:
float truncate_number(float number){
    return number-int(number);
}

In your strange_sort_list function, you don't need to