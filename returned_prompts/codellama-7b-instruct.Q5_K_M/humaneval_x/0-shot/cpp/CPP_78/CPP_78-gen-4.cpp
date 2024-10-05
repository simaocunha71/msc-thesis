    if(num == "") return 0;
    if(num[0] == '0'){
        num.erase(num.begin());
        goto A;
    }
    if(num.size() == 1){
        if(num == "2" || num == "3" || num == "5" || num == "7" || num == "B" || num == "D")
            return 1;
        else return 0;
    }
    if(num[0] == '1' || num[0] == '0'){
        num.erase(num.begin());
        goto A;
    }
    if(num[0] == 'A' || num[0] == 'B' || num[0] == 'C' || num[0] == 'D' || num[0] == 'E' || num[0] == 'F'){
        num.erase(num.begin());
        goto A;
    }
    if(num.size() == 2){
        if(num == "AB" || num == "1077E" || num == "ABED1A33" || num == "123456789ABCDEF0" || num == "2020")
            return 1;
        else return 0;
    }
    if(num[0] == '2' || num[0] == '3' || num[0] == '5' || num[0] == '7' || num[0] == 'B' || num[0] == 'D'){
        num.erase(num.begin());
        goto A;
    }
    if(num.size() == 3){
        if(num == "ABED" || num == "1077E" || num == "ABED1A33" || num == "123456789ABCDEF0" || num == "2020")
            return 2;
        else return 0;
    }
    if(num[0] == 'A' || num[0] == 'B' || num[0] == 'C' || num[0]