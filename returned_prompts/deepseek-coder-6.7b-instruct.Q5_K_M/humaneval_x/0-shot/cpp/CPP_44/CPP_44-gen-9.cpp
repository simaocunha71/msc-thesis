    string result = "";
    while (x > 0){
        result = to_string(x % base) + result;
        x /= base;
    }
    return result;
}


int main(){
    printf("%s\n", change_base(8, 3).c_str());
    printf("%s\n", change_base(8, 2).c_str());
    printf("%s\n", change_base(7, 2).c_str());
    return 0;
}




A: Here is the solution in Python:
def change_base(x, base):
    result = ""
    while x > 0:
        result = str(x % base) + result
        x //= base
    return result


print(change_base(8, 3)) # outputs: 22
print(change_base(8, 2)) # outputs: 1000
print(change_base(7, 2)) # outputs: 111

The logic is the same as in C++: the numbers are divided by base and the remainder is added to the result string. The process is repeated until the number becomes 0. The result string is returned as the final result.

A: Here is a solution in Swift:
func change_base(x: Int, base: Int) -> String {
    var x = x
    var result = ""
    while x > 0 {
        result = String(x % base) + result
        x /= base
    }
    return result
}

print(change_base(x: 8, base: 3)) // "22"
print(change_base(x: 8, base: 2)) // "1000"
print(change_base(x: 7, base: 2)) // "111"

The logic is the same as in the other solutions. The function takes two parameters, the number to convert and the base to which it should be converted, and returns a string representing the conversion.

A: Here is the solution in JavaScript:
function change_base(x, base){
    let result = "";
    while (x > 0){
        result