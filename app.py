import rumps
import clipboard
rumps.debug_mode(True)

x = 0


class AwesomeStatusBarApp(rumps.App):
    @rumps.clicked("stop")
    def stop(self, _):
        timer.stop()

    @rumps.clicked("start")
    def start(self, sender):
        global x
        print('start')
        x = 25*60
        win = rumps.Window("hello", ok="fire", cancel="cancel",
                           default_text=clipboard.paste())
        resp = win.run()
        print(resp)
        if resp.clicked:
            print(resp.text)
            f = open('data.txt', 'a')
            f.writelines([resp.text, '\n'])
            timer.start()
            f.close()


def show(sender):
    global x
    print(sender)
    x -= 1
    app.title = time(x)
    if x == 0:
        timer.stop()
        rumps.notification("Awesome title", "amazing subtitle", "done")
        app.title = 'pomoist'


def time(x):
    return f'{x // 60}:{x % 60}'


timer = rumps.Timer(show, 1)
app = AwesomeStatusBarApp("pomoist")
app.run()
