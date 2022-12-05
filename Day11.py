a = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

b = a.splitlines()
count = 0
for i in range(len(b)): 
    for j in range(len(b[i])):
        if b[i][j] == "L":  # Haupt
            if j + 1 < len(b[i]):  # überprüfung rechts
                if b[i][j + 1] == "L" or b[i][j + 1] == ".":
                    print("1")
                    count += 1
            else:
                count += 1
            if j - 1 < 0:  # überprüfung links
                if b[i][j - 1] == "L" or b[i][j - 1] == ".":
                    print("2")
                    count += 1
            else:
                count += 1
            if i - 1 < 0:  # überprüfung oben
                if b[i - 1][j] == "L" or b[i - 1][j] == ".":
                    print("3")
                    count += 1
                    if j + 1 < len(b[i]):  # überprüfung rechts
                        if b[i - 1][j + 1] == "L" or b[i - 1][j + 1] == ".":
                            print("4")
                            count += 1
                    if j - 1 < 0:  # überprüfung links
                        if b[i - 1][j - 1] == "L" or b[i - 1][j - 1] == ".":
                            print("5")
                            count += 1
            else:
                print("hllo")
                count += 1
            if i + 1 < len(b):  # überprüfung unten
                if b[i + 1][j] == "L" or b[i + 1][j] == ".":
                    print("6")
                    count += 1
                    if j + 1 < len(b[i]):  # überprüfung rechts
                        if b[i + 1][j + 1] == "L" or b[i + 1][j + 1] == "L":
                            print("7")
                            count += 1
                    if j - 1 < 0:  # überprüfung links
                        if b[i + 1][j - 1] == "L" or b[i + 1][j - 1] == "L":
                            print("8")
                            count += 1
            else:
                count += 1
            if count == 8:
                s = b[i].replace("L", "#", j)
                print(s)
