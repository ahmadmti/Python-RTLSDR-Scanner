import wx

from license.license_verify import hash_license, decrypt, verify_license
from rtlsdr_scanner.password_dialog import resource_path


class LicenseFrame(wx.Frame):
    def __init__(self,onVerify):
        wx.Frame.__init__(self, None, title='SahrpMap License')
        self.onVerify=onVerify
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.license_input_label = wx.StaticText(panel, label="Please Enter Your License")
        sizer.Add(self.license_input_label, 0, wx.ALL | wx.EXPAND, 5)
        self.license_input = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        sizer.Add(self.license_input, 1, wx.ALL | wx.EXPAND)
        license_verify = wx.Button(panel, label='Verify')
        license_verify.Bind(wx.EVT_BUTTON, self.verify)
        sizer.Add(license_verify, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(sizer)
        self.Show()

    def verify(self, event):
        if decrypt(self.license_input.GetValue()):
            data=hash_license(self.license_input.GetValue())
            with open("license.lic", 'wb') as file:
                file.write(data)
            self.onVerify()
            self.Destroy()
        else:
            self.license_input_label.SetLabel("Please enter valid license")

def is_licenced():
    try:
        with open("license.lic", 'rb') as file:
            data=file.read()
            return verify_license(data)
    except Exception as e:
        return False