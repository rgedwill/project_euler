
def main():
    f = open("p12_input.txt", "r")
    ans = sum([int(i) for i in f])
    print(ans)
if __name__ == "__main__":
    main()