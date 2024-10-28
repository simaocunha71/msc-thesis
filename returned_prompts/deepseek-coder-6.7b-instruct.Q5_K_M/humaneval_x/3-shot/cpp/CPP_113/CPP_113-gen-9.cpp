    vector<string> result;
    for(auto s : lst){
        int count = 0;
        for(auto c : s)
            if((c-'0') % 2 != 0)
                count++;
        result.push_back("the number of odd elements " + to_string(count) + "n the str" + to_string(count) + "ng " + to_string(count) + " of the " + to_string(count) + "nput.");
    }
    return result;
}


