# Python implementation of producer-consumer solution with multithreading

### Introduction
This is my python implementation for producer-consumer solution with multithreading, which is
like a production line with multiple consumers and producers.

### Data structures:

production_input: Queue (threading safe)

consumption_input: Queue (threading safe)

producer: an instance of MyProducer inherent from Producer with methods produce and run

consumer: an instance of MyConsumer inherent from Consumer with methods consume and run

### How does the code work:

production_input --  producers -- consumption_input -- consumers -- done

### How does a producer work:

Get a task from production_input, run the task and put the result in consumption_input

### How does a consumer work:

Get a task from consumption_input, run the task without output

### Note:

You could make the demo work defining your own run methods in MyProduction and MyConsumer.
