
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    return 'db' + binary + 'db'

print(decimal_to_binary(15))
print(decimal_to_binary(32))

# returns "db1111db" and "db100000db"
<jupyter_output>
db1111db
db100000db
<jupyter_text>
Question 2:
<jupyter_code>
