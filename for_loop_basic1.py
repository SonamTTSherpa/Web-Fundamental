#1
def a():
    return 5
print(a())

#2
def a():
    return 5
print(a()+a())

#3
def a():
    return 5
    return 10
print(a())

#4
def a():
    return 5
    print(10)
print(a())

#5
def a():
    print(5)
x = a()
print(x)

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
<div id="copy-toolbar-container" style="cursor: pointer; position: absolute; top: 5px; right: 5px; padding: 0px 3px; background: rgba(224, 224, 224, 0.2) none repeat scroll 0% 0%; box-shadow: rgba(0, 0, 0, 0.2) 0px 2px 0px 0px; color: rgb(187, 187, 187); border-radius: 0.5em; font-size: 0.8em;"><span id="copy-toolbar">copy</span></div>

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

x = "Hello Python"
print(x)
y = 42
print(y)