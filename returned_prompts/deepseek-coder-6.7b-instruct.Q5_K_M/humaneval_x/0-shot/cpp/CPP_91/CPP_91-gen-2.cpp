    int count = 0;
    string word;
    stringstream ss(S);
    while(ss >> word){
        if(word[0] == 'I'){
            count++;
        }
    }
    return count;
}

int main(){
    string S = "The sky is blue. The sun is shining. I love this weather";
    printf("%d\n", is_bored(S));
    return 0;
}

*/

#include <iostream>
#include <string>
#include <sstream>

int is_bored(std::string S){
    int count = 0;
    std::string word;
    std::istringstream ss(S);
    while(std::getline(ss, word, '.')){
        if(word[0] == 'I'){
            count++;
        }
    }
    return count;
}

int main(){
    std::string S = "The sky is blue. The sun is shining. I love this weather";
    std::cout << is_bored(S) << std::endl;
    return 0;
}

/*
