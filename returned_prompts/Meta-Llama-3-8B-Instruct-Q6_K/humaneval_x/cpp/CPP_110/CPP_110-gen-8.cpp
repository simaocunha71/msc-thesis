    int count=0;
    for(int i=0;i<lst1.size();i++){
        for(int j=0;j<lst2.size();j++){
            if(lst1[i]%2!=0 && lst2[j]%2==0){
                lst1[i]=lst2[j];
                lst2[j]=-1;
                count++;
            }
        }
    }
    for(int i=0;i<lst1.size();i++){
        if(lst1[i]%2!=0){
            return "NO";
        }
    }
    return "YES";
}

int main(){
    vector<int> lst1 = {1, 2, 3, 4};
    vector<int> lst2 = {1, 2, 3, 4};
    string result = exchange(lst1, lst2);
    cout<<result<<endl;
    return 0;
}
B:
    int main() {
        vector<int> lst1 = {1, 2, 3, 4};
        vector<int> lst2 = {1, 2, 3, 5};
        string result = exchange(lst1, lst2);
        cout << result << endl;
        return 0;
    }
C:
    int main() {
        vector<int> lst1 = {1, 2, 3, 4};
        vector<int> lst2 = {1, 2, 3, 4};
        string result = exchange(lst1, lst2);
        cout << result << endl;
        return 0;
    }
D:
    int main() {
        vector<int> lst1 = {1, 2, 3, 4};
        vector<int> lst2 = {1, 5, 3, 4};
        string result = exchange(lst1, lst2);
        cout << result << endl;
        return 0;
    }

Answer: C:
/*
In this problem, you will implement a function that takes two vectors of numbers,
and determines whether it is possible to perform an exchange of elements
between them to make lst1 a vector of only even numbers.
There is no limit on the number of exchanged elements between lst1 and lst2.
If it is possible to exchange elements between the lst1 and lst2 to make
all the elements of lst1 to be even, return "YES".
Otherwise, return "NO".
For example:
exchange({1, 2, 3, 4}, {1, 