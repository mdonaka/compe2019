import csv

if __name__ == "__main__":

    with open("result/04", "r") as f:
        reader = csv.reader(f)
        cnt = 0
        all = 0
        for i, row in enumerate(reader):
            if not i%3 == 1:
                continue
            all += 1

            ok = True
            for x in row:
                if float(x) < 0:
                    ok = False
            if ok:
                cnt += 1
        print(all, cnt)
