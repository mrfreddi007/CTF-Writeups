#!/usr/bin/env python3
import sys
import time
import random
import hashlib

def seed():
    a = round(time.time())
    print(a)
    return a

def hash(text):
    return hashlib.sha256(str(text).encode()).hexdigest()

def main():
    s = 1636222760
    while True:
        for i in range(10000000):
            s = s - 1
            random.seed(s, version=2)
            x = random.random()
             
            # x = 0.016879293473860302
            flag = hash(x)

            if 'b9ff3ebf' in flag:
                with open("./flag.txt", "w") as f:
                    f.write(f"dam{{{flag}}}")
                    print(f"Flag is: dam{{{flag}}}")
                f.close()
                return

if __name__ == "__main__":
   sys.exit(main())
