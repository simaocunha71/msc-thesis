    int eaten=0,left=0;
    if (need>remaining){
        eaten=remaining-number;
        left=0;
    }
    else {
        eaten=need-number;
        left=remaining-eaten;
    }

    return vector<int>{number+eaten,left};
}


