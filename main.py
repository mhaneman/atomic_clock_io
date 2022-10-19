import threading

""" ~~~~~~~~~~ EXPECTATIONS OF SOFTWARE ~~~~~~~~~~
1.  collect data from hardware
    a. -> collect in specific time increments
    b. -> Store this data in CSV

2.  from collected data, determine a fit for the accuracy of atomic clock
    a. -> visually plot of the data and fit 
    b. -> give data such as certainty, min intensity, which cycle

3.  continously graph the accuracy per cycle
    a. -> graph linear bounds for certainty
"""


""" ~~~~~~~~~~ IMPLEMENTATION OF EXPECTATIONS ~~~~~~~~~~
1.  have a thread for a data buffer
    a. -> the time it takes to collect hardware data is independent of runtime

2.  have a async matplotlib graphs
    a. -> updates and processes whenever new data is recieved
"""

""" ~~~~~~~~~~ GAME PLAN ~~~~~~~~~~
1. HARDWARE IO
    a. -> init the software for data collection
    b. -> recieve hardare data
            -> test if thread time is consistent
        

2. FIT DATA
    a. -> 
"""

def get_new_data(num):
    # function to print cube of given num
    print("Cube: {}" .format(num * num * num))
 
 
def process_current_data():
    # function to print square of given num
    print("Square: {}" .format(num * num))

def live_graph():
    pass
 
 
if __name__ =="__main__":
    t1 = threading.Thread(target=get_new_data, args=(10,))
    t2 = threading.Thread(target=process_current_data, args=(10,))
 
    t1.start()
    t2.start()
 
    t1.join()
    t2.join()
    # both threads completely executed