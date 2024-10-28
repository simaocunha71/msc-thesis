    int count = 0;
    size_t found = str.find(substring);
    while (found != std::string::npos)
    {
        count++;
        found = str.find(substring, found+1);
    }
    return count;
}

int main() {
    printf("%d\n", how_many_times("","a"));
    printf("%d\n", how_many_times("aaa","a"));
    printf("%d\n", how_many_times("aaaa","aa"));
    return 0;
}
```

## C++
```C++
#include<iostream>
#include<string>

int how_many_times(std::string str, std::string substring) {
    int count = 0;
    size_t found = str.find(substring);
    while (found != std::string::npos)
    {
        count++;
        found = str.find(substring, found+1);
    }
    return count;
}

int main() {
    std::cout << how_many_times("","a") << "\n";
    std::cout << how_many_times("aaa","a") << "\n";
    std::cout << how_many_times("aaaa","aa") << "\n";
    return 0;
}
```

## JavaScript
```JavaScript
function how_many_times(str, substring) {
    var count = 0, pos = 0;
    while (true) {
        pos = str.indexOf(substring, pos);
        if (pos !== -1) {
            count++;
            pos++;
        } else {
            break;
        }
    }
    return count;
}

console.log(how_many_times("","a"));
console.log(how_many_times("aaa","a"));
console.log(how_many_times("aaaa","aa"));
```

## Python
```Python
def how_many_times(str, substring):
    count = start = 0
    while True:
        start = str.find(