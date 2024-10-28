    vector<int> filtered;

B:
    for(auto it = values.begin(); it != values.end(); ++it){

C:
        try{
            int value = boost::any_cast<int>(*it);
            filtered.push_back(value);
        }
        catch(boost::bad_any_cast& e){
            continue;
        }
    }

D:
    return filtered;
}

int main(){
    list_any values = {1, 2, 3, "abc", list_any(), list_any()};
    vector<int> filtered = filter_integers(values);
    for(auto it = filtered.begin(); it != filtered.end(); ++it){
        printf("%d\n", *it);
    }
    return 0;
}

