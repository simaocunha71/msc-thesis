    int start1=interval1[0];
    int end1=interval1[1];
    int start2=interval2[0];
    int end2=interval2[1];
    if (start1>end2 || start2>end1)
        return "NO";
    int intersection_start=max(start1,start2);
    int intersection_end=min(end1,end2);
    if (intersection_end<intersection_start)
        return "NO";
    int intersection_length=intersection_end-intersection_start+1;
    if (is_prime(intersection_length))
        return "YES";
    else
        return "NO";
}
bool is_prime(int num){
    if(num <= 1) return false;
    for(int i = 2; i <= sqrt(num); i++){
        if(num % i == 0) return false;
    }
    return true;
}