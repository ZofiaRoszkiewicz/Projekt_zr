from tkinter import *
import tkintermapview
from tkinter import ttk
root = Tk()
root.title('System zarządzania księgarniami')
root.geometry('1400x800')
main_frame = Frame(root)
main_frame.pack(fill='both', expand=True, padx=10, pady=10)

# Lewa strona z zakładkami
left_frame = Frame(main_frame)
left_frame.pack(side='left', fill='both', expand=True)

# Prawa strona z mapą
right_frame = Frame(main_frame)
right_frame.pack(side='right', fill='both', expand=True, padx=(10, 0))

# Tworzenie mapy w prawej ramce
map_widget = tkintermapview.TkinterMapView(right_frame, width=700, height=750)
map_widget.pack(fill='both', expand=True)
map_widget.set_position(52.23, 21.00)
map_widget.set_zoom(6)

notebook = ttk.Notebook(left_frame)
notebook.pack(fill='both', expand=True, padx=10, pady=10)

#zakładka z księgarniami
frame_ksiegarnie = ttk.Frame(notebook)
notebook.add(frame_ksiegarnie, text='Księgarnie')
ramka_lista_ksiegarni = Frame(frame_ksiegarnie)
ramka_formularz_ksiegarni = Frame(frame_ksiegarnie)
ramka_szczegoly_ksiegarni = Frame(frame_ksiegarnie)

#zakładka z pracownikami
frame_pracownicy = ttk.Frame(notebook)
notebook.add(frame_pracownicy, text='Pracownicy')
ramka_lista_pracownikow = Frame(frame_pracownicy)
ramka_formularz_pracownikow = Frame(frame_pracownicy)
ramka_lista_pracownikow.grid(row=0, column=0, padx=10, pady=5, sticky='nsew')
ramka_formularz_pracownikow.grid(row=0, column=1, padx=10, pady=5, sticky='nsew')


#zakładka z klientami
frame_klienci = ttk.Frame(notebook)
notebook.add(frame_klienci, text='Klienci')
ramka_lista_klientow = Frame(frame_klienci)
ramka_formularz_klientow = Frame(frame_klienci)
ramka_lista_klientow.grid(row=0, column=0, padx=10, pady=5, sticky='nsew')
ramka_formularz_klientow.grid(row=0, column=1, padx=10, pady=5, sticky='nsew')




root.mainloop()