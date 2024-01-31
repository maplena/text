
import time

while True:

    with open("test.txt", "a") as file:
        file.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        file.write("\n")
    time.sleep(1)

