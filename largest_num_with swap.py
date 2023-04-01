def largestnum(num):
    num_to_str = list(str(num))
    temp = num_to_str[:]
    for i in range(len(num_to_str)):
        for j in range(i + 1, len(num_to_str)):
            # num_to_str[i], num_to_str[j] = num_to_str[j], num_to_str[i]
            temp2 = num_to_str[i]
            num_to_str[i] = num_to_str[j]
            num_to_str[j] = temp2

            if num_to_str > temp:
                temp = num_to_str[:]

            temp2 = num_to_str[j]
            num_to_str[j] = num_to_str[i]
            num_to_str[i] = temp2
            # num_to_str[i], num_to_str[j] = num_to_str[j], num_to_str[i]

    return int("".join(temp))


def main():
    x = int(2736)
    print(largestnum(x))


if __name__ == "__main__":
    main()
