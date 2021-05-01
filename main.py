from jnius import autoclass
from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):

    def build(self):
        def _on_click(btn):
            btn.disabled = True

            service = autoclass("org.test.myapp.ServiceService")
            mActivity = autoclass("org.kivy.android.PythonActivity").mActivity
            argument = ""
            service.start(mActivity, argument)

        return Button(text='Start foreground service',
                      on_release=_on_click)


if __name__ == '__main__':
    MyApp().run()
