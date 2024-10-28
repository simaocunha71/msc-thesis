    if(need>remaining)
    {
        number+=remaining;
        remaining=0;
    }
    else
    {
        number+=need;
        remaining-=need;
    }
    return {number, remaining};
}


