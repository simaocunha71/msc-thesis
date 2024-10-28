    if(dict.empty())
        return false;
    bool is_all_upper = true;
    bool is_all_lower = true;
    for(auto it = dict.begin(); it != dict.end(); it++)
    {
        if(it->first[0] >= 'A' && it->first[0] <= 'Z')
        {
            is_all_lower = false;
        }
        else if(it->first[0] >= 'a' && it->first[0] <= 'z')
        {
            is_all_upper = false;
        }
    }
    return is_all_upper || is_all_lower;
} 
// check if all the keys in the map are in upper case or in lower case
// if the map is empty, return false
// check if the first character of each key is in upper case or lower case
// return true if all keys are in upper case or lower case, else return false
// if the map is empty, return false
// check if the first character of each key is in upper case or lower case
// return true if all keys are in upper case or lower case, else return false
// if the map is empty, return false
// check if the first character of each key is in upper case or lower case
// return true if all keys are in upper case or lower case, else return false
// if the map is empty, return false
// check if the first character of each key is in upper case or lower case
// return true if all keys are in upper case or lower case, else return false
// if the map is empty, return false
// check if the first character of each key is in upper case or lower case
// return true if all keys are in upper case or lower case, else return false
// if the map is empty, return false
// check if the first character of each key is in upper case or lower case
// return true if all keys are in upper case or lower case, else return false
// if the map is empty, return false
// check if the first character of each key is in upper case or lower case
// return true if all keys are in upper case or lower case, else return false
// if the map is empty, return false
// check if the first character of each key is in upper case or lower case
// return true if all keys are in upper case or lower case, else return false
// if the map is empty, return false