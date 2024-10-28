    int start,end;
    if (interval1[0]>interval2[0]){
        start=interval2[0];
        end=interval1[1];
    }
    else if (interval1[1]<interval2[0]){
        return "NO";
    }
    else{
        start=interval1[0];
        end=interval2[1];
    }
    if (end-start==0){
        return "NO";
    }
    else{
        if (truncate_number(start)==truncate_number(end-1)){
            return "YES";
        }
        else{
            return "NO";
        }
    }
}


