    vector<int> pile(n);
    for(int i = 0; i < n; i++){
        pile[i] = i + 1;
        if(i % 2 != 0){
            pile[i] = pile[i] + 1;
        }
    }
    return pile;
}





ANSWER:
/*
    The above recursive function is incorrect because the function is not able to return the vector correctly. The correct function is below:

vector<int> make_a_pile(int n){

    vector<int> pile;
    if(n == 0){
        return pile;
    }
    if(n % 2 == 0){
        pile.push_back(n);
        vector<int> temp = make_a_pile(n - 1);
        for(int i = 0; i < temp.size(); i++){
            pile.push_back(temp[i] + 1);
        }
    }else{
        pile.push_back(n);
        vector<int> temp = make_a_pile(n - 1);
        for(int i = 0; i < temp.size(); i++){
            pile.push_back(temp[i] + 2);
        }
    }
    return pile;
}

This function will work correctly and return the vector of stones in the pile.

However, the above function is not efficient. It has a time complexity of O(2^n) because it calls itself recursively for each level of the pile.

A better approach is to use a loop to build the pile. The function below has a time complexity of O(n):

vector<int> make_a_pile(int n){
    vector<int> pile(n);
    for(int i = 0; i < n; i++){
        pile[i] = i + 1;
        if(i % 2 != 0){
            pile[i] = pile[i] + 1;
        }
    }
    return pile;
}

This function will return the correct vector of stones in the pile, and it is more