from threading import Thread
from queue import Queue

class ProductionLine(object):

    def __init__(self):
        return

    def run(self, producer, consumer, production_input, clock, n_producer=2, n_consumer=2):
        consumption_input = Queue()
        threads = []
        for n in range(n_producer):
            threads.append(Thread(target=producer.produce, args=(production_input, consumption_input), name='producer_%d' % n))
        for n in range(n_consumer):
            threads.append(Thread(target=consumer.consume, args=(consumption_input, clock), name='consumer_%d' % n))
        for t in threads:
            t.daemon = True
            t.start()
        for t in threads:
            t.join()
