int max = 0;
int freq = 0;
int ans = -1;
for(int i = 0; i < lst.size(); i++)
    if(lst[i] > max)
        max = lst[i], freq = 1;
    else if(lst[i] == max)
        freq++;
if(freq >= max)
    return max;
else{
    max--;
    goto A;
}

B:
int max = 0;
int freq = 0;
int ans = -1;
for(int i = 0; i < lst.size(); i++)
    if(lst[i] > max)
        max = lst[i], freq = 1;
    else if(lst[i] == max)
        freq++;
if(freq >= max)
    return max;
else{
    max--;
    goto B;
}

C:
int max = 0;
int freq = 0;
int ans = -1;
for(int i = 0; i < lst.size(); i++)
    if(lst[i] > max)
        max = lst[i], freq = 1;
    else if(lst[i] == max)
        freq++;
if(freq >= max)
    return max;
else{
    max--