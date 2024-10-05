    map<char, int> hist;
    int maxCount = 0;
    map<char, int>::iterator it;
    for(char c : test){
        if(c != ' '){
            hist[c]++;
            if(hist[c] > maxCount)
                maxCount = hist[c];
        }
    }
    for(it = hist.begin(); it != hist.end(); it++){
        if((*it).second != maxCount)
            hist.erase(it);
    }
    return hist;
}


