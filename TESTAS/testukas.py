import camelcase # Šis skriptas naudoja camelcase biblioteką eilutei konvertuoti į camel case formatą.

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))
