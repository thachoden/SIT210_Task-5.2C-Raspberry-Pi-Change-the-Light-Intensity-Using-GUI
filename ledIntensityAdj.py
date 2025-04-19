import tkinter as tk
import RPi.GPIO as GPIO

class LEDControl:
    def __init__(self, master):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        
        self.pwm = GPIO.PWM(17, 100)
        self.pwm.start(0)
        
        master.title("LED Control")
        
        tk.Scale(
            master, 
            from_=0, 
            to=100, 
            orient=tk.HORIZONTAL, 
            label="LED Brightness",
            command=lambda value: self.pwm.ChangeDutyCycle(float(value))
        ).pack(fill = tk.X, padx=20, pady=20)
        
# Create exit button
        self.exit_button = tk.Button(master, text="Exit", command=self.close)
        self.exit_button.pack(pady=20)
        master.protocol("WM_DELETE_WINDOW", self.close)
    
    def close(self):
        self.pwm.stop()
        GPIO.cleanup()
        root.quit()

root = tk.Tk()
LEDControl(root)
root.mainloop()
