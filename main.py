from utils.production_line import ProductionLine
from utils.producer import Producer
from utils.consumer import Consumer
from queue import Queue
from time import time, sleep
from random import random


class MyProducer(Producer):

    def __init__(self):
        super(MyProducer, self).__init__()
        return

    def run(self, task):
        sleep(random())
        return 'done'


class MyConsumer(Consumer):
    def __init__(self):
        super(MyConsumer, self).__init__()
        return

    def run(self, task):
        sleep(random())
        return 'done'


if __name__ == "__main__":
    t0 = time()
    production_input = Queue()
    clock = Queue()

    ###########################
    for i in range(10):
        production_input.put(i)
        clock.put(i)

    ###########################

    print('There are %d jobs to be done\n' % production_input.qsize())

    production_line = ProductionLine()
    producer = MyProducer()
    consumer = MyConsumer()
    production_line.run(producer, consumer, production_input, clock)
    production_input.join()

    print('Time: {:.2f}s'.format(time() - t0))
