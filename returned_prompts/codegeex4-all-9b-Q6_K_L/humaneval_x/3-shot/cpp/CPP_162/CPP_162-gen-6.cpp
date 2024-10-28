
has_close_elements

The function name is not very descriptive. Maybe
bool areCloseNumbers(vector<float> numbers, float threshold)
{
    int i,j;
    
    for (i=0;i<numbers.size();i++)
        for (j=i+1;j<numbers.size();j++)
            if (abs(numbers[i]-numbers[j])<threshold)
                return true;

    return false;
}

separate_paren_groups

The function name is not very descriptive. Maybe
vector<string> getGroups(string paren_string)
{
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    int i;
    for (i=0;i<paren_string.length();i++)
    {
        chr=paren_string[i];
        if (chr=='(')
        {
            level+=1;
            current_paren+=chr;
        }
        if (chr==')')
        {
            level-=1;
            current_paren+=chr;
            if (level==0){
                all_parens.push_back(current_paren);
                current_paren="";
            }
        }
    }
    return all_parens;
}

truncate_number

The function name is not very descriptive. Maybe
float getDecimals(float number)
{
    return number - int(number);
}

string_to_md5

The function name is not very descriptive. Maybe
string getMD5(string text)
{
    if (text.length()==0){
    return NULL;
    }
    unsigned char result[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)text.c_str(), text.length(), (unsigned char*)&result);
    char buffer[2*MD5_DIGEST_LENGTH+1];
    for (int i=0;i<MD5_DIGEST_LENGTH;i++)
        sprintf(&buffer[i*2], "%02x", (unsigned int)result[i]);
    return string(buffer);
}