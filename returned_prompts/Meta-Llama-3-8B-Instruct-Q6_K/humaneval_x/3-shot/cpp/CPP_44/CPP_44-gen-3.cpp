    string result = "";
    while(x > 0)
    {
        int rem = x % base;
        if(rem > 9)
            result = (char)(rem + 55) + result;
        else
            result = to_string(rem) + result;
        x /= base;
    }
    return result;
}
// This solution uses the concept of remainder to convert the number from decimal to other base.
// It uses string to store the result. The remainder is appended at the beginning of the string.
// If the remainder is more than 9 (for bases greater than 10), it is converted to a character.
// The division is done until the number becomes 0. The result is the string representation of the number in the desired base.