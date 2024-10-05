    return string(to_string(x).rbegin()+shift,to_string(x).rend()).append(to_string(x).begin(),to_string(x).begin()+shift);
}
