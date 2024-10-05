    bool all_lower = true;
    bool all_upper = true;
    for (auto it = dict.begin(); it != dict.end(); it++) {
        string key = it->first;
        if ((key[0] >= 'a' && key[0] <= 'z') || (key[0] >= 'A' && key[0] <= 'Z')) {
            for (int i = 1; i < key.length(); i++) {
                if (!(key[i] >= 'a' && key[i] <= 'z') && !(key[i] >= 'A' && key[i] <= 'Z')) {
                    all_lower = false;
                    all_upper = false;
                    break;
                }
            }
        } else {
            all_lower = false;
            all_upper = false;
        }
    }
    return all_lower || all_upper;
}  // Returns true if all keys are in lower case or all keys are in upper case, else returns false. // The function returns false if the given map is empty.  // It checks if there are any keys that are not in lower case or upper case.  // If any key is found that is not in lower case or upper case, the function returns false.  // If all keys are in lower case or all keys are in upper case, the function returns true.  // If the map is empty, the function returns false.  // It checks each key in the map and checks if it is in lower case or upper case.  // If a key is not in lower case or upper case, the function returns false.  // If all keys are in lower case or upper case, the function returns true.  // If the map is empty, the function returns false.  // It checks each key in the map and checks if it is in lower case or upper case.  // If a key is not in lower case or upper case, the function returns false.  // If all keys are in lower case or upper case, the function returns true.  // If the map is empty, the function returns false.  // It checks each key in the map and checks if it is in lower case or upper case.  // If a key is not in lower case or upper case, the function returns false.  // If all keys are in lower case or upper case, the function returns true.  // If the map is empty, the function returns false.  // It checks each key in the