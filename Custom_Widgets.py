###
### Name of project: Custom_Widgets.py
###
### Author: CyberCoral
###
### Main repository of file: 
###
### Date of creation: 21 / October / 2024
###
### Description: It is a library that has shortcuts to
###              Tkinter ttk widgets and its own class, 
###              which contains methods that create those widgets
###              for easier use, reducing the total lines of code.
###
### Summary of use: This program can be used as a standalone
###                 program (it will run a sample program by default),
###                 or it can serve as a library for other
###                 programs.
###

import tkinter as tk
from tkinter import ttk

###
### Create a personalized widget initializer, add buttons next.
###

widgets = ["label","entry","button"]

class Personalized_Widget:
    def __init__(self, stringvar: tk.StringVar, master: tk.Tk):
        if not isinstance(stringvar, tk.StringVar):
            raise TypeError("A labeled entry needs a tk.StringVar variable.")
        elif not isinstance(master, tk.Tk) and not isinstance(master, ttk.Frame):
            raise TypeError("The master must be either a tk.Tk or ttk.Frame object.")
        self.strvar = stringvar
        self.master = master
        self.widgets = []
        self.label = None
        self.entry = None
        self.button = None
        
    
    def Label(self,**kwargs):
        try:
            self.label = ttk.Label(self.master,**kwargs)
            self.widgets.append("label")
        except TypeError:
            raise NameError("ttk.Label() got an unexpected keyword argument. Check the name of the arguments of Label().")
    
    def Entry(self,**kwargs):
        if "textvariable" in list(kwargs.keys()):
            raise IndexError("By default, textvariable is always included.")
        try:
            self.entry = ttk.Entry(self.master,textvariable=self.strvar, **kwargs)
            self.widgets.append("entry")
        except TypeError:
            raise NameError("ttk.Entry() got an unexpected keyword argument. Check the name of the arguments of Entry().")
        
    def Button(self, **kwargs):
        try:
            self.button = ttk.Button(self.master, **kwargs)
            self.widgets.append("button")
        except TypeError:
            raise NameError("ttk.Button() got an unexpected keyword argument. Check the name of the arguments of Button().")
        
    def Entry_with_Label(self,label_kwargs, entry_kwargs):
        self.Label(**label_kwargs)
        self.Entry(**entry_kwargs)
        print("An entry with label has been created.")
        
    def Entry_Label_Button(self, label_kwargs, entry_kwargs, button_kwargs):
        self.Label(**label_kwargs)
        self.Entry(**entry_kwargs)
        self.Button(**button_kwargs)
        print("An entry with label and a button has been created.")
    
    def Label_with_Button(self, label_kwargs, button_kwargs):
        self.Label(**label_kwargs)
        self.Button(**button_kwargs)
        print("A label with a button has been created.")
        
    def Pack(self, args: dict = {"fill":"x","expand":True}):
        widgets_used = self.widgets
        if not isinstance(widgets_used, list):
            raise TypeError("The widgets_used variable must be a list.")
        
        widgets_used = list(set([i for i in widgets_used if i in widgets]))
        if len(widgets_used) == 0 or len(args) == 0:
            return
        
        if not isinstance(args, dict):
            raise TypeError("args must be a dictionary.")
        
        for i in widgets_used:
            try:
                eval(f"self.{i}.pack(**args)")
                if i == "entry":
                    eval(f"self.{i}.focus()")
            except Exception as e:
                print("{} could not be packed because of {}.".format(i,e))
                pass
            if len(args) == widgets.index(i) + 1:
                break

    def Grid(self, *args):
        widgets_used = self.widgets
        if not isinstance(widgets_used, list):
            raise TypeError("The widgets_used variable must be a list.")
        
        widgets_used = [i for i in widgets_used if i in widgets]
        
        if not isinstance(args, list) and not isinstance(args, tuple):
            raise TypeError("args must be a list.")
        
        if len(widgets_used) < len(args):
            widgets_used = widgets_used[:len(args)]
        for i in widgets_used:
            try:
                kwargs = args[widgets_used.index(i)]
                eval(f"self.{i}.grid(**kwargs)")
                if i == "entry":
                    eval(f"self.{i}.focus()")
            except Exception as e:
                print("{} could not be packed because of {}.".format(i,e))
                pass
            if len(args) == widgets.index(i) + 1:
                break
        
    
def EntryWithLabel(strvar, master, label_kwargs={"text":"sample text"}, entry_kwargs={}, pack_kwargs={"fill":"x","expand":True},*,pack_or_grid: bool = True, grid_kwargs: list = [{}, {}]):
    '''
    Defines an entry with label, given the kwargs, stringvar and master.    

    Parameters
    ----------
    strvar : tk.StringVar
        The string var which stores the data
    master : tk.Tk
        The root of the entry.
    label_kwargs : dict (must exist in ttk.Label())
        The kwargs for the label.
    entry_kwargs : dict (must exist in ttk.Entry())
        The kwargs for the entry.
    pack_kwargs : dict (must exist in .pack())
        The kwargs for the .pack() invocation.
    pack_or_grid : bool
        True for packing, False for using grid.

    Returns
    -------
    labeled_entry object.

    '''
    entry_obj = Personalized_Widget(strvar,master)
    entry_obj.Entry_with_Label(label_kwargs, entry_kwargs)
    if not isinstance(pack_or_grid, bool):
        raise TypeError("not_pack must be a bool.")
    elif pack_or_grid == True:
        entry_obj.Pack(pack_kwargs)
    else:
        entry_obj.Grid(grid_kwargs)
    
    return entry_obj

