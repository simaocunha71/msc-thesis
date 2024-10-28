    vector<string> result;
    string new_s="";
    for(int i=0;i<s.length();i++){
        bool found=false;
        for(int j=0;j<c.length();j++){
            if(s[i]==c[j]){
                found=true;
                break;
            }
        }
        if(!found){
            new_s+=s[i];
        }
    }
    if(new_s==string(new_s.rbegin(),new_s.rend())){
        result.push_back(new_s);
        result.push_back("True");
    }else{
        result.push_back(new_s);
        result.push_back("False");
    }
    return result;
}  // Time Complexity is O(n*m) where n is the length of s and m is the length of c.  // Space Complexity is O(n) for the new_s string.