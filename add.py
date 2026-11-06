def addition(x, y):
    return x + y

if __name__ == "__main__":
    print("Application Started")
    print("10 + 9 = ", addition(10, 9))
    if addition(10, 9) != 19:
        print("Addition failed")
    else:
        print("Application Finished")