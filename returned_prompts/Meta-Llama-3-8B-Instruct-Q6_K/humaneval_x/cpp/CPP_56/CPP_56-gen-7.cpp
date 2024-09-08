    int count = 0; // count the number of opening brackets
    for(int i = 0; i < brackets.size(); i++){
        if(brackets[i] == '<'){
            count++; // increment the count for every opening bracket
        }
        else if(brackets[i] == '>'){
            count--; // decrement the count for every closing bracket
            if(count < 0){ // if count becomes negative, it means there are more closing brackets than opening brackets
                return false; // return false
            }
        }
    }
    if(count == 0){ // if count is 0 at the end, it means every opening bracket has a corresponding closing bracket
        return true;
    }
    else{
        return false; // if count is not 0, it means there are more opening brackets than closing brackets
    }
}

int main() {
    string brackets = "<>";
    cout << correct_bracketing(brackets) << endl;
    return 0;
}
