import sys
from os import walk, system

tuple_ = [sys.argv[1], sys.argv[2], 0]

try:
    tuple_[2] = int(sys.argv[3])
except:
    pass

for item in walk(tuple_[0]):
    full = item[0].split('/')[len(tuple_[0].split('/')):]
    size = len(full)
    for i in range(size - tuple_[2] + (1 if tuple_[2] != 0 else 0), size):
        p = ""
        for j in full[i:]:
            p += j + "/"
        p = p[:len(p) - 1]
        system(
            'mkdir -p ' + tuple_[1] + "/" + p
        )
    ans = ""
    for j in full[size - tuple_[2] + (1 if tuple_[2] != 0 else 0):]:
        ans += j + "/"
    ans = ans[:len(ans) - 1]
    for j in item[2]:
        system(
                f"cp " + item[0] + "/" + j + " " + tuple_[1] + "/" + ans
        )
