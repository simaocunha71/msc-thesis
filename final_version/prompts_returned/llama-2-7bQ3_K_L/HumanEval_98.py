
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    upper_count = 0
    for i in range(len()):
        if s[i] == 'a' or s[i] == 'e':
            if i % 2:
                upper_count += 1
            
    return upper_count

def main():
    # Test the function. Input: "abcdef"
    print(count_upper('abcdef'))
    
if __name__ == '__main__':
    main()