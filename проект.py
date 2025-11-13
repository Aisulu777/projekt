import tkinter as tk
from tkinter import ttk

systems = {
    "Екілік (Binary)": 2,
    "Сегіздік (Octal)": 8,
    "Ондық (Decimal)": 10,
    "Он алтылық (Hexadecimal)": 16
}


def get_valid_chars(base):
    if base == 2: return "01"
    if base == 8: return "01234567"
    if base == 10: return "0123456789"
    if base == 16: return "0123456789ABCDEFabcdef"
    return ""


def is_valid_number(value, base):
    return all(c in get_valid_chars(base) for c in value)


def convert_number(*_):
    input_value = input_var.get().strip().upper()
    if not input_value:
        result_var.set("")
        update_counts()
        return

    from_base = systems[from_system.get()]
    to_base = systems[to_system.get()]

    if not is_valid_number(input_value, from_base):
        error_label.config(text=f"⚠ {from_system.get()} үшін қате сан енгізілді")
        result_var.set("")
        update_counts()
        return
    else:
        error_label.config(text="")

    try:
        dec_value = int(input_value, from_base)
        if to_base == 2:
            result = bin(dec_value)[2:]
        elif to_base == 8:
            result = oct(dec_value)[2:]
        elif to_base == 10:
            result = str(dec_value)
        else:
            result = hex(dec_value)[2:].upper()

        result_var.set(result)
        update_counts()
    except Exception:
        error_label.config(text="⚠ Түрлендіру кезінде қате")
        result_var.set("")
        update_counts()


def update_hints(*_):
    hints = {
        2: "Тек 0 және 1 сандарын пайдаланыңыз",
        8: "0-ден 7-ге дейінгі цифрларды пайдаланыңыз",
        10: "0-ден 9-ға дейінгі цифрларды пайдаланыңыз",
        16: "0–9 және A–F пайдаланыңыз"
    }
    res_hints = {
        2: "Екілік түрінде көрсетіледі",
        8: "Сегіздік түрінде көрсетіледі",
        10: "Ондық түрінде көрсетіледі",
        16: "Он алтылық түрінде көрсетіледі"
    }

    from_base = systems[from_system.get()]
    to_base = systems[to_system.get()]

    input_hint_label.config(text=hints[from_base])
    result_hint_label.config(text=res_hints[to_base])
    convert_number()


def update_counts():
    input_digits_label.config(text=f"Сан цифрлары (енгізу): {len(input_var.get().strip())}")
    output_digits_label.config(text=f"Сан цифрлары (нәтиже): {len(result_var.get().strip())}")



root = tk.Tk()
root.title("Сан жүйелерінің түрлендіргіші")
root.geometry("675x470")
root.resizable(False, False)

style = ttk.Style()
style.theme_use('clam')

main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0, sticky="nsew")


systems_frame = ttk.Frame(main_frame)
systems_frame.grid(row=0, column=0, columnspan=2, pady=(0, 15))

left_label = ttk.Label(systems_frame, text="Бастапқы жүйе:", font=('Arial', 10))
left_label.grid(row=0, column=0, sticky="w", pady=(0, 5))

from_system = tk.StringVar(value="Ондық (Decimal)")
from_combo = ttk.Combobox(
    systems_frame, textvariable=from_system,
    values=list(systems.keys()), state='readonly', width=30, font=('Arial', 10)
)
from_combo.grid(row=1, column=0, padx=(0, 20))

right_label = ttk.Label(systems_frame, text="Мақсатты жүйе:", font=('Arial', 10))
right_label.grid(row=0, column=1, sticky="w", pady=(0, 5))

to_system = tk.StringVar(value="Екілік (Binary)")
to_combo = ttk.Combobox(
    systems_frame, textvariable=to_system,
    values=list(systems.keys()), state='readonly', width=30, font=('Arial', 10)
)
to_combo.grid(row=1, column=1, padx=(20, 0))


ttk.Separator(main_frame, orient='horizontal').grid(row=1, column=0, columnspan=2, sticky="ew", pady=15)


ttk.Label(main_frame, text="Құралдар", font=('Arial', 10), foreground='gray').grid(row=2, column=0, columnspan=2, pady=(0, 15))


io_frame = ttk.Frame(main_frame)
io_frame.grid(row=3, column=0, columnspan=2)


input_frame = ttk.Frame(io_frame)
input_frame.grid(row=0, column=0, padx=(0, 20))

ttk.Label(input_frame, text="Санды енгізіңіз:", font=('Arial', 10)).grid(row=0, column=0, sticky="w")
input_var = tk.StringVar()
input_entry = ttk.Entry(input_frame, textvariable=input_var, width=30, font=('Arial', 12))
input_entry.grid(row=1, column=0, pady=(0, 5))
input_hint_label = ttk.Label(input_frame, text="0-ден 9-ға дейінгі цифрларды пайдаланыңыз", font=('Arial', 8), foreground='gray')
input_hint_label.grid(row=2, column=0, sticky="w")


arrow_label = ttk.Label(io_frame, text="→", font=('Arial', 24), foreground='gray')
arrow_label.grid(row=0, column=1, padx=10, pady=30)


output_frame = ttk.Frame(io_frame)
output_frame.grid(row=0, column=2, padx=(20, 0))
ttk.Label(output_frame, text="Нәтиже:", font=('Arial', 10)).grid(row=0, column=0, sticky="w")
result_var = tk.StringVar()
ttk.Entry(output_frame, textvariable=result_var, width=30, font=('Arial', 12), state='readonly').grid(row=1, column=0, pady=(0, 5))
result_hint_label = ttk.Label(output_frame, text="Екілік түрінде көрсетіледі", font=('Arial', 8), foreground='gray')
result_hint_label.grid(row=2, column=0, sticky="w")


error_label = ttk.Label(main_frame, text="", foreground='red', font=('Arial', 9, 'bold'), wraplength=600)
error_label.grid(row=4, column=0, columnspan=2, pady=10)


examples_frame = ttk.LabelFrame(main_frame, text="Мысалдар", padding="10")
examples_frame.grid(row=5, column=0, columnspan=2, pady=10, sticky="ew")

examples_text = (
    "• 1010 (екілік) = 10 (ондық)\n"
    "• 255 (ондық) = FF (он алтылық)\n"
    "• 377 (сегіздік) = 11111111 (екілік)"
)
ttk.Label(examples_frame, text=examples_text, font=('Arial', 9), foreground='gray', justify="left").grid(sticky="w")


ttk.Separator(main_frame, orient='horizontal').grid(row=6, column=0, columnspan=2, sticky="ew", pady=15)


status_frame = ttk.Frame(main_frame)
status_frame.grid(row=7, column=0, columnspan=2, sticky="ew")

input_digits_label = ttk.Label(status_frame, text="Сан цифрлары (енгізу): 0", font=('Arial', 9), foreground='gray')
input_digits_label.grid(row=0, column=0, sticky="w")
output_digits_label = ttk.Label(status_frame, text="Сан цифрлары (нәтиже): 0", font=('Arial', 9), foreground='gray')
output_digits_label.grid(row=0, column=1, sticky="e")


from_combo.bind("<<ComboboxSelected>>", update_hints)
to_combo.bind("<<ComboboxSelected>>", update_hints)
input_var.trace_add("write", convert_number)

update_hints()
root.mainloop()
