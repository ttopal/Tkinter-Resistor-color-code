# ResistorColor Code GUI
import tkinter as tk
import tkinter.ttk as ttk


class ResCodeWidget(ttk.Panedwindow):
    def __init__(self, master=None, **kw):
        super(ResCodeWidget, self).__init__(master, **kw)
        self.F_color = ttk.Frame(self)
        self.F_color.configure(height=200, padding=10, width=200)
        self.F_cncolor = ttk.Frame(self.F_color)
        self.F_cncolor.configure(height=200, width=200)
        self.cn_color1 = tk.Canvas(self.F_cncolor)
        self.cn_color1.configure(background="black", height=100, width=30)
        self.cn_color1.pack(anchor="ne", padx=10, pady=30, side="left")
        self.cn_color2 = tk.Canvas(self.F_cncolor)
        self.cn_color2.configure(background="brown", height=100, width=30)
        self.cn_color2.pack(anchor="ne", padx=10, pady=30, side="left")
        self.F_cnv3 = ttk.Frame(self.F_cncolor)
        self.F_cnv3.configure(height=100, width=30)
        self.cn_color3 = tk.Canvas(self.F_cnv3)
        self.cn_color3.configure(background="red", height=100, width=30)
        self.cn_color3.pack(anchor="ne", padx=10, pady=30, side="left")
        self.F_cnv3.pack(side="left")
        self.cn_color4 = tk.Canvas(self.F_cncolor)
        self.cn_color4.configure(background="blue", height=100, width=30)
        self.cn_color4.pack(anchor="ne", padx=10, pady=30, side="left")
        self.cn_color5 = tk.Canvas(self.F_cncolor)
        self.cn_color5.configure(background="green", height=100, width=30)
        self.cn_color5.pack(anchor="ne", padx=10, pady=30, side="left")
        self.F_cncolor.pack(side="left")
        self.F_cnimg = ttk.Frame(self.F_color)
        self.cn_image = tk.Canvas(self.F_cnimg)
        self.cn_image.pack(side="right")
        self.F_cnimg.pack(padx=10, side="left")
        self.F_color.pack(side="top")
        self.add(self.F_color, weight="1")
        self.F_scale = ttk.Frame(self)
        self.F_scale.configure(height=200, width=200)
        self.F_sc1 = ttk.Frame(self.F_scale)
        self.F_sc1.configure(height=200, width=150)
        self.lb_scale1 = ttk.Label(self.F_sc1)
        self.lb_scale1.configure(text='1. Band')
        self.lb_scale1.pack(padx=10, pady=10, side="top")
        self.sc_color1 = ttk.Scale(self.F_sc1)
        self.color1_sc_val = tk.IntVar(value=0)
        self.sc_color1.configure(
            cursor="hand2",
            from_=0,
            orient="vertical",
            to=9,
            value=0,
            variable=self.color1_sc_val)
        self.sc_color1.pack(pady=5, side="top")
        self.sc_color1.bind("<B1-Motion>", self.color1_sc_res, add="")
        self.lb_scale1_res = ttk.Label(self.F_sc1)
        self.lb_scale1_res.configure(
            compound="top", justify="center", text='0')
        self.lb_scale1_res.pack(pady=10, side="top")
        self.F_sc1.pack(anchor="ne", padx=3, pady=5, side="left")
        self.F_sc2 = ttk.Frame(self.F_scale)
        self.F_sc2.configure(height=200, width=150)
        self.lb_scale2 = ttk.Label(self.F_sc2)
        self.lb_scale2.configure(text='2. Band')
        self.lb_scale2.pack(padx=10, pady=10, side="top")
        self.sc_color2 = ttk.Scale(self.F_sc2)
        self.color2_sc_val = tk.IntVar(value=0)
        self.sc_color2.configure(
            cursor="hand2",
            from_=0,
            orient="vertical",
            to=9,
            value=0,
            variable=self.color2_sc_val)
        self.sc_color2.pack(pady=5, side="top")
        self.sc_color2.bind("<B1-Motion>", self.color2_sc_res, add="")
        self.lb_scale2_res = ttk.Label(self.F_sc2)
        self.lb_scale2_res.configure(text='0')
        self.lb_scale2_res.pack(pady=10, side="top")
        self.F_sc2.pack(anchor="ne", padx=3, pady=5, side="left")
        self.F_sc3 = ttk.Frame(self.F_scale)
        self.F_sc3.configure(height=200, width=150)
        self.lb_scale3 = ttk.Label(self.F_sc3)
        self.lb_scale3.configure(text='3. Band')
        self.lb_scale3.pack(padx=10, pady=10, side="top")
        self.sc_color3 = ttk.Scale(self.F_sc3)
        self.color3_sc_val = tk.IntVar(value=0)
        self.sc_color3.configure(
            cursor="hand2",
            from_=0,
            orient="vertical",
            to=9,
            value=0,
            variable=self.color3_sc_val)
        self.sc_color3.pack(pady=5, side="top")
        self.sc_color3.bind("<B1-Motion>", self.color3_sc_res, add="")
        self.lb_scale3_res = ttk.Label(self.F_sc3)
        self.lb_scale3_res.configure(text='0')
        self.lb_scale3_res.pack(pady=10, side="top")
        self.F_sc3.pack(anchor="ne", padx=3, pady=5, side="left")
        self.F_sc4 = ttk.Frame(self.F_scale)
        self.F_sc4.configure(height=200, width=150)
        self.lb_scale4 = ttk.Label(self.F_sc4)
        self.lb_scale4.configure(text='Multiplier')
        self.lb_scale4.pack(padx=10, pady=10, side="top")
        self.sc_color4 = ttk.Scale(self.F_sc4)
        self.color4_sc_val = tk.IntVar(value=0)
        self.sc_color4.configure(
            cursor="hand2",
            from_=0,
            orient="vertical",
            to=11,
            value=0,
            variable=self.color4_sc_val)
        self.sc_color4.pack(pady=5, side="top")
        self.sc_color4.bind("<B1-Motion>", self.color4_sc_res, add="")
        self.lb_scale4_res = ttk.Label(self.F_sc4)
        self.lb_scale4_res.configure(text='0')
        self.lb_scale4_res.pack(pady=10, side="top")
        self.F_sc4.pack(anchor="ne", padx=3, pady=5, side="left")
        self.F_sc5 = ttk.Frame(self.F_scale)
        self.F_sc5.configure(height=200, width=150)
        self.lb_scale5 = ttk.Label(self.F_sc5)
        self.lb_scale5.configure(text='Tolerans')
        self.lb_scale5.pack(padx=10, pady=10, side="top")
        self.sc_color5 = ttk.Scale(self.F_sc5)
        self.color5_sc_val = tk.IntVar(value=0)
        self.sc_color5.configure(
            cursor="hand2",
            from_=0,
            orient="vertical",
            to=7,
            value=0,
            variable=self.color5_sc_val)
        self.sc_color5.pack(pady=5, side="top")
        self.sc_color5.bind("<B1-Motion>", self.color5_sc_res, add="")
        self.lb_scale5_res = ttk.Label(self.F_sc5)
        self.lb_scale5_res.configure(text='0')
        self.lb_scale5_res.pack(pady=10, side="top")
        self.F_sc5.pack(anchor="ne", padx=3, pady=5, side="left")
        self.F_rbtn = ttk.Frame(self.F_scale)
        self.F_rbtn.configure(height=200, width=200)
        self.cbtn_band5 = ttk.Checkbutton(self.F_rbtn)
        self.band_select_var = tk.BooleanVar()
        self.cbtn_band5.configure(
            cursor="hand2",
            text='5-Band',
            variable=self.band_select_var)
        self.cbtn_band5.pack(anchor="center", pady=10, side="top")
        self.cbtn_band5.configure(command=self.band_selected)
        self.btn_calc = ttk.Button(self.F_rbtn)
        self.btn_calc.configure(text='Calculate')
        self.btn_calc.pack(anchor="center", pady=20, side="bottom")
        self.btn_calc.configure(command=self.calc_rescode)
        self.F_rbtn.pack(anchor="ne", ipadx=10, pady=40, side="left")
        self.F_result = ttk.Frame(self.F_scale)
        self.F_result.configure(height=200, width=200)
        self.lb_result = ttk.Label(self.F_result)
        self.lb_result.configure(
            font="{verdana} 14 {bold}",
            text='Resistor Value')
        self.lb_result.pack(
            anchor="center",
            expand="true",
            fill="both",
            pady=5,
            side="top")
        self.lb_res = ttk.Label(self.F_result)
        self.lb_res.configure(font="{verdana} 13 {}", text='0')
        self.lb_res.pack(expand="true", fill="both", pady=5, side="top")
        self.F_result.pack(padx=10, side="right")
        self.F_scale.pack(side="top")
        self.add(self.F_scale, weight="1")
        self.configure(height=500, width=650)
        self.pack(side="top")

    def color1_sc_res(self, event=None):
        pass

    def color2_sc_res(self, event=None):
        pass

    def color3_sc_res(self, event=None):
        pass

    def color4_sc_res(self, event=None):
        pass

    def color5_sc_res(self, event=None):
        pass

    def band_selected(self):
        pass

    def calc_rescode(self):
        pass

