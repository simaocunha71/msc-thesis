
    vector<int> depths;
    int depth = 0;
    stringstream ss(paren_string);
    string paren_group;

    while(getline(ss, paren_group, ' ')){
        depth = 0;
        int max_depth = 0;

        for(char &c : paren_group){
            if(c == '('){
                depth++;
                if(depth > max_depth){
                    max_depth = depth;
                }
            }
            else if(c == ')'){
                depth--;
            }
        }

        depths.push_back(max_depth);
    }

    return depths;


}


