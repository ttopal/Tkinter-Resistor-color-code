import tkinter as tk
import tkinter.ttk as ttk

# internals
from .rescodegui import ResCodeWidget


class ResCode(ResCodeWidget):
    def __init__(self, *args, **kwargs):
        ResCodeWidget.__init__(self, *args, **kwargs)

        self.color_12 = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "gray", "white"]
        self.color_mult = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "gray", "white", "gold", "silver"]
        self.color_tol = ["brown", "red", "green", "blue", "violet", "gray", "gold", "silver"]
        self.tol_val = ["1%", "2%", "0.5%", "0.25%", "0.1%", "0.05%", "5%", "10%"]
        
        self.band_select_var.set(True)
        
        self.img1 = tk.PhotoImage(file="R1.png")
        self.cn_image.create_image( 0, 0, image = self.img1, anchor = "nw")

        
        
    def calculate_resval(self):    
        self.band_1 = self.color1_sc_val.get()
        self.band_2 = self.color2_sc_val.get()
        self.band_3 = self.color3_sc_val.get()
        self.band_4 = self.color4_sc_val.get()
        self.band_5 = self.color5_sc_val.get()
        
        if  self.band_select_var.get():
            self.Resval = (self.band_1 * 100 + self.band_2 * 10 + self.band_3) * 10 ** self.band_4
        else:
            self.Resval = (self.band_1 * 10 + self.band_2) * 10 ** self.band_4
        
        if self.Resval > 1000000000:
            self.Resval /= 1000000000
            self.kmgval ="G Ohms"
        elif self.Resval > 1000000:
            self.Resval /= 1000000
            self.kmgval ="M Ohms"
        elif self.Resval > 1000:
            self.Resval /= 1000
            self.kmgval ="K Ohms"
        else:
            self.kmgval ="Ohms"

        self.lb_res['text'] = f"{self.Resval}{self.kmgval} ± {self.tol_val[self.band_5]}"




    def color1_sc_res(self, event=None):
        val = self.color1_sc_val.get()
        self.lb_scale1_res['text'] = str(val)
        self.cn_color1['bg']=self.color_12[val]
        return val

    def color2_sc_res(self, event=None):
        val = self.color2_sc_val.get()
        self.lb_scale2_res['text'] = str(val)
        self.cn_color2['bg']=self.color_12[val]
        return val

    def color3_sc_res(self, event=None):
        val = self.color3_sc_val.get()
        self.lb_scale3_res['text'] = str(val)
        self.cn_color3['bg']=self.color_12[val]
        return val

    def color4_sc_res(self, event=None):
        val = self.color4_sc_val.get()
        self.lb_scale4_res['text'] = str(val)
        self.cn_color4['bg']=self.color_mult[val]
        return val

    def color5_sc_res(self, event=None):
        val = self.color5_sc_val.get()
        self.lb_scale5_res['text'] = str(val)
        self.cn_color5['bg']=self.color_tol[val]
        return val

    def band_selected(self):
        if  not self.band_select_var.get():
            self.lb_scale3.pack_forget()
            self.sc_color3.pack_forget()
            self.lb_scale3_res.pack_forget()
            self.cn_color3.pack_forget()
        else:
            self.lb_scale3.pack(padx=10, pady=10, side="top")
            self.sc_color3.pack(pady=5, side="top")
            self.lb_scale3_res.pack(pady=10, side="top")
            self.cn_color3.pack(anchor="ne", padx=10, pady=30, side="left")
    
    def calc_rescode(self):
        self.calculate_resval()
        
