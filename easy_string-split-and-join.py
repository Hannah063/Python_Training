def split_and_join(line):
    #return line.replace(" ", "-")
    array = line.split()
    return "-".join(array)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)