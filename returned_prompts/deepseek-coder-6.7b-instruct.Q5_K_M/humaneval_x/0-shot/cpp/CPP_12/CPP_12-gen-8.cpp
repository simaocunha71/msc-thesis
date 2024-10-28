    if(strings.empty())
        return None
B:
    longest = strings[0]
    for string in strings:
        if len(string) > len(longest):
            longest = string
C:
    return longest
*/

