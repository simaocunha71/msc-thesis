    int count = 0;
    string temp = "";
    for (int i = 0; i < S.length(); i++){
        if (S[i] == '.' || S[i] == '?' || S[i] == 's' || S[i] == 'S'){
            if (temp[0] == 'I') {
                count++;
            }
            temp = "";
        }
        else{
            temp += S[i];
        }
    }
    if (temp[0] == 'I') {
        count++;
    }
    return count;
}

int main(){
    printf("%d\n",is_bored("Hello world"));
    printf("%d\n",is_bored("The sky is blue. The sun is shining. I love this weather"));
    return 0;
}

// Output:
// 0
// 1


Explanation:
In the second example, there are 2 sentences. The first one starts with 'I' so it is a boredom. The second one starts with 'I' so it is also a boredom. So, the total number of boredoms is 2.
*/










































































































































































































































