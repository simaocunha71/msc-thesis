    transform(str.begin(), str.end(), str.begin(), ::tolower); //to convert string to lower case
    vector<char> v(str.begin(), str.end()); //convert string to vector
    sort(v.begin(), v.end()); //sort the vector
    v.erase(unique(v.begin(), v.end()), v.end()); //remove duplicate characters
    return v.size(); //return the size of vector
}
int main(){
    printf("%d\n", count_distinct_characters("xyzXYZ"));
    printf("%d\n", count_distinct_characters("Jerry"));
    return 0;
}

*/

*/
#include <stdio.h>

int count_distinct_characters(char *str){
    int freq[256] = {0}, i; //create an array to store frequency of characters
    for(i = 0; str[i]; i++){
        freq[str[i]]++; //increment frequency of each character
    }
    int count = 0;
    for(i = 0; i < 256; i++){
        if(freq[i] > 0){ //if frequency is more than 0, then character is distinct
            count++; //increment count
        }
    }
    return count; //return count of distinct characters
}

int main(){
    printf("%d\n", count_distinct_characters("xyzXYZ"));
    printf("%d\n", count_distinct_characters("Jerry"));
    return 0;
}






































































































































