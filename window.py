import tkinter
import buttons

root = tkinter.Tk()
root.title("Tabla Periodica")
root.resizable(0, 0)
root.config(bg="grey")

help = tkinter.Label(root, text="Elige uno de los elementos \npara ver la informacion", font=("Arial", 16))
help.grid(row=0, column=4, rowspan=3, columnspan=4)

##############################################################
###                       Fila 1                           ###
##############################################################
H = buttons.Button(root, "H", 0, 0)
He = buttons.Button(root, "He", 0, 17)

##############################################################
###                       Fila 2                           ###
##############################################################
Li = buttons.Button(root, "Li", 1, 0)
Be = buttons.Button(root, "Be", 1, 1)
B  = buttons.Button(root, "B", 1, 12)
C  = buttons.Button(root, "C", 1, 13)
N  = buttons.Button(root, "N", 1, 14)
O  = buttons.Button(root, "O", 1, 15)
F  = buttons.Button(root, "F", 1, 16)
Ne = buttons.Button(root, "Ne", 1, 17)

##############################################################
###                       Fila 3                           ###
##############################################################
Na = buttons.Button(root, "Na", 2, 0)
Mg = buttons.Button(root, "Mg", 2, 1)
Al = buttons.Button(root, "Al", 2, 12)
Si = buttons.Button(root, "Si", 2, 13)
P  = buttons.Button(root, "P", 2, 14)
S  = buttons.Button(root, "S", 2, 15)
Cl = buttons.Button(root, "Cl", 2, 16)
Ar = buttons.Button(root, "Ar", 2, 17)

##############################################################
###                       Fila 4                           ###
##############################################################
K  = buttons.Button(root, "K", 3, 0)
Ca = buttons.Button(root, "Ca", 3, 1)
Sc = buttons.Button(root, "Sc", 3, 2)
Ti = buttons.Button(root, "Ti", 3, 3)
V  = buttons.Button(root, "V", 3, 4)
Cr = buttons.Button(root, "Cr", 3, 5)
Mn = buttons.Button(root, "Mn", 3, 6)
Fe = buttons.Button(root, "Fe", 3, 7)
Co = buttons.Button(root, "Co", 3, 8)
Ni = buttons.Button(root, "Ni", 3, 9)
Cu = buttons.Button(root, "Cu", 3, 10)
Zn = buttons.Button(root, "Zn", 3, 11)
Ga = buttons.Button(root, "Ga", 3, 12)
Ge = buttons.Button(root, "Ge", 3, 13)
As = buttons.Button(root, "As", 3, 14)
Se = buttons.Button(root, "Se", 3, 15)
Br = buttons.Button(root, "Br", 3, 16)
Kr = buttons.Button(root, "Kr", 3, 17)

##############################################################
###                       Fila 5                           ###
##############################################################
Rb = buttons.Button(root, "Rb", 4, 0)
Sr = buttons.Button(root, "Sr", 4, 1)
Y  = buttons.Button(root, "Y", 4, 2)
Zr = buttons.Button(root, "Zr", 4, 3)
Nb = buttons.Button(root, "Nb", 4, 4)
Mo = buttons.Button(root, "Mo", 4, 5)
Tc = buttons.Button(root, "Tc", 4, 6)
Ru = buttons.Button(root, "Ru", 4, 7)
Rh = buttons.Button(root, "Rh", 4, 8)
Pd = buttons.Button(root, "Pd", 4, 9)
Ag = buttons.Button(root, "Ag", 4, 10)
Cd = buttons.Button(root, "Cd", 4, 11)
In = buttons.Button(root, "In", 4, 12)
Sn = buttons.Button(root, "Sn", 4, 13)
Sb = buttons.Button(root, "Sb", 4, 14)
Te = buttons.Button(root, "Te", 4, 15)
I  = buttons.Button(root, "I", 4, 16)
Xe = buttons.Button(root, "Xe", 4, 17)

