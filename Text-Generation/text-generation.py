import tkinter as tk
from tkinter import scrolledtext
from transformers import pipeline

def generate_text():
    prompt = prompt_entry.get()
    max_length = int(max_length_entry.get())
    min_length = int(min_length_entry.get())
    num_sequences = int(num_sequences_entry.get())
    
    generator = pipeline("text-generation", model="distilgpt2")
    generated_texts = generator(prompt, max_length=max_length, min_length=min_length, num_return_sequences=num_sequences)
    
    # Clear previous results
    result_box.delete(1.0, tk.END)
    
    # Display each generated sequence
    for i, text in enumerate(generated_texts):
        result_box.insert(tk.END, f"Result {i+1}:\n{text['generated_text']}\n\n")

root = tk.Tk()
root.title("Text Generation GUI")

tk.Label(root, text="Prompt:").grid(row=0, column=0)
prompt_entry = tk.Entry(root, width=50)
prompt_entry.grid(row=0, column=1)

tk.Label(root, text="Max Length:").grid(row=1, column=0)
max_length_entry = tk.Entry(root)
max_length_entry.grid(row=1, column=1)

tk.Label(root, text="Min Length:").grid(row=2, column=0)
min_length_entry = tk.Entry(root)
min_length_entry.grid(row=2, column=1)

tk.Label(root, text="Number of Sequences:").grid(row=3, column=0)
num_sequences_entry = tk.Entry(root)
num_sequences_entry.grid(row=3, column=1)


generate_button = tk.Button(root, text="Generate Text", command=generate_text)
generate_button.grid(row=4, column=0, columnspan=2)

result_box = scrolledtext.ScrolledText(root, height=10, width=50)
result_box.grid(row=5, column=0, columnspan=2)

root.mainloop()
