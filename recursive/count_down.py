def countdown(num):
    print(num)

    if num == 0:
        return
    else:
        countdown(num - 1)

if __name__ == "__main__":
    countdown(10)
