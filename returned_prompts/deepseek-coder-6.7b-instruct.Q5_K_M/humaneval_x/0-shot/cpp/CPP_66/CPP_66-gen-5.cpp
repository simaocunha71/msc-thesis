    int sum = 0;
    for(int i = 0; i < s.length(); i++){
        if(isupper(s[i])){
            sum += int(s[i]);
        }
    }
    return sum;
}

int main(){
    printf("%d\n", digitSum(""));
    printf("%d\n", digitSum("abAB"));
    printf("%d\n", digitSum("abcCd"));
    printf("%d\n", digitSum("helloE"));
    printf("%d\n", digitSum("woArBld"));
    printf("%d\n", digitSum("aAaaaXa"));
    return 0;
}

*/

#include<stdio.h>
#include<string.h>
#include<ctype.h>
int digitSum(char* s){

    int sum = 0;
    for(int i = 0; i < strlen(s); i++){
        if(isupper(s[i])){
            sum += (int)s[i];
        }
    }
    return sum;
}

int main(){
    printf("%d\n", digitSum(""));
    printf("%d\n", digitSum("abAB"));
    printf("%d\n", digitSum("abcCd"));
    printf("%d\n", digitSum("helloE"));
    printf("%d\n", digitSum("woArBld"));
    printf("%d\n", digitSum("aAaaaXa"));
    return 0;
}




/*
int main(){
    printf("%d\n", digitSum("")); //0
    printf("%d\n", digitSum("abAB")); //131
    printf("%d\n", digitSum("abcCd")); //67
    printf("%d\n", digitSum("helloE")); //69
    printf("%d\n", digitSum("woArBld")); //131
    printf("%d\n", digitSum("aAaaaXa")); //153
    return 0;
}
*/



/*
int main(){
    printf("%d\n", digit