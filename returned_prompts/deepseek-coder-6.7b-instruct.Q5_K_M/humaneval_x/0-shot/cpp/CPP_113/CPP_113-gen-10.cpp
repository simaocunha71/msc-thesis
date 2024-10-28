    vector<string> output;
    map<int,int> count;
    for(int i=0; i<lst.size(); i++){
        for(int j=0; j<lst[i].size(); j++){
            if((lst[i][j]-'0')%2 != 0)
                count[i]++;
        }
        string s = "the number of odd elements in the string " + to_string(count[i]) + " of the input.";
        output.push_back(s);
    }
    return output;
}





int main(){

    vector<string> input = {"3","11111111"};
    vector<string> output = odd_count(input);
    for(int i=0; i<output.size(); i++){
        printf("%s\n", output[i].c_str());
    }
    return 0;
}




/*
