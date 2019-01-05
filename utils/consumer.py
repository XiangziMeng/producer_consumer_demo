from threading import current_thread

class Consumer(object):

    def __init__(self):
        return

    def consume(self, input, clock):
        name = current_thread().getName()
        while clock.qsize() > 0:
            clock.get()
            clock.task_done()
            to_be_done = clock.qsize()
            task = input.get()
            print(' ' * 26 + '%s, to be done: %d' % (name, to_be_done))
            self.run(task)
            input.task_done()
