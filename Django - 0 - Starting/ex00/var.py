def my_var():
    a = 42
    b = "42"
    c = "quarante-deux"
    d = 42.0
    e = True
    f = [5*10 - 8]
    g = {42: 42}
    h = (42,)
    i = set()

    print(f"- a: {a} est de type {type(a)}")
    print(f"- b: {b} est de type {type(b)}")
    print(f"- c: {c} est de type {type(c)}")
    print(f"- d: {d} est de type {type(d)}")
    print(f"- e: {e} est de type {type(e)}")
    print(f"- f: {f} est de type {type(f)}")
    print(f"- g: {g} est de type {type(g)}")
    print(f"- h: {h} est de type {type(h)}")
    print(f"- i: {i} est de type {type(i)}")

def main():
    my_var()

if __name__ == "__main__":
    main()