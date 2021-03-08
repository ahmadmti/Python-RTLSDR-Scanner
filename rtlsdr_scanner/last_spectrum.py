import wx

from rtlsdr_scanner.password_dialog import PASS_OK, PASS_CANCEL, resource_path


class LastSpectrumValueDialog(wx.Dialog):
    def __init__(self, parent,value=-48.3399255981):
        super(LastSpectrumValueDialog, self).__init__(parent, -1, "Last Scan minimum value",)
        panel = wx.Panel(self)
        panel.SetBackgroundColour((0,0,0))
        sizer = wx.BoxSizer(wx.VERTICAL)
        value=round(value,2)
        self.label = wx.StaticText(panel, label=str(value))
        font = wx.Font(72, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        self.label.SetFont(font)
        self.label.SetForegroundColour((255, 255, 255))
        panel.SetSizer(sizer)
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
                self.EndModal(PASS_OK)
            else:
                self.input.SetBackgroundColour ( "Pink" )

    def on_cancel(self,event):
        self.EndModal(event.EventObject.Id)