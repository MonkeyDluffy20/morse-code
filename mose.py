import tkinter as tk

code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'
}

def morse():
    text = entry.get().upper()
    t = ''
    
    for char in text:
        if char == ' ':
            t += '    '
        elif char in code:
            t += code[char] + ' '
    result.config(text=t)
window = tk.Tk()
window.title("Morse Code Generator")
window.geometry('300x300')

entry = tk.Entry(window)
entry.pack(pady=10)

button = tk.Button(window,text="Convert to Morse Code", command=morse)
button.pack()

result = tk.Label(window, text="")
result.pack()
window.mainloop()
