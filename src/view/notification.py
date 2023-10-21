from plyer import notification

title = 'Wrong Posture Alert!'
message = 'You are sitting with hunged shoulders.'
appico = 'imgs/sitfixlogo.ico'
notification.notify(
    title=title,
    message=message,
    app_name='Sitfix-ai',
    app_icon=appico
)
class Notification:
    def __init__(self, title, message) -> None:
        self.title = title
        self.message = message
        self.app_name = "Sitfix-ai"
        self.appico = 'imgs/sitfixlogo.ico'
