    if (abs(a-int(a))+abs(b-int(b))+abs(c-int(c))>0.0001)
        return false;
    if (a==int(a)+int(b)+int(c))
        return true;
    if (b==int(b)+int(a)+int(c))
        return true;
    if (c==int(c)+int(a)+int(b))
        return true;
    return false;
}  // https://www.codewars.com/kata/5c1a0f65d7db9a0011a6f7f1/train/cpp


