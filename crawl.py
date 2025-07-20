import sys
import time


def writer(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    time.sleep(1)
    print()
    return None
