    vector<float> l_even;
    vector<float> l_odd;
    vector<float> l_even_sorted;

    for(int i=0;i<l.size();i++){
        if(i%2==0){
            l_even.push_back(l[i]);
        }
        else{
            l_odd.push_back(l[i]);
        }
    }
    sort(l_even.begin(),l_even.end());

    for(int i=0;i<l_even.size();i++){
        l_even_sorted.push_back(l_even[i]);
    }
    for(int i=0;i<l_odd.size();i++){
        l_even_sorted.push_back(l_odd[i]);
    }

    return l_even_sorted;

B:
    vector<float> l_even;
    vector<float> l_odd;
    vector<float> l_even_sorted;

    for(int i=0;i<l.size();i++){
        if(i%2==0){
            l_even.push_back(l[i]);
        }
        else{
            l_odd.push_back(l[i]);
        }
    }
    sort(l_even.begin(),l_even.end());

    for(int i=0;i<l.size();i++){
        if(i%2==0){
            l_even_sorted.push_back(l_even[i/2]);
        }
        else{
            l_even_sorted.push_back(l_odd[i-1]);
        }
    }

    return l_even_sorted;

C:
    vector<float> l_even;
    vector<float> l_odd;
    vector<float> l_even_sorted;
    vector<float> l_even_sorted_reversed;

    for(int i=0;i<l.size();i++){
        if(i%2==0){
            l_even.push_back(l[i]);
        }
        else{
            l_odd.push_back(l[i]);
        }
    }
    sort(l_even.begin(),l_even.end());

    for(int i=0;i<l_even.size();i++){
        l_even_sorted.push_back(l_even[i]);
    }
    for(int i=0;i<l_odd.size();i++){
        l_even_sorted.push_back(l_odd[i]);
    }

    for(int i=0;i<l_even_sorted.size();i++){
        l_even_sorted_reversed.push_back(l_even_sorted[l_even_sorted.size()-1-i]);
    }

    return l_even_sorted_reversed;

D:
    vector<float> l_even;
    vector<float> l_odd;
    vector<float> l_even_sorted;

    for(int i=0;i<l.size();i++){
        if(i%2==0){
            l_even.push_back(l[i]);
        }
        else{
            l