# !/usr/bin/dev python
# -*- coding:utf-8 -*-

import requests
import threading
import Queue
import codecs

filePoint = codecs.open('cgi.txt', 'r')
rootURL = 'http://www.blackstxz.com'
pool = list()
queue = Queue.Queue()


def dirScan():
    global filePoint

    for line in filePoint:
        target_url = rootURL + line
        req = requests.get(target_url)
        if req.status_code == 200:
            print 'yes'
            print target_url,

if __name__ == "__main__":
    for i in range(5):
        pool.append(threading.Thread(target=dirScan))

    for thread in pool:
        thread.start()

    for thread in pool:
        thread.join()

    print 'End...'
