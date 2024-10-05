    vector<int> beats;
    string current_note;
    for(char chr : music_string){
        if(chr != ' '){
            current_note += chr;
        }
        else{
            if(current_note == "o"){
                beats.push_back(4);
            }
            else if(current_note == "o|"){
                beats.push_back(2);
            }
            else if(current_note == ".|"){
                beats.push_back(1);
            }
            current_note = "";
        }
    }
    if(current_note == "o"){
        beats.push_back(4);
    }
    else if(current_note == "o|"){
        beats.push_back(2);
    }
    else if(current_note == ".|"){
        beats.push_back(1);
    }
    return beats;
}


