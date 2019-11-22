if __name__ == '__main__':
    while 1:
        try:
            line = input()
            if not line[:-1] == "" and not "evaluating" in line:
                print(line)
        except EOFError:
            break
