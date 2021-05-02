from abc import ABCMeta, abstractstaticmethod
import os
from plyer import notification
import subprocess

class INotification(ABCMeta):
    
    @abstractstaticmethod
    def notify(title, text):
        pass

class AppleNotification(INotification):
    
    def notify(title, text):
        os.system("""
              osascript -e 'display notification"{}" with title "{}"'
              """.format(text, title))
        
class WindowsNotification(INotification):
    
    def notify(title, text):
        notification.notify(title=title, message=text, timeout=10)
        
class LinuxNotification(INotification):
    
    def notify(title, text):
        subprocess.Popen([title, text])
        

class NotificationFactory:
    
    @staticmethod
    def create_notification(os, title, text):
        
        try:
            
            if os == 'darwin':
                AppleNotification.notify(title, text)

            elif os == 'win32' or os == 'cygwin':
                WindowsNotification.notify(title, text)
                
            elif os == 'linux':
                LinuxNotification.notify(title, text)
                
            else:
                raise AssertionError("Not a supported OS.")
            
        except AssertionError as _e:
            print(_e)
    
if __name__ == '__main__':
    NotificationFactory.create_notification(os, title, text)