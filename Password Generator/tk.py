import tkinter as tk
import passwordGen as passwordModule

main_window = tk.Tk(className="password_generator")
main_window.geometry("400x200")
main_window.resizable(False, False)

mainFrame = tk.Frame(main_window)
headerLabel = tk.Label(main_window,text="password_generator window", anchor="center").pack(pady=10)

length_text = tk.Label(
    main_window,
    text="password_length",
    font=("default", 8)
).pack(pady=0.5)
length_var = tk.StringVar(main_window)
length_input = tk.Entry(
    main_window,
    textvariable=length_var,
    width=30,
    justify="center"
).pack(pady=1)

output_text = tk.Label(
    main_window,
    text="generated_password",
    font=("default", 8)
).pack(pady=0.5)
output_var = tk.StringVar(main_window)
output_input = tk.Entry(
    main_window,
    width=30,
    textvariable=output_var,
    state="readonly",
    justify="center"
).pack(pady=1)

generate_button = tk.Button(
    main_window,
    width=20,
    text="generate",
    command=lambda : output_var.set(passwordModule.Generate(int(length_var.get()))),
    repeatdelay=1
).pack(pady=20)

main_window.mainloop()