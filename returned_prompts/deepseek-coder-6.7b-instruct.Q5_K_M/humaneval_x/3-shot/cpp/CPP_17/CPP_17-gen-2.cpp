    vector<int> beats;
    string temp;
    for(char c : music_string){
        if(c == ' '){
            if(temp == "o") beats.push_back(4);
            else if(temp == "o|") beats.push_back(2);
            else if(temp == ".|") beats.push_back(1);
            temp = "";
        }
        else{
            temp += c;
        }
    }
    if(temp == "o") beats.push_back(4);
    else if(temp == "o|") beats.push_back(2);
    else if(temp == ".|") beats.push_back(1);
    return beats;
}


