    if(n <= 0){
        return "0";
    }
    else{
        return to_string(n) + " " + string_sequence(n-1);
    }
}
