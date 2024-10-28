    if(dict.empty())
        return false;

    string first_key = *(dict.begin())->first;

    for(auto it = dict.begin(); it != dict.end(); ++it)
    {
        if(tolower(it->first) != tolower(first_key) && toupper(it->first) != toupper(first_key))
            return false;
    }
    return true;
} 
//The function check_dict_case checks if all keys in the map are in the same case 
//(either all are in lower case or all are in upper case). If the map is empty, it returns false. 

//This function first checks if the map is empty. If it is, it returns false. 

//Then it takes the first key in the map and converts it to lower case and upper case. 

//Then it iterates over the rest of the keys in the map. If any key is not in the same case 
//(either lower case or upper case) as the first key, it returns false. 

//If it has checked all keys and hasn't returned false, it means all keys are in the same case, 
//so it returns true. 

//The function uses the tolower and toupper functions from the string library to convert the keys to lower and upper case. 

//It uses the auto keyword to declare the iterator variable. This is a feature of C++11. 

//The function returns false if the map is empty and true if all keys are in the same case. 
//It uses the *(dict.begin())->first expression to get the first key in the map. This is because dict.begin() returns an iterator to the first element in the map, and *(dict.begin())->first returns the key of this element. 
//It uses the tolower and toupper functions to convert the key to lower and upper case. 
//It uses the == operator to compare the case of the key with the case of the first key. 
//It returns false if any key is not in the same case as the first key, and true if all keys are in the same case. 
//It uses the for loop to iterate over the rest of the keys in the map. 
//It uses the auto keyword to declare the iterator variable. 
//It uses the ++ operator to increment the iterator. 
//It returns false if any key is not in the same case as the first key, and true if all keys are in the same case. 
//It uses the return statement to return the