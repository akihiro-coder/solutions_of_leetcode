def outer(a):

    def inner(b):
        print(b * 5)
        return

    return inner(a)

print(outer(5))
