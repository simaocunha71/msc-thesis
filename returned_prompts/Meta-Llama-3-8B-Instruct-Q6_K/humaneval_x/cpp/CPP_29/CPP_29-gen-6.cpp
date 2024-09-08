vector<string> filtered;
for(const string& s : strings){
    if(s.find(prefix) == 0) {
        filtered.push_back(s);
    }
}
return filtered;
}

