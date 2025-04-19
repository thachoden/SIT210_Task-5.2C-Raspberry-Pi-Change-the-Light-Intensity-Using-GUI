import tkinter as tk
import RPi.GPIO as GPIO

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

# Create PWM
pwm = GPIO.PWM(17, 100)
pwm.start(0)

# Create main window
root = tk.Tk()
root.title("LED Brightness Control")
root.geometry("400x300")  # Set window size
root.configure(bg='#f0f0f0')  # Light gray background

# Create frame for better layout
frame = tk.Frame(root, bg='#f0f0f0')
frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

# Title Label
title_label = tk.Label(
    frame, 
    text="LED Brightness Control", 
    font=("Arial", 16, "bold"),
    bg='#f0f0f0'
)
title_label.pack(pady=(0, 20))

# Slider for LED Brightness
brightness_slider = tk.Scale(
    frame,
    from_=0,
    to=100,
    orient=tk.HORIZONTAL,
    length=300,
    label="Adjust Brightness",
    sliderlength=20,
    width=15,
    command=lambda value: pwm.ChangeDutyCycle(float(value))
)
brightness_slider.pack(pady=10)

# Current Value Display
value_label = tk.Label(
    frame, 
    text="Current Brightness: 0%", 
    font=("Arial", 12),
    bg='#f0f0f0'
)
value_label.pack(pady=10)

# Update function for value display
def update_value(value):
    value_label.config(text=f"Current Brightness: {value}%")
    pwm.ChangeDutyCycle(float(value))

# Modify slider to use update function
brightness_slider.config(command=update_value)

# Exit Button
def on_closing():
    pwm.stop()
    GPIO.cleanup()
    root.quit()

exit_button = tk.Button(
    frame, 
    text="Exit", 
    command=on_closing,
    bg='#ff6347',  # Tomato red
    fg='white',
    font=("Arial", 12)
)
exit_button.pack(pady=20)

# Ensure proper cleanup on window close
root.protocol("WM_DELETE_WINDOW", on_closing)

# Start the application
root.mainloop()