##############################################################
###                       Fila 6                           ###
##############################################################
Cs = buttons.Button(root, "Cs", 5, 0)
Ba = buttons.Button(root, "Ba", 5, 1)
La = buttons.Button(root, "La", 5, 2)
Hf = buttons.Button(root, "Hf", 5, 3)
Ta = buttons.Button(root, "Ta", 5, 4)
W  = buttons.Button(root, "W", 5, 5)
Re = buttons.Button(root, "Re", 5, 6)
Os = buttons.Button(root, "Os", 5, 7)
Ir = buttons.Button(root, "Ir", 5, 8)
Pt = buttons.Button(root, "Pt", 5, 9)
Au = buttons.Button(root, "Au", 5, 10)
Hg = buttons.Button(root, "Hg", 5, 11)
Tl = buttons.Button(root, "Tl", 5, 12)
Pb = buttons.Button(root, "Pb", 5, 13)
Bi = buttons.Button(root, "Bi", 5, 14)
Po = buttons.Button(root, "Po", 5, 15)
At = buttons.Button(root, "At", 5, 16)
Rn = buttons.Button(root, "Rn", 5, 17)

##############################################################
###                       Fila 7                           ###
##############################################################
Fr  = buttons.Button(root, "Fr", 6, 0)
Ra  = buttons.Button(root, "Ra", 6, 1)
Ac  = buttons.Button(root, "Ac", 6, 2)
Rf  = buttons.Button(root, "Rf", 6, 3)
Db  = buttons.Button(root, "Db", 6, 4)
Sg  = buttons.Button(root, "Sg", 6, 5)
Bh  = buttons.Button(root, "Bh", 6, 6)
Hs  = buttons.Button(root, "Hs", 6, 7)
Mt  = buttons.Button(root, "Mt", 6, 8)
Ds  = buttons.Button(root, "Ds", 6, 9)
Rg  = buttons.Button(root, "Rg", 6, 10)
Cn  = buttons.Button(root, "Cn", 6, 11)
Uut = buttons.Button(root, "Uut", 6, 12)
Fl  = buttons.Button(root, "Fl", 6, 13)
Uup = buttons.Button(root, "Uup", 6, 14)
Lv  = buttons.Button(root, "Lv", 6, 15)
Uus = buttons.Button(root, "Uus", 6, 16)
Uuo = buttons.Button(root, "Uuo", 6, 17)

##############################################################
###                   Fila Lantanidos                      ###
##############################################################
Lantanidos = tkinter.Label(root, text="Lantanidos", font=("Arial", 12))
Lantanidos.grid(row=7, column=1, columnspan=2, sticky="nsew", padx=2, pady=2)

Ce = buttons.Button(root, "Ce", 7, 3)
Pr = buttons.Button(root, "Pr", 7, 4)
Nd = buttons.Button(root, "Nd", 7, 5)
Pm = buttons.Button(root, "Pm", 7, 6)
Sm = buttons.Button(root, "Sm", 7, 7)
Eu = buttons.Button(root, "Eu", 7, 8)
Gd = buttons.Button(root, "Gd", 7, 9)
Tb = buttons.Button(root, "Tb", 7, 10)
Dy = buttons.Button(root, "Dy", 7, 11)
Ho = buttons.Button(root, "Ho", 7, 12)
Er = buttons.Button(root, "Er", 7, 13)
Tm = buttons.Button(root, "Tm", 7, 14)
Yb = buttons.Button(root, "Yb", 7, 15)
Lu = buttons.Button(root, "Lu", 7, 16)

##############################################################
###                   Fila Alcalinos                       ###
##############################################################
Alcalinos = tkinter.Label(root, text="Alcalinos", font=("Arial", 13))
Alcalinos.grid(row=8, column=1, columnspan=2, sticky="nsew", padx=2, pady=2)

Th = buttons.Button(root, "Th", 8, 3)
Pa = buttons.Button(root, "Pa", 8, 4)
U  = buttons.Button(root, "U", 8, 5)
Np = buttons.Button(root, "Np", 8, 6)
Pu = buttons.Button(root, "Pu", 8, 7)
Am = buttons.Button(root, "Am", 8, 8)
Cm = buttons.Button(root, "Cm", 8, 9)
Bk = buttons.Button(root, "Bk", 8, 10)
Cf = buttons.Button(root, "Cf", 8, 11)
Es = buttons.Button(root, "Es", 8, 12)
Fm = buttons.Button(root, "Fm", 8, 13)
Md = buttons.Button(root, "Md", 8, 14)
No = buttons.Button(root, "No", 8, 15)
Lr = buttons.Button(root, "Lr", 8, 16)



root.mainloop()
