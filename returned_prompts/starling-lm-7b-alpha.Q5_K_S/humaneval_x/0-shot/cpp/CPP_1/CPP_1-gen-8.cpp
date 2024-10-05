    int i=0;
    int j=paren_string.length()-1;
    vector<string> result;
    while(i<j){
        int start=i;
        int end=j;
        while(paren_string[start]==' ')start++;
        while(paren_string[end]==' '||paren_string[end]==')')end--;
        if(paren_string[start]!=')'&&paren_string[end]!='('){
            int left=start;
            int right=end;
            string temp;
            while(left<right){
                temp+=paren_string[left];
                left++;
                while(paren_string[left]==' ')left++;
            }
            result.push_back(temp);
            i=start+1;
            j=end-1;
        }else{
            i++;
            j--;
        }
    }
    return result;
}


/*
This function takes in a string of multiple groups of nested parentheses and returns a vector of strings,
representing the balanced groups of parentheses in the input string.

Nested parentheses are not separated.
Spaces in the input string are ignored.

Explanation:
The function iteratively goes through the string and whenever it finds a '(' or a ')' it checks if the current
group of parentheses is balanced. If it is, it adds it to the result vector. Otherwise it continues to the next
group of parentheses.

The function uses two pointers, one starting from the left and one starting from the right. The pointers keep
going forward until they find a ')' or a '(' respectively. If the character at the pointer's position is not ')'
or '(' respectively, the pointer is incremented. Once the pointers find the correct character, they start
going forward again until they find a '(' or a ')' respectively. The characters between the start and end
pointers are stored in a temporary string and added to the result vector. The left and right pointers are
updated to search for the next balanced group of parentheses. The function continues this process until the
left and right pointers cross each other.
*/
