    int i,c=0,j;
    string hex="2357BDF";
    for(i=0;i<num.size();i++){
        for(j=0;j<hex.size();j++){
            if(num[i]==hex[j])
                c++;
        }
    }
    return c;
}
int main(){
    string num;
    printf("Enter the hexadecimal number: ");
    scanf("%s",&num);
    int res=hex_key(num);
    printf("Number of primes in hexadecimal: %d",res);
    return 0;
}
*/

*/

//C++/hexToBin.cpp
#include<iostream>
#include<string>
using namespace std;

string hexToBin(string hex){
    int i = 0;
    string bin = "";
    while(hex[i]){
        switch(toupper(hex[i])){
            case '0': bin += "0000"; break;
            case '1': bin += "0001"; break;
            case '2': bin += "0010"; break;
            case '3': bin += "0011"; break;
            case '4': bin += "0100"; break;
            case '5': bin += "0101"; break;
            case '6': bin += "0110"; break;
            case '7': bin += "0111"; break;
            case '8': bin += "1000"; break;
            case '9': bin += "1001"; break;
            case 'A': bin += "1010"; break;
            case 'B': bin += "1011"; break;
            case 'C': bin += "1100"; break;
            case 'D': bin += "1101"; break;
            case 'E': bin += "1110"; break;
            case 'F': bin += "1111"; break;
            default : bin = "Invalid Hexadecimal Number";