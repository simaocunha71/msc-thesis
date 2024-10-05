    int eaten = number + need;
    if(eaten > remaining + number){
        eaten = remaining + number;
    }
    int left = remaining + number - eaten;
    return {eaten, left};
}

