def replace_spaces(s):
    return s.replace(' ', '_').replace('_', ' ')

assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
print(replace_spaces('Jumanji The Jungle'))  # Output: Jumanji_The_Jungle
print(replace_spaces('_Jumanji_The_Jungle_'))  # Output: Jumanji The Jungle
print(replace_spaces('JumanjiTheJungle'))  # Output: Jumanji_The_Jungle
print(replace_spaces('_Jumanji_The_Jungle'))  # Output: Jumanji The Jungle
print(replace_spaces('Jumanji   The   Jungle'))  # Output: Jumanji_The_Jungle
print(replace_spaces('Jumanji_The_Jungle_'))  # Output: Jumanji The Jungle
print(replace_spaces('Jumanji_The_Jungle   '))  # Output: Jumanji_The_Jungle
print(replace_spaces('   Jumanji_The_Jungle'))  # Output: Jumanji_The_Jungle
print(replace_spaces('   Jumanji   The   Jungle   '))  # Output: Jumanji_The_Jungle
print(replace_spaces('   Jumanji   The   Jungle   '))  # Output: Jumanji_The_Jungle
print(replace_spaces('   Jumanji   The   Jungle   '))  # Output: Jumanji_The_Jungle
print(replace_spaces('   Jumanji   The   Jungle   '))  # Output: Jumanji_The_Jungle
print(replace_spaces('   Jumanji   The   Jungle   '))  # Output: Jumanji_The_Jungle
print(replace_spaces('   Jumanji   The   Jungle   '))  # Output: Jumanji_The_Jungle
print(replace_spaces('   Jumanji   The   Jungle   '))  # Output: Jumanji_The_Jungle
print(replace_spaces('   Jumanji   The   Jungle   '))  # Output: Jumanji_The_Jungle
print(replace_spaces('   Jumanji   The   Jungle   '))  # Output: Jumanji_The_Jungle
print(replace_spaces('   Jumanji   The   Jungle   '))  # Output: Jumanji_The_Jungle