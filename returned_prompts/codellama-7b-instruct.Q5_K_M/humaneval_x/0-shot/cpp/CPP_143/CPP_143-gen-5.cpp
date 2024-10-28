    string str = " ";
    int i = 0;
    int j = 0;
    while(sentence[i] != ' '){
        if(sentence[i] == ' '){
            i++;
            continue;
        }
        else{
            str += sentence[i];
            i++;
            while(sentence[i] != ' '){
                str += sentence[i];
                i++;
            }
            break;
        }
    }
    return str;
}
int main(int argc, char const *argv[])
{
    string sentence = "This is a test";
    printf("%s", words_in_sentence(sentence).c_str());
    return 0;
}



