f = open("occupations.csv", "r").readlines()
f = [x.strip("\r\n") for x in f]
f = f[1:-1]

def parse(elem):
    occ = ""
    i = 0
    while i < len(elem):
        if elem[i] == '"':
            occ += elem[i]
            i += 1
            while elem[i] != '"':
                occ += elem[i]
                i += 1
            occ += '"'
        elif elem[i] == ",":
            i += 1
            break
        else:
            occ += elem[i]
        i += 1
    pt = float(elem[i:])
    return occ, pt


d = {}
for e in f:
    occ,pt = parse(e)
    d[occ] = pt
print d