def EntryLabelButton(strvar, master, label_kwargs={"text":"sample text"}, entry_kwargs={}, button_kwargs = {"command":lambda _: 0}, pack_kwargs={"fill":"x","expand":True},*,pack_or_grid: bool = True, grid_kwargs: list = [{}, {}, {}]):
    '''
    Creates an entry with a label and a button,
    given the kwargs, stringvar and master.
    '''
    entry_obj = Personalized_Widget(strvar,master)
    entry_obj.Entry_Label_Button(label_kwargs, entry_kwargs, button_kwargs)
    if not isinstance(pack_or_grid, bool):
        raise TypeError("not_pack must be a bool.")
    elif pack_or_grid == True:
        entry_obj.Pack(pack_kwargs)
    else:
        entry_obj.Grid(*grid_kwargs)
    
    return entry_obj

def Label_with_Button(strvar, master, label_kwargs={"text":"sample text"}, button_kwargs = {"text":"Example","command":lambda _: 0}, pack_kwargs={"fill":"x","expand":True},*,pack_or_grid: bool = True, grid_kwargs: list = [{}, {}]):
    '''
    Creates an entry with a label and a button,
    given the kwargs, stringvar and master.
    '''
    entry_obj = Personalized_Widget(strvar,master)
    entry_obj.Label_with_Button(label_kwargs, button_kwargs)
    if not isinstance(pack_or_grid, bool):
        raise TypeError("not_pack must be a bool.")
    elif pack_or_grid == True:
        entry_obj.Pack(pack_kwargs)
    else:
        entry_obj.Grid(*grid_kwargs)
    
    return entry_obj

def Entry(strvar, master, entry_kwargs = {}, pack_kwargs={"fill":"x","expand":True},*,pack_or_grid: bool = True, grid_kwargs: list = [{}]):
    '''
    Creates a label with the given kwargs,
    stringvar and master.
    '''
    entry_obj = Personalized_Widget(strvar,master)
    entry_obj.Entry(**entry_kwargs)
    if not isinstance(pack_or_grid, bool):
        raise TypeError("not_pack must be a bool.")
    elif pack_or_grid == True:
        entry_obj.Pack(pack_kwargs)
    else:
        entry_obj.Grid(*grid_kwargs)
    
    return entry_obj

def Label(strvar, master, label_kwargs={"text":"sample text"}, pack_kwargs={"fill":"x","expand":True},*,pack_or_grid: bool = True, grid_kwargs: list = [{}]):
    '''
    Creates a label with the given kwargs,
    stringvar and master.
    '''
    entry_obj = Personalized_Widget(strvar,master)
    entry_obj.Label(**label_kwargs)
    if not isinstance(pack_or_grid, bool):
        raise TypeError("not_pack must be a bool.")
    elif pack_or_grid == True:
        entry_obj.Pack(pack_kwargs)
    else:
        entry_obj.Grid(*grid_kwargs)
    
    return entry_obj

def Button(strvar, master,button_kwargs = {"text":"Example","command":lambda _: 0}, pack_kwargs={"fill":"x","expand":True},*,pack_or_grid: bool = True, grid_kwargs: list = [{}]):
    '''
    Creates a label with the given kwargs,
    stringvar and master.
    '''
    entry_obj = Personalized_Widget(strvar,master)
    entry_obj.Button(**button_kwargs)
    if not isinstance(pack_or_grid, bool):
        raise TypeError("not_pack must be a bool.")
    elif pack_or_grid == True:
        entry_obj.Pack(pack_kwargs)
    else:
        entry_obj.Grid(*grid_kwargs)
    
    return entry_obj


# Code example with most of this library's functions.
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("300x400")
    root.resizable(False, False)
    root.title('Sample program')
    
    a = tk.StringVar()
    b = tk.StringVar()
    c = tk.StringVar()
    
    func_input1 = EntryWithLabel(a, root,{"text":"Sample 1","width":25,"compound":"left"},{"width":25},{"expand":False},pack_or_grid=True)
    func_input2 = EntryWithLabel(b, root,{"text":"Sample 2","width":25,"compound":"left"},{"width":25},{"expand":False},pack_or_grid=True)
    
    output = Label(c, root, {"text":"The result of mixing samples.","width":25,"compound":"left"},{"expand":False}, pack_or_grid = True)
    output = Label_with_Button(c, root, {"textvariable":c, "width":25, "compound":"left","borderwidth":1,"relief":"solid","background":"white"},{"text":"Mix samples 1 and 2","width":25,"command":lambda:c.set(func_input1.strvar.get() + func_input2.strvar.get())},{"expand":False,"fill":"y"})
    
    root.mainloop()
