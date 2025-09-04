pts = []

def getsev(p):
    return p[1]

def aging():
    for i in range(len(pts)):
        n, s = pts[i]
        pts[i] = (n, s + 1)

while True:
    act = input("\nType add / serve / exit: ").lower()

    if act == "add":
        n = input("Enter patient name: ")
        s = int(input("Enter severity (1-10): "))
        pts.append((n, s))

    elif act == "serve":
        if pts:
            aging()
            p = max(pts, key=getsev)
            pts.remove(p)
            print("Serving:", p[0], "with severity", p[1])
        else:
            print("no patients right now")

    elif act == "exit":
        break

    else:
        print("invalid option, try again")
