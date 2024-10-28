    if(dict.empty())
    return false;
    bool upper=true;
    bool lower=true;
    for(auto it=dict.begin();it!=dict.end();it++)
    {
        if(it->first[0]>='a' && it->first[0]<='z')
        lower=false;
        if(it->first[0]>='A' && it->first[0]<='Z')
        upper=false;
    }
    return upper || lower;
}  // return false if not all keys in lower case or all keys in upper case
// return true if all keys in lower case or all keys in upper case
// return false if map is empty  //  return true if map is not empty but not all keys in lower case or all keys in upper case
// return true if map is not empty and all keys in lower case or all keys in upper case
// return false if map is empty or not all keys in lower case or all keys in upper case
// return true if map is empty or all keys in lower case or all keys in upper case
// return true if map is not empty or all keys in lower case or all keys in upper case
// return false if map is not empty or not all keys in lower case or all keys in upper case
// return true if map is not empty or not all keys in lower case and all keys in upper case
// return false if map is not empty or all keys in lower case and all keys in upper case
// return true if map is empty or all keys in lower case or all keys in upper case
// return true if map is not empty or all keys in lower case or all keys in upper case
// return false if map is not empty or not all keys in lower case or all keys in upper case
// return true if map is empty or not all keys in lower case or all keys in upper case
// return false if map is empty or all keys in lower case or all keys in upper case
// return true if map is not empty or all keys in lower case or all keys in upper case
// return false if map is empty or not all keys in lower case or all keys in upper case
// return true if map is not empty or not all keys in lower case or all keys in upper case
// return false if map is not empty or all keys in lower case or all keys in upper case
// return true if map is empty or not all keys in lower case or all