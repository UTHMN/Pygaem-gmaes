import time
import winsound


# define mode before using function.
mode = "secs"


def countdown(length):
    while length > 0:
        length -= 1
        time.sleep(1)
        print(length)
    winsound.PlaySound('timer-end.mp3', winsound.SND_FILENAME)


countdown(5)
