    count := 0
    s = strings.ToLower(s)
    for _, v := range s {
        if v == 'a' || v == 'e' || v == 'i' || v == 'o' || v == 'u' {
            count++
        }
    }
    if s[len(s)-1] == 'y' {
        count++
    }
    return count
}

func main() {
    fmt.Println(VowelsCount("abcde"))  // Output: 2
    fmt.Println(VowelsCount("ACEDY"))  // Output: 3
}
```



## Rust

```Rust
fn vowels_count(s: &str) -> i32 {
    let vowels = ['a', 'e', 'i', 'o', 'u'];
    let mut count = 0;
    for c in s.chars() {
        if vowels.contains(&c) {
            count += 1;
        }
    }
    if s.chars().last().unwrap_or(' ') == 'y' {
        count += 1;
    }
    count
}

fn main() {
    printlnasca2d7d4-48af-b57e-7bdd6b97874c
    printlnasca2d7d4-48af-b57e-7bdd6b97874c
}
```



## Julia

```julia
function vowels_count(s::String)
    count = 0
    for c in s
        if c in ('a', 'e', 'i', 'o', 'u', 'y')
            global count += 1
        end
    end
    if s[end] == 'y'
        global count += 1
    end
    return count
end

println(vowels_count("abcde"))  # Output: 2
println(vowels_count("ACEDY"))  # Output: 3
```



## Ruby

```Ruby
def vowels_count(s)
    vow