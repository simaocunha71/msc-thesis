    int a, b, total_apples = 0, total_oranges = 0;
    sscanf(s.c_str(), "%d apples and %d oranges", &total_apples, &total_oranges);
    a = total_apples;
    b = total_oranges;
    int total_fruits = n;
    int total_mangoes = total_fruits - (total_apples + total_oranges);
    return total_mangoes;
}
int main(){
    string s1 = "5 apples and 6 oranges";
    string s2 = "0 apples and 1 oranges";
    string s3 = "2 apples and 3 oranges";
    string s4 = "100 apples and 1 oranges";
    printf("%d\n",fruit_distribution(s1,19)); //8
    printf("%d\n",fruit_distribution(s2,3)); //2
    printf("%d\n",fruit_distribution(s3,100)); //95
    printf("%d\n",fruit_distribution(s4,120)); //19
    return 0;
}
*/

int main() {
    string s1 = "5 apples and 6 oranges";
    string s2 = "0 apples and 1 oranges";
    string s3 = "2 apples and 3 oranges";
    string s4 = "100 apples and 1 oranges";
    cout << fruit_distribution(s1,19) << endl; //8
    cout << fruit_distribution(s2,3) << endl; //2
    cout << fruit_distribution(s3,100) << endl; //95
    cout << fruit_distribution(s4,120) << endl; //19
    return 0;
}

// This code is a C++ solution for the problem. It takes a string that represents the number of 
// apples and oranges and an integer that represents the total number of fruits in the basket. 
// The function fruit_distribution calculates the number of mango fruits by subtracting the total 
// number of apples