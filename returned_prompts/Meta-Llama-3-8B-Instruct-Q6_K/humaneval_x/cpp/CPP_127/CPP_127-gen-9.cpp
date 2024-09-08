    int start1 = interval1[0];
    int end1 = interval1[1];
    int start2 = interval2[0];
    int end2 = interval2[1];
    int intersection_start = max(start1, start2);
    int intersection_end = min(end1, end2);

    if(intersection_start > intersection_end)
        return "NO";
    int intersection_length = intersection_end - intersection_start + 1;
    int flag = 0;
    for(int i = 2; i <= intersection_length; i++){
        int count = 0;
        for(int j = 1; j * j <= i; j++){
            if(i % j == 0){
                count++;
            }
        }
        if(count == 1){
            flag = 1;
            break;
        }
    }
    if(flag == 1)
        return "YES";
    else
        return "NO";

B:
    int start1 = interval1[0];
    int end1 = interval1[1];
    int start2 = interval2[0];
    int end2 = interval2[1];

    int intersection_start = max(start1, start2);
    int intersection_end = min(end1, end2);

    if(intersection_start > intersection_end)
        return "NO";
    int intersection_length = intersection_end - intersection_start + 1;

    if(isPrime(intersection_length))
        return "YES";
    else
        return "NO";

C:
    int start1 = interval1[0];
    int end1 = interval1[1];
    int start2 = interval2[0];
    int end2 = interval2[1];

    int intersection_start = max(start1, start2);
    int intersection_end = min(end1, end2);

    if(intersection_start > intersection_end)
        return "NO";
    int intersection_length = intersection_end - intersection_start + 1;

    if(primeCheck(intersection_length))
        return "YES";
    else
        return "NO";

D:
    int start1 = interval1[0];
    int end1 = interval1[1];
    int start2 = interval2[0];
    int end2 = interval2[1];

    int intersection_start = max(start1, start2);
    int intersection_end = min(end1, end2);

    if(intersection_start > intersection_end)
        return "NO";
    int intersection_length = intersection_end -