import inflect

p = inflect.engine()
s = []

while True:
    try:
        pro = input("Input (or press Ctrl+D to finish): ").strip()
        if not pro:
            continue
        s.append(pro)
        sn = p.join(s)
    except (EOFError, KeyboardInterrupt):
        print("Adieu, adieu, to", sn)
        break
