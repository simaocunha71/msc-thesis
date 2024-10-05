    int i;
    int cube = (int)pow(i,3);
    while (cube <= a) {
        if (cube == a) return true;
        i++;
        cube = (int)pow(i,3);
    }
    return false;
} // This function is not efficient as it needs to calculate cube of all numbers up to 'a'. We can do better.


