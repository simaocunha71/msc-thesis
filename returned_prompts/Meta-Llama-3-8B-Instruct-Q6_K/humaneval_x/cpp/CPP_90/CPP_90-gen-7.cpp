    if(lst.size()==0 || lst.size()==1) return NULL; // Check if the vector is empty or has only one element
    sort(lst.begin(), lst.end()); // Sort the vector
    for(int i=0; i<lst.size()-1; i++){
        if(lst[i+1] != lst[i]){ // Check if the current element is smaller than the next one
            return lst[i+1]; // Return the 2nd smallest element
        }
    }
    return NULL; // If the loop ends without finding the 2nd smallest element, return NULL
}

