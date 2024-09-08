    vector<int> result;
    for(list_any::iterator it = values.begin(); it != values.end(); ++it){
        boost::any &any = *it;
        if(isa<int>(any)){
            result.push_back(boost::any_cast<int>(any));
        }
    }
    return result;
}
int main() {
    list_any values;
    values.push_back("abc");
    values.push_back(5);
    values.push_back(3.14);
    values.push_back(1);
    values.push_back(2);
    values.push_back(3);
    values.push_back({});
    values.push_back({});

    vector<int> result = filter_integers(values);
    for(int i = 0; i < result.size(); i++){
        cout << result[i] << endl;
    }
    return 0;
}
