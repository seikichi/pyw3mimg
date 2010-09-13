#!/usr/bin/python
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE

class W3MImageDisplay(object):
    """wrapper of w3mimgdisplay
    """

    def __init__(self, path='w3mimgdisplay', auto_sync=True):
        """
        Arguments:
        - `path`: path to w3mimgdisplay
        - `auto_sync`: sync automaticaly
        """
        self._path = path
        self._auto_sync = auto_sync
        self._proc = Popen(self._path, shell=True, stdin=PIPE, stdout=PIPE)
        self._proc.stdin.flush()

    def write(self, s):
        self._proc.stdin.write(s)
        self._proc.stdin.flush()

    def draw(self, path, n, x, y, w=0, h=0, sx=0, sy=0, sw=0, sh=0):
        self.write('0;%d;%d;%d;%d;%d;%d;%d;%d;%d;%s\n' % (n, x, y, w, h, sx, sy, sw, sh, path))
        if self._auto_sync:
            self.sync()

    def redraw(self, path, n, x, y, w=0, h=0, sx=0, sy=0, sw=0, sh=0):
        self.write('1;%d;%d;%d;%d;%d;%d;%d;%d;%d;%s\n' % (n, x, y, w, h, sx, sy, sw, sh, path))
        if self._auto_sync:
            self.sync()

    def terminate(self):
        self.write('2;\n')

    def sync(self):
        self.write('3;\n')

    def nop(self):
        self.write('4;\n')
        self._proc.stdout.readline()

    def get_size(self, path):
        self.write('5;\n')
        wh = self._proc.stdout.readline().split(' ')
        return (int(wh[0]), int(wh[1]))

    def clear(self, x, y, w, h):
        self.write('6;%d;%d;%d;%d\n', x, y, w, h)


