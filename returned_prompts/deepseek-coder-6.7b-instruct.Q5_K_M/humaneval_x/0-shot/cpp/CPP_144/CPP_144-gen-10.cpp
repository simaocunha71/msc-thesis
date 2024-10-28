    int a, b, c, d;
    a = stoi(x.substr(0, x.find('/')));
    b = stoi(x.substr(x.find('/') + 1));
    c = stoi(n.substr(0, n.find('/')));
    d = stoi(n.substr(n.find('/') + 1));
    if (a * d == b * c)
        return true;
    else
        return false;
}

int main(){
    string x, n;
    cin>>x>>n;
    if(simplify(x,n))
        cout<<"true";
    else
        cout<<"false";
    return 0;
}
*/

#include <iostream>
#include <string>
using namespace std;

bool simplify(string x, string n) {
    int numerator1 = stoi(x.substr(0, x.find('/')));
    int denominator1 = stoi(x.substr(x.find('/') + 1));
    int numerator2 = stoi(n.substr(0, n.find('/')));
    int denominator2 = stoi(n.substr(n.find('/') + 1));

    return (numerator1 * denominator2) == (numerator2 * denominator1);
}

int main() {
    string x, n;
    cin >> x >> n;
    cout << (simplify(x, n) ? "true" : "false");
    return 0;
}

//src/main/java/com/solution/Main.java
package com.solution;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String x = scanner.next();
        String n = scanner.next();
        System.out.println(simplify(x, n) ? "true" : "false");
    }

    public static boolean simplify(String x, String n) {
        int numerator1 = Integer