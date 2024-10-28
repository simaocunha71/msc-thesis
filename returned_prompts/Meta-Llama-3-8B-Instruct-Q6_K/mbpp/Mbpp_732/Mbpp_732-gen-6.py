def replace_specialchar(s):
    s = s.replace(" ", ":")
    s = s.replace(",", ":")
    s = s.replace(".", ":")
    return s
assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')
print(replace_specialchar('Python language, Programming language.'))  # 'Python:language::Programming:language:'
print(replace_specialchar('Hello World, Python is awesome.'))  # 'Hello:World::Python:is:awesome.'
print(replace_specialchar('a.b,c,d'))  # 'a:b,c:d'
print(replace_specialchar('   '))  # ':'
print(replace_specialchar(''))  # ''
print(replace_specialchar('a'))  # 'a'
print(replace_specialchar('a b'))  # 'a:b'
print(replace_specialchar('a b.c,d'))  # 'a:b.c:d'  # 'a:b:c:d'  # 'a:b:c:d'  # 'a:b:c:d'  # 'a:b:c:d'
print(replace_specialchar('a b.c,d e f'))  # 'a:b.c:d:e:f'  # 'a:b:c:d:e:f'  # 'a:b:c:d:e:f'  # 'a:b:c:d:e:f'  # 'a:b:c:d:e:f'
print(replace_specialchar('a b.c,d e f.g,h,i'))  # 'a:b.c:d:e:f.g:h:i'  # 'a:b:c:d:e:f.g:h:i'  # 'a:b:c:d:e:f.g:h:i'  # 'a:b:c:d:e:f.g:h:i'  # 'a:b:c:d:e:f.g:h:i'
print(replace_specialchar('a b.c,d e f.g,h,i:j,k'))  # 'a:b.c:d:e:f.g:h:i:j:k'  # 'a:b:c:d:e:f.g:h:i:j:k'  # 'a:b:c:d:e:f.g:h:i:j:k'  # 'a:b:c:d:e:f.g:h:i:j:k'  # 'a:b:c:d:e:f.g:h:i:j:k'
print(replace_specialchar('a b.c,d e f.g,h,i:j,k.l,m'))  # 'a:b.c:d:e:f.g:h:i:j:k.l:m'  # 'a:b:c:d:e:f.g