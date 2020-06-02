import time

class Timer(object):
    STDOUT=0
    STRING=1
    SILENT=2
    def __init__(self, name="timer", tic=False, show=None):
        self._name = name
        self._start = None
        self._last = None
        self._end = None
        if tic:
            self.tic(show)

    def tic(self, show=None):
        now = time.time()
        if self._start is None:
            self._start = now
            msg = "Timer %s starts" % self._name
            self._last = now
        else:
            elapsed = now - self._last
            msg = "Timer %s: %.2f sec elapsed" % (self._name, elapsed)
            self._last = now
        if show == Timer.STDOUT:
            print(msg)
        elif show == Timer.STRING:
            return msg

    def toc(self, show=None):
        if self._start is None:
            msg = "Timer %s did not start" % (self._name)
        else:
            msg = self.tic(Timer.STRING)
            now = time.time()
            total = now - self._start
            msg += "\nTimer %s stops: %.2f sec elapsed" % (self._name, total)
            self._start = None
        if show == Timer.STDOUT:
            print(msg)
        elif show == Timer.STRING:
            return msg
