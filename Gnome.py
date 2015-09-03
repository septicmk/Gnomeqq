import pgi
pgi.install_as_gi()
from gi.repository import Notify
from gi.repository import Gtk
import threading

class Not(threading.Thread):
    def __init__(self, who, txt):
        threading.Thread.__init__(self)
        self.who = who
        self.txt = txt

    def run(self):
        self.notify(self.who, self.txt)

    def notify(self, who, txt):
        def quit(notif_object, action_name, users_data):
            notif_object.close()
            Gtk.main_quit()
        Notify.init('QQ_Msg')
        nf = Notify.Notification.new(who, txt, 'dialog-information')
        nf.add_action('quit','quit',quit,None,None)
        nf.show()
        Gtk.main()

class Win(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="login")
        self.box = Gtk.Box(spacing=6)
        self.add(self.box)
        img = Gtk.Image.new_from_file("./v.jpg")
        self.box.pack_start(img, True, True, 0)

class X(threading.Thread):
    def __init__(self, win):
        threading.Thread.__init__(self)
        self.win = win

    def run(self):
        win = self.win        
        win.connect("delete-event", Gtk.main_quit)
        win.show_all()
        Gtk.main() 

