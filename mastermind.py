import random
import tkinter as tk

# Generate random choices
str_options = "YGRWBO"
choices = ""
for ch in range(4): 
    choices += random.choice(str_options)
print(choices)

# Function to create a circle on the canvas
def create_circle(canvas, x, y, r, color):  # center coordinates, radius, color
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1, fill=color, outline="")

# Function to display text on the canvas
def display_text(canvas, text, x0, y0, tag):
    canvas.create_text(x0, y0, text=text, fill="white", font=('Helvetica 15 bold'), tag=tag)

# Function to clear text on the canvas
def clear_text(canvas, tag):
    canvas.delete(tag)

# Function to evaluate user input
def evaluate_input():
    global tries, win
    user_input = entry.get()
    correct = 0
    incorrect = 0

    for u in user_input:
        if u in choices:
            correct += 1
        else:
            incorrect += 1

    clear_text(canvas, "result")
    display_text(canvas, f"Correct: {correct}", 200, 175, "result")
    display_text(canvas, f"Incorrect: {incorrect}", 200, 200, "result")

    tries += 1

    if correct == 4:
        win = True
        clear_text(canvas, "result")
        display_text(canvas, "You win!", 200, 200, "result")
        submit_button.config(state=tk.DISABLED)
    elif tries >= 10:
        display_text(canvas, "No more tries left!", 200, 100, "result")
        submit_button.config(state=tk.DISABLED)

def main():
    global entry, canvas, submit_button, tries, win
    tries = 0
    win = False

    root = tk.Tk()
    root.title("Colored Circles with Tkinter")
    canvas = tk.Canvas(root, width=400, height=300, background="black")
    canvas.pack()

    # Display text on the canvas
    str1 = "These are the options"
    display_text(canvas, str1, 200, 25, "static")
    str2 = "You can choose any 4 of these"
    display_text(canvas, str2, 200, 50, "static")

    # Draw different colored circles
    create_circle(canvas, 50, 100, 25, "yellow")
    create_circle(canvas, 100, 100, 25, "green")
    create_circle(canvas, 150, 100, 25, "red")
    create_circle(canvas, 200, 100, 25, "white")
    create_circle(canvas, 250, 100, 25, "orange")
    create_circle(canvas, 300, 100, 25, "blue")

    # Display generated choices
    display_text(canvas, f"Generated choices: {choices}", 200, 140, "static")

    # Entry widget for user input
    entry = tk.Entry(root)
    entry.pack()

    # Button to submit input
    submit_button = tk.Button(root, text="Submit", command=evaluate_input)
    submit_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
