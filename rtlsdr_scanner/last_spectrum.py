import wx
from win32crypt import CryptUnprotectData, CryptProtectData

from rtlsdr_scanner.password_dialog import PASS_OK, PASS_CANCEL, resource_path

def save_mod():
    data=CryptProtectData("pass")
    with open("rf.mod", 'wb') as file:
        file.write(data)

def verify_mod(data):
    try:
        if data:
            data = CryptUnprotectData(data)
            if data[1]=='pass':
                return True
            else:
                return False
        else:
            return False
    except Exception as e:
        return False


def is_allow_df_mod():
    try:
        with open("rf.mod", 'rb') as file:
            data=file.read()
            return verify_mod(data)
    except Exception as e:
        return False

class LastSpectrumValueDialog(wx.Frame):
    def __init__(self, parent=None,value=-48.3399255981,onClosed=None):
        wx.Frame.__init__(self,parent, title="Last Scan maximum value",)
        panel = wx.Panel(self)
        panel.SetBackgroundColour((0,0,0))
        horizontal_sizer = wx.BoxSizer(wx.HORIZONTAL)
        vertical_sizer = wx.BoxSizer(wx.VERTICAL)
        value = round(value, 2)
        self.label = wx.StaticText(panel, label=str(value))
        font = wx.Font(72, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        self.label.SetFont(font)
        self.label.SetForegroundColour((255, 255, 255))
        horizontal_sizer.Add(self.label, 0, wx.CENTER)

        vertical_sizer.Add((0, 0), 1, wx.EXPAND)
        vertical_sizer.Add(horizontal_sizer, 0, wx.CENTER)
        vertical_sizer.Add((0, 0), 1, wx.EXPAND)

        panel.SetSizer(vertical_sizer)
        self.Bind(wx.EVT_CLOSE, onClosed)
        self.Show()

class LastSpectrumValuePasswordDialog(wx.Dialog):
    def __init__(self, parent,):
        style = wx.DEFAULT_DIALOG_STYLE
        super(LastSpectrumValuePasswordDialog, self).__init__(parent, -1, "last scan password", style=style)
        text = wx.StaticText(self, -1, "Please enter password for last scan")
        input = wx.TextCtrl(self, -1, style=wx.PASSWORD)
        button_cancel = wx.Button(self, PASS_OK, label='Ok')
        button_cancel.Bind(wx.EVT_BUTTON, self.on_ok)

        button_ok = wx.Button(self, PASS_CANCEL, label='Cancel')
        button_ok.Bind(wx.EVT_BUTTON, self.on_cancel)
        sizer = wx.BoxSizer(wx.VERTICAL)
        row_sizer=wx.BoxSizer(wx.HORIZONTAL)
        row_sizer.Add(button_ok,0,wx.EXPAND|wx.ALL, 5)
        row_sizer.Add(button_cancel, 0, wx.EXPAND|wx.ALL, 5)
        sizer.Add(text, 0, wx.ALL, 5)
        sizer.Add(input, 0, wx.EXPAND, 1)
        sizer.Add(row_sizer,0,wx.EXPAND,5)
        self.SetSizerAndFit(sizer)
        self.input = input
    def SetValue(self, value):
        self.input.SetValue(value)

    def on_ok(self,event):
        with open(resource_path("res/LastSpectrumValuePasswordDialog.txt")) as file:
            password = file.read().strip()
            if self.input.GetValue() == password:
                save_mod()
                self.EndModal(PASS_OK)
            else:
                self.input.SetBackgroundColour ( "Pink" )

    def on_cancel(self,event):
        self.EndModal(event.EventObject.Id)