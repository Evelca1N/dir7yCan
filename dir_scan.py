# !/usr/bin/dev python
# -*- coding:utf-8 -*-

from gevent import monkey; monkey.patch_all()
import requests
import codecs
import optparse
import gevent

filePoint = 0
pool = list()


def openDict(dict_name):
    global filePoint
    suc = True
    try:
        filePoint = codecs.open(dict_name, 'r')
    except Exception as e:
        print e
        suc = False
        filePoint.close()
    return suc


def dirScan(target_url):
    global filePoint

    for line in filePoint:
        target_url = target_url + line
        req = requests.get(target_url)
        if req.status_code == 200:
            print '[!]sensetive file found at url : %s' % (target_url)


if __name__ == "__main__":

    # 解析传入的参数
    parser = optparse.OptionParser('python dir_scan.py -u url --gevent 10 \
--dict dir.txt')
    parser.add_option('-u', dest='url', help=\
            'url to start sensitive file search')
    parser.add_option('--gevet', dest='gevent_num', help=\
            'gevent nubmer for scanning', default=10)
    parser.add_option('--dict', dest='dic', help=\
            'dictionary used', default='dir.txt')
    (options, args) = parser.parse_args()

    if options.url and openDict(options.dic):
        for i in range(options.gevent_num):
            pool.append(gevent.spawn(dirScan, options.url))
        gevent.joinall(pool)
    else:
        print parser.print_help()

