    str := strconv.FormatInt(int64(N), 2)
    sum := 0
    for _, v := range str {
        digit, _ := strconv.Atoi(string(v))
        sum += digit
    }
    return strconv.FormatInt(int64(sum), 2)
}

func main() {
    fmt.Println(Solve(1000)) // 1
    fmt.Println(Solve(150))  // 110
    fmt.Println(Solve(147))  // 1100
}

```



## Ada

```ada
with Ada.Strings; 
with Ada.Strings.Fixed; 
with Ada.Strings.Maps;
with Ada.Text_IO;

procedure Main is
    function Solve(N: Integer) return String is
        sum: Integer := 0;
        str: String := Integer'Image(N);
        digit: Integer;
    begin
        for i in str'Range loop
            if str(i) >= '0' and str(i) <= '9' then
                digit := Character'Pos(str(i)) - Character'Pos('0');
                sum := sum + digit;
            end if;
        end loop;

        return Ada.Strings.Fixed.Trim(
            Ada.Strings.Fixed.Trim(Integer'Image(sum), Ada.Strings.Left),
            Ada.Strings.Left);
    end Solve;
begin
    Ada.Text_IO.Put_Line(Solve(1000)); -- 1
    Ada.Text_IO.Put_Line(Solve(150));  -- 6
    Ada.Text_IO.Put_Line(Solve(147));  -- 12
end Main;
```



## ALGOL

```ALGOL
BEGIN
  PROCEDURE Solve = (INT N)STRING:
  BEGIN
    INT sum := 0;
    STRING str := INT2