# строки

print("-----------------")
s = "Hello, World!"
s = 'Hello, World!'

print(s)

s = 'Hello, \nWorld!'

print(s)

s = ('Hello, '
     'World!')

print(s)

s = r'Hello, \nWorld!'

print(s)

print("-----------------")

email = 'username@domain.com'

print(email)

email = 'username@domain.com'

print(email[1])

email = 'username@domain.com'

print(email[-2])

email = 'username@domain.com'

print(email[0:5])

email = 'username@domain.com'

print(email[:5])

print(email[0:10:2])

print(email[::-1])

print(email[50:51])

email.split("@")

print("-----------------")

assert email.endswith('domain.com')

print("-----------------")

a = "Hello"
b = " World"

print(a + b)

a = "Hello"
b = "World"

print(a + ", " + b + "!")

print("{a}, {b}!".format(a=a, b=b))

print(f"{a}, {b.upper()}!!!")

print(f"{a=}, {b=}!!!")

print("%s, %s!" % (a, b))

print("{a}, {b}!".format(a=a, b=b))

print("-----------------")

url_template = "https://yourservice.com/v1/api{}"

users_url = url_template.format("users")
groups_url = url_template.format("groups")

s = "1234"
n = 1234

# assert s == str(n)

assert int(s) == n

assert s.isdigit()

