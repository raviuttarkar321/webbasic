import threading
import time
def print_cube(number):
    """
    function to print cube of given num
    """
    num=1
    while num<number:
        print("Cube: {}".format(num * num * num))
        time.sleep(10)
        num=num+1
  
def print_square(number):
    """
    function to print square of given num
    """
    num=1
    while num<number:
        print("Square: {}".format(num * num))
        time.sleep(10)
        num=num+1
        
    
t1 = threading.Thread(target=print_square, args=(10,))
t2 = threading.Thread(target=print_cube, args=(10,))

# starting thread 1
t1.start()

# starting thread 2
t2.start()
# wait until thread 1 is completely executed
t1.join()
# wait until thread 2 is completely executed
t2.join()

# both threads completely executed
print("Done!")