    int count=0, i=0;
    while(str[i]){
        if(str.substr(i,substring.size())==substring){
            count++;
            i+=substring.size();
        }
        else{
            i++;
        }
    }
    return count;
}
int main()
{
    printf("%d\n",how_many_times("","a"));
    printf("%d\n",how_many_times("aaa","a"));
    printf("%d\n",how_many_times("aaaa","aa"));
    return 0;
}
```

#### Python Solution

```python
def how_many_times(str, substring):
    count = start = 0
    while True:
        start = str.find(substring, start) + 1
        if start > 0:
            count+=1
        else:
            return count

print(how_many_times("", "a"))
print(how_many_times("aaa", "a"))
print(how_many_times("aaaa", "aa"))
```

#### JavaScript Solution

```javascript
function how_many_times(str, substring){
    var count = 0, i = 0;
    while(i < str.length){
        if(str.substring(i,i+substring.length) == substring){
            count++;
            i+=substring.length;
        }
        else{
            i++;
        }
    }
    return count;
}
console.log(how_many_times("","a"));
console.log(how_many_times("aaa","a"));
console.log(how_many_times("aaaa","aa"));
```

#### Ruby Solution

```ruby
def how_many_times(str, substring)
    count = start = 0
    while true
        start = str.index(substring, start) + 1
        if start > 0
            count+=1
        else
            return count
        end
    end
end
puts how_many_times("","a")
puts how_