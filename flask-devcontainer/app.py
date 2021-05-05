import threading
import time

# import debugpy

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    dwarfs = ['Doc', 'Happy', 'Grumpy', 'Sleepy', 'Bashful', 'Sneezy', 'Dopey']
    
    t = time.time()
    
    t1 = threading.Thread(target=greet_them, args=(dwarfs,))
    t2 = threading.Thread(target=assign_id, args=(dwarfs,))
    
    t1.start()
    t2.start()
    
    # t1.join()
    # t2.join()
    
    print("Time to finish was {timelapsed}".format(timelapsed=time.time()-t))
    # print("Debugpy version: {version}".format(version=debugpy.__version__))    
    return "Hello, Flask!"

# t1 thread
def greet_them(dwarfs):
    greet_them_sub(dwarfs)
 
def greet_them_sub(dwarfs):
    for dwarf in dwarfs:
        print("Hello Dears {dwarf}. How are you?".format(dwarf=dwarf))
        # breakpoint()
        # Look at the vscode 'CALL STACK' in the lower left
        # Move cursor over the 'Thread-X' discover debugging options
        time.sleep(2)
 
# t2 thread
def assign_id(dwarfs):
    assign_id_sub(dwarfs)

def assign_id_sub(dwarfs):
    i = 1
    for dwarf in dwarfs:
        print("Hey! {dwarf}, your id is {i}.".format(dwarf=dwarf, i=i))
        i += 1
        # breakpoint()
        # Look at the vscode 'CALL STACK' in the lower left
        # Move cursor over the 'Thread-X' discover debugging options
        time.sleep(2)        
 
if __name__ == '__main__':
    app.run(threaded=False, debug=False)
