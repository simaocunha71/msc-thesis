    float mean = 0.0;
    float sum = 0.0;
    int i;
    for (i=0;i<numbers.size();i++)
    {
        mean += numbers[i];
    }
    mean /= numbers.size();
    for (i=0;i<numbers.size();i++)
    {
        sum += abs(numbers[i]-mean);
    }
    return sum/numbers.size();
} 
}  // namespace std

int main() {
    cout << has_close_elements({1.0, 2.0, 3.0}, 0.5) << endl;
    cout << has_close_elements({1.0, 2.8, 3.0, 4.0, 5.0, 2.0}, 0.3) << endl;
    cout << separate_paren_groups("( ) (( )) (( )( ))").size() << endl;
    cout << truncate_number(3.5) << endl;
    cout << mean_absolute_deviation({1.0, 2.0, 3.0, 4.0}) << endl;
    return 0;
}
```
