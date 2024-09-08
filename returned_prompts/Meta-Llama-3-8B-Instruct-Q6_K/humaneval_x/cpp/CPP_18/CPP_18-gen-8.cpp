    int count = 0;
    int len = str.length();
    int sub_len = substring.length();
    for(int i = 0; i <= len - sub_len; i++){
        if(str.substr(i,sub_len) == substring){
            count++;
        }
    }
    return count;
}

int main(){
    string str, sub;
    cout<<"Enter the main string: "<<endl;
    getline(cin,str);
    cout<<"Enter the substring: "<<endl;
    getline(cin,sub);
    int result = how_many_times(str,sub);
    printf("The substring '%s' appears %d times in the string.\n", sub.c_str(), result);
    return 0;
}

Output:
Enter the main string:
aaaa
Enter the substring:
aa
The substring 'aa' appears 3 times in the string.

Enter the main string:
aaaa
Enter the substring:
aaa
The substring 'aaa' appears 1 times in the string.

Enter the main string:
a
Enter the substring:
a
The substring 'a' appears 1 times in the string.