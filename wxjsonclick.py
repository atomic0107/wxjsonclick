'''
Created on 2018/08/11
refer to URL
https://torina.top/detail/43/
https://wxpython.org/Phoenix/docs/html/wx.MouseEvent.html?highlight=dclick#wx.MouseEvent.Aux1DClick
http://wxwindowsjp.osdn.jp/docs/html/wx/wx411.htm
http://maku77.github.io/python/wxpython/textctrl.html
http://wxwindowsjp.osdn.jp/docs/html/wx/wx381.htm
https://wxpython.org/Phoenix/docs/html/wx.KeyEvent.html
https://www.blog.pythonlibrary.org/2009/08/29/wxpython-catching-key-and-char-events/
text events
http://wxwindowsjp.osdn.jp/docs/html/wx/wx381.htm
@author: atomic
'''
import json
import wx
##############################################
#            global variable
##############################################
rec_side = 50       #四角の辺の大きさ
bd_width = 500     #フレームの横幅
bd_height = 500    #フレームの縦幅
center_x = bd_width/2
center_y = bd_height/2
clr = "black"       #背景の色
tclr = 'black'       #テキストの色
prime_cnt = 50
f = open('data.json', 'r')
#f = open('data_w.json', 'w')
jsonData = json.load(f)
f.close
print (json.dumps(jsonData, sort_keys = True, indent = 4))
#dict = json.load(json_t)
#"""
dict = {
    "関数":None,
    "定義":None,
    "構造体":None,
    "列挙隊":None,
    "テーブル":None
}
#"""
ret_text = "None"
TEXTBOX_CNT = 0
TEXTBOX_ENABLE = 1
TEXTBOX_DISABLE = 0

class mind():
    #コンストラクタ
    cur_len = 0
    cur_x = center_x
    cur_y = center_y
    tab_flag = False
    del_editbox = None#delete editbox
    callSkip = None
    #constractor
    def __init__(self,panel):
        self.textobj_list = []
        self.textbox_list = []
        self.textbox_cnt = 0
        self.x = mind.cur_x
        self.y = mind.cur_y
        self.dict_list = list(dict.keys())
        mind.panel = panel
        mind.cur_len = len(self.dict_list)
        for text_cnt in range(mind.cur_len):
            mind.cur_y = center_y + text_cnt * 25
            self.textobj = wx.StaticText(mind.panel, wx.ID_ANY, self.dict_list[text_cnt],pos = (mind.cur_x,mind.cur_y))
            self.textobj.SetForegroundColour(tclr)
            #self.textobj.Bind(wx.EVT_LEFT_DOWN, self.click)
            self.textobj.Bind(wx.EVT_LEFT_DCLICK, self.double_click)
            self.textobj_list.append(self.textobj)

    def key_event(self,event):
        self.keycode = event.GetKeyCode()
        print("press key")
        print(self.keycode)
        #event.GetSkipped()
        if self.keycode == wx.WXK_TAB:
            print("tab")
            self.y += 25
            self.textbox = wx.TextCtrl(mind.panel, -1, pos = (self.x,self.y),style = wx.TE_PROCESS_ENTER )
            self.textbox.Bind(wx.EVT_TEXT_ENTER, self.OnTabText)
            self.textbox_list.append(self.textbox)
            self.textbox_cnt += 1
        print(" self.textbox_cnt = " + str(self.textbox_cnt))
        print(" len(self.textbox_list) = " + str(len(self.textbox_list)))

    def OnTabText(self, event):
        self.box = event.GetEventObject()
        input_text = self.box.GetValue()
        self.box.Destroy()
        self.textbox_cnt -= 1
        print(input_text)
        #if int(dict.setdefault(input_text,None)) > len(self.dict_list)):
        textobj = wx.StaticText(mind.panel, wx.ID_ANY, input_text,pos = (self.x,self.y))
        textobj.SetForegroundColour(tclr)
        textobj.Bind(wx.EVT_LEFT_DOWN, self.tabclick)
        textobj.Bind(wx.EVT_LEFT_DCLICK, self.tabdouble_click)
        dict.setdefault( input_text , None )
        self.write_dict(dict)
        print(dict)

    def tabclick(self, event):
        if self.textbox_cnt > TEXTBOX_DISABLE:
            print(self.textbox_cnt)
            self.textbox_list[self.textbox_cnt-1].Destroy()
            del self.textbox_list[self.textbox_cnt-1]
            print("#textbox_delete")
            self.textbox_cnt -= 1
        click = event.GetEventObject()  # クリックされたのはどのオブジェクトか
        click_text = click.GetLabel()  # そのオブジェクトのラベルを取得
        ret_text = click_text
        print(ret_text)

    def tabdouble_click(self, event):
        self.click = event.GetEventObject()  # クリックされたのはどのオブジェクトか
        click_text = self.click.GetLabel()  # そのオブジェクトのラベルを取得
        ret_text = click_text
        print(ret_text)
        #self.textbox = wx.TextCtrl(self.panel, -1, click_text, pos = self.click.GetPosition(),style = wx.TE_PROCESS_ENTER )
        self.textbox = wx.TextCtrl(mind.panel, -1, click_text, pos = self.click.GetPosition(),style = wx.TE_LEFT )
        self.textbox.Bind(wx.EVT_TEXT_ENTER, self.OnText)
        self.textbox_list.append(self.textbox)
        self.textbox_cnt += 1
        print(" self.textbox_cnt = " + str(self.textbox_cnt))
        print(" len(self.textbox_list) = " + str(len(self.textbox_list)))

    def click(self, event):
        if self.textbox_cnt > TEXTBOX_DISABLE :
            print(self.textbox_cnt)
            self.textbox_list[self.textbox_cnt-1].Destroy()
            del self.textbox_list[self.textbox_cnt-1]
            print("#textbox_delete")
            self.textbox_cnt -= 1
        click = event.GetEventObject()  # クリックされたのはどのオブジェクトか
        click_text = click.GetLabel()  # そのオブジェクトのラベルを取得
        ret_text = click_text
        print(ret_text)

    def double_click(self, event):
        self.click = event.GetEventObject()  # クリックされたのはどのオブジェクトか
        click_text = self.click.GetLabel()  # そのオブジェクトのラベルを取得
        ret_text = click_text
        print(ret_text)
        self.textbox = wx.TextCtrl(mind.panel, -1, click_text, pos = self.click.GetPosition(),style = wx.TE_PROCESS_ENTER )
        self.textbox.SelectAll()
        self.textbox.SetFocus()
        print(self.textbox.GetSelection())
        self.textbox.Bind(wx.EVT_TEXT_ENTER, self.OnText)
        self.textbox_list.append(self.textbox)
        self.textbox_cnt += 1
        print(" self.textbox_cnt = " + str(self.textbox_cnt))
        print(" len(self.textbox_list) = " + str(len(self.textbox_list)))

    def OnText(self, event):
        self.ontextobj = event.GetEventObject()
        #self.textbox.SelectAll()
        input_text =self.textbox.GetValue()
        #self.textbox.SetValue(input_text)
        if self.textbox_cnt > TEXTBOX_DISABLE:
            print(self.textbox_cnt)
            self.textbox_list[self.textbox_cnt-1].Destroy()
            del self.textbox_list[self.textbox_cnt-1]
            print("#textbox_delete")
            self.textbox_cnt -= 1
        print(input_text)
        #self.click.SetLabel(input_text)

    def del_txtbox(self):
        print(" self.textbox_cnt = " + str(self.textbox_cnt))
        print(" len(self.textbox_list) = " + str(len(self.textbox_list)))

    @classmethod
    def entry_label(cls):
        cls.cur_y = center_y + cls.cur_len * 25
        cls.tab_flag = 0
        editbox = wx.TextCtrl(mind.panel, -1, pos = (cls.cur_x,cls.cur_y),style = wx.TE_PROCESS_ENTER )
        editbox.SetFocus()
        cls.del_editbox = editbox
        cls.tab_flag = True#set tab pressed
        editbox.Bind(wx.EVT_TEXT_ENTER, cls.write_label )

    @classmethod
    def write_label(cls,event):
        editbox = event.GetEventObject()
        input_text = editbox.GetValue()
        editbox.Destroy()
        write_flag = dict.setdefault(input_text,None)
        print(dict.setdefault(input_text,None))
        if write_flag == None:
            Static = wx.StaticText(cls.panel, -1, input_text, pos = (cls.cur_x,cls.cur_y))
            Static.SetForegroundColour(tclr)
            cls.tab_flag = False#set tab unpressed
            cls.cur_len += 1#inclease text objct
        else:
            print("dict is not available")
        print(dict)

    @classmethod
    def cls_leave(cls,event):
        editbox = event.GetEventObject()
        editbox.Destroy()
        cls.tab_flag = False#set tab unpressed

    @classmethod
    def cls_delete(cls,event):
        editbox = event.GetEventObject()
        editbox.Destroy()
        cls.tab_flag = False#set tab unpressed

#class Main(wx.Frame):
class Main():
    #def __init__(self, parent, id, title):
    def __init__(self):
        #wx.Frame.__init__(self, parent, id, title)
        frame = wx.Frame(None,title="mindnet")
        frame.SetClientSize(bd_width,bd_height)
        #panel = wx.Panel(frame)
        frame.Bind(wx.EVT_LEFT_DOWN, self.click_ev)
        mind(frame)
        frame.Show(True)

    def click_ev(self,event):
        panel = event.GetEventObject()
        panel.Bind(wx.EVT_CHAR_HOOK, self.key_event)#WIN OK
        #panel.Bind(wx.EVT_KEY_DOWN, self.key_event)#MAC OK
        if mind.tab_flag == True:
            print("delete editbox")
            mind.del_editbox.Destroy()
            mind.tab_flag  = False#set tab unpressed
        else:
            print("no editbox")

    def key_event(self,event):
        self.keycode = event.GetKeyCode()
        
        # 後続のキーイベントをスキップする
        mind.callSkip = True

        if self.keycode == wx.WXK_TAB:
            print("press TAB")
            if mind.tab_flag == False:#tab dont pressed case
                print("create editbox")
                mind.entry_label()
            else:
                print("cant create editbox")

        elif self.keycode == wx.WXK_ESCAPE:
            print("press ESC")
            if mind.tab_flag == True:
                print("delete editbox")
                mind.del_editbox.Destroy()
                mind.tab_flag = False#set tab unpressed
            else:
                print("no editbox")
        else:
            print("other key down")
            event.Skip()
            

def main():
    app = wx.App()
    Main()
    app.MainLoop()

if __name__ == "__main__":
    main()
