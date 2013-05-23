from tkinter import Tk, Canvas, Frame, BOTH

CIRCLE_RADIUS = 100
MARGIN = 10

class Speedometer(Frame):
    
    global canvas
    
    def __init__(self, parent):
        Frame.__init__(self, parent)   

        self.parent = parent        
        self.initUI()

    def initUI(self):
        self.parent.title("Raspberry Pi Sensorik")        
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)          
        canvas.create_oval(MARGIN, MARGIN, CIRCLE_RADIUS*2, CIRCLE_RADIUS*2, outline="#fb0", fill="#fb0", width=2)
        
        #canvas.create_oval(20, 10, 20+CIRCLE_SIZE, CIRCLE_SIZE, outline="#f50", fill="#f50")
        #canvas.create_oval(CIRCLE_SIZE * 3, 10, CIRCLE_SIZE, CIRCLE_SIZE, outline="#05f", fill="#05f")       
        canvas.pack(fill=BOTH, expand=1)
        
def task():
    print("hello")
    #canvas.create_line(MARGIN, MARGIN + CIRCLE_RADIUS, CIRCLE_RADIUS*2, 10+CIRCLE_RADIUS, fill="black")
    #root.after(2000,task)  # reschedule event in 2 seconds

def main():
    root = Tk()
    ex = Speedometer(root)
    root.geometry("400x400+300+300")
    root.after(2000, task())
    root.mainloop()  

if __name__ == '__main__':
    main()  
    print("hey")