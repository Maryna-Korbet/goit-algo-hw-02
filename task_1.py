# TODO: It is necessary to develop a program that simulates the reception and processing of applications: 
# the program should automatically generate new applications (identified by a unique number or other data), 
# add them to the queue, and then sequentially remove them from the queue for "processing", 
# thus simulating the work of a service center.


from queue import Queue
import random
import time

queue = Queue()

def generate_request():
    request = {
        "id": int(time.time() * 1000),
        "data": random.randint(1, 10),
    }

    queue.put(request)
    print(f"Generated request: {request}")

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Processing request: {request}")
        
        time.sleep(1)
        print(f"Request processed: {request}")
    else:
        print(f"Queue is empty")

if __name__ == "__main__":
    while True:
        generate_request()
        process_request()
        time.sleep(4)
