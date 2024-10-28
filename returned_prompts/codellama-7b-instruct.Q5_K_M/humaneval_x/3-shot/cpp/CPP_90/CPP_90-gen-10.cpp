    if (lst.size()>1){
        vector<int>::iterator it;
        it=min_element(lst.begin(),lst.end());
        int min=*it;
        lst.erase(it);
        it=min_element(lst.begin(),lst.end());
        int min2=*it;
        if (min2==min)
            return None;
        else
            return min2;
    }
    else
        return None;
}



