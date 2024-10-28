    for(int i = 0; i < message.size(); i++){
        char c = message[i];
        if(isalpha(c)){
            if(islower(c)){
                message[i] = toupper(c);
            }
            else{
                message[i] = tolower(c);
            }
        }
        if(strchr("aeiouAEIOU", c)){
            if(islower(c)){
                message[i] = char(c - 32 + 2);
            }
            else{
                message[i] = char(c + 2);
            }
        }
    }
    return message;
}

int main()
{
    cout<<encode("test")<<endl;
    cout<<encode("This is a message")<<endl;
    return 0;
}

*/

int main() {
    std::cout << encode("test") << std::endl;
    std::cout << encode("This is a message") << std::endl;
    return 0;
}

*/

int main() {
    std::cout << encode("test") << std::endl;
    std::cout << encode("This is a message") << std::endl;
    return 0;
}

*/

int main() {
    std::cout << encode("test") << std::endl;
    std::cout << encode("This is a message") << std::endl;
    return 0;
}

*/

int main() {
    std::cout << encode("test") << std::endl;
    std::cout << encode("This is a message") << std::endl;
    return 0;
}

*/

int main() {
    std::cout << encode("test") << std::endl;
    std::cout << encode("This is a message") << std::endl;
    return 0;
}

*/

int main() {
    std::cout << encode("test") << std::endl;
    std::cout << encode("This is a message