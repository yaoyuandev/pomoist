import rumps
import clipboard
import sync
import vika_api
rumps.debug_mode(True)

x = 0


class AwesomeStatusBarApp(rumps.App):

    @rumps.clicked('🔥 start')
    def start(self, sender):
        global x
        print('start')
        x = 25*60
        win = rumps.Window("hello", ok="fire", cancel="cancel",
                           default_text=clipboard.paste())
        resp = win.run()
        print(resp)
        if resp.clicked:
            url = resp.text
            f = open('data.txt', 'a')
            f.writelines([url, '\n'])
            timer.start()
            f.close()
            sync.sync(url)

    @rumps.clicked('💤 relax')
    def relax(self, _):
        global x
        x = 5 * 60
        timer.start()
        vika_api.insert_relax()

    @rumps.clicked("🛑 stop")
    def stop(self, _):
        timer.stop()
        app.title = 'pomoist'


def tick(sender):
    global x
    print(sender)
    x -= 1
    app.title = time(x)
    if x == 0:
        timer.stop()
        rumps.notification("Awesome title", "amazing subtitle", "done")
        app.title = 'pomoist'


def time(x):
    return f'{x // 60:02d}:{x % 60:02d}'


timer = rumps.Timer(tick, 1)
app = AwesomeStatusBarApp("pomoist")
app.run()
