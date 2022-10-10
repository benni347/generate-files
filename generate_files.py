#!/usr/bin/env python
"""
This file is used to generate random text files
"""
import os
import random
import datetime
import time

cwd = os.getcwd()


def gen(amount):
    for i in range(amount):
        # this will create amount files.
        now_time = datetime.datetime.now(datetime.timezone.utc)
        unix_time = str(int(time.mktime(now_time.timetuple())))

        try:
            fp = open("./" + unix_time + ".txt", "w")
        except PermissionError:
            print("User doesnt have permission to open file")
        else:
            with fp:
                fp.write(str(random.randbytes(1024)))
        # try:
        #     fp = open("./" + unix_time + ".txt", "r")
        # except PermissionError:
        #     print("User doesnt have permission to open file")
        # else:
        #     with fp:
        #         print(os.path.getsize(fp.name))


if __name__ == "__main__":
    gen(amount=10)
