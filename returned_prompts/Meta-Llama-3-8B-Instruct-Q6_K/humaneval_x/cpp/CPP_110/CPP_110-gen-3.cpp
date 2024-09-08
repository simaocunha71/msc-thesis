    // Create a copy of lst1
    vector<int> copy_lst1 = lst1;

    // Iterate over lst2
    for(int i = 0; i < lst2.size(); i++){
        // Check if the current element in lst2 is even
        if(lst2[i] % 2 == 0){
            // Iterate over copy_lst1
            for(int j = 0; j < copy_lst1.size(); j++){
                // Check if the current element in copy_lst1 is odd
                if(copy_lst1[j] % 2 != 0){
                    // Replace the odd element with the even element
                    copy_lst1[j] = lst2[i];
                    break;
                }
            }
        }
    }

    // Check if all elements in copy_lst1 are even
    for(int k = 0; k < copy_lst1.size(); k++){
        if(copy_lst1[k] % 2 != 0){
            return "NO";
        }
    }

    return "YES";
}

int main() {
    vector<int> lst1 = {1, 2, 3, 4};
    vector<int> lst2 = {1, 2, 3, 4};
    printf("%s\n", exchange(lst1, lst2).c_str());
    return 0;
}

B:
    // Create a copy of lst1
    vector<int> copy_lst1 = lst1;

    // Iterate over lst2
    for(int i = 0; i < lst2.size(); i++){
        // Check if the current element in lst2 is even
        if(lst2[i] % 2 == 0){
            // Find the first odd element in copy_lst1
            for(int j = 0; j < copy_lst1.size(); j++){
                if(copy_lst1[j] % 2 != 0){
                    // Replace the odd element with the even element
                    swap(copy_lst1[j], lst2[i]);
                    break;
                }
            }
        }
    }

    // Check if all elements in copy_lst1 are even
    for(int k = 0; k < copy_lst1.size(); k++){
        if(copy_lst1[k] % 2 != 0){
            return "NO";
        }
    }

    return "YES";
}

C:
    // Create a copy of lst1
    vector<int> copy_lst1 = lst1;

    // Iterate over lst2