    string result="";
    int len_a=a.size();
    int len_b=b.size();
    int len_res=max(len_a,len_b);

B:
    for(int i=0;i<len_res;i++){
        char a_bit=(i<len_a) ? a[len_a-i-1] : '0';
        char b_bit=(i<len_b) ? b[len_b-i-1] : '0';
        char res_bit=(a_bit==b_bit) ? '0' : '1';
        result=res_bit+result;
    }

    return result;
}

int main(){
    printf("Result: %s\n", string_xor("010", "110").c_str());
    return 0;
}

*/

