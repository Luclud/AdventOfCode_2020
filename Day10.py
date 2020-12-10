from collections import Counter

a = """30
73
84
136
132
117
65
161
49
68
139
46
21
127
109
153
163
160
18
22
131
146
62
113
172
150
171
98
93
130
170
59
1
110
2
55
37
44
148
102
40
28
35
43
56
169
33
5
141
83
15
105
142
36
116
11
45
82
10
17
159
140
12
108
29
72
121
52
91
166
88
97
118
99
124
149
16
9
143
104
57
79
123
58
96
24
162
23
92
69
147
156
25
133
34
8
85
76
103
122"""

b = list(map(int,a.splitlines()))
#b.append(0)
b.sort()
#b.append(b[-1]+3)

def task1():
    i = 1
    j = 0
    try:
        for x in range(len(b)):
            if b[x+1] - b[x] == 1:
                i += 1
            if b[x+1] - b[x] == 3:
                j += 1

    except:
        pass
    print(i * j)

l = [0]
m = []
n = []

def task2():
    s = ""
    count = 1
    print(b)
    try:
        for x in range(len(b)+1):
            if b[x+1] - b[x] == 3:
                if b[x] not in l:
                    l.append(b[x])
                if b[x+1] not in l:
                    l.append(b[x+1])

    except:
        pass
    print(l)
    try:
        for x in b:
            if x not in l:
                m.append(x)
        print(m)
    except:
        pass

    m.append(1000)
    for x in range(len(m)-1):
        if m[x+1] - m[x] < 3:
            s += " " + str(m[x])
        else:
            s += " " + str(m[x])
            s = s[1:]
            n.append(s.split(" "))
            s = ""
    count = 1
    for x in n:
        if len(x) == 3:
            count *= 7
        if len(x) == 2:
            count *= 4
        if len(x) == 1:
            count *= 2
    return count


