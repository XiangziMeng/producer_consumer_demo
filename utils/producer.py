from threading import current_thread

class Producer(object):

    def __init__(self):
        return

    def produce(self, input, output):
        name = current_thread().getName()
        while input.qsize() > 0:
            task = input.get()
            print('%s, to be done: %d' % (name, input.qsize()))
            output.put(self.run(task))
            input.task_done()
