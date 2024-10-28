    for(int i=0;i<message.length();i++){
        if(message[i]=='a')message[i]='c';
        else if(message[i]=='e')message[i]='g';
        else if(message[i]=='i')message[i]='k';
        else if(message[i]=='o')message[i]='q';
        else if(message[i]=='u')message[i]='w';
        else if(message[i]=='A')message[i]='C';
        else if(message[i]=='E')message[i]='G';
        else if(message[i]=='I')message[i]='K';
        else if(message[i]=='O')message[i]='Q';
        else if(message[i]=='U')message[i]='W';
        else if(message[i]>='a' && message[i]<='z')message[i]=message[i]+32;
        else if(message[i]>='A' && message[i]<='Z')message[i]=message[i]+32;
    }
    for(int i=0;i<message.length();i++){
        if(message[i]>='a' && message[i]<='z')message[i]=message[i]-32;
        else if(message[i]>='A' && message[i]<='Z')message[i]=message[i]-32;
    }
    return message;
}
int main(){
    string s;
    cin>>s;
    cout<<encode(s)<<endl;
}


ANSWER:
No
Explanation:
The function correctly encodes the message by swapping cases of all the letters, and replacing all vowels in the message with the letter that appears 2 places ahead of that vowel in the English alphabet.
*/















































