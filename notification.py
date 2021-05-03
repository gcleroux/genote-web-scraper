from plyer import notification
from sys import platform
import os

def notify(initialGrades, updatedGrades):
    
    for key in updatedGrades.keys():
                
                if initialGrades[key] != updatedGrades[key]:
                    
                    if platform != 'darwin':
                        notification.notify(title="New grade in " + key, message="Good luck!", timeout=10)
                        
                    else:
                        # Plyer is broken on MacOS, so I'm using an applescript instead for the moment
                        os.system("""osascript -e 'display notification"{}" with title "{}"'
                                  """.format("Good luck!", "New grade in " + key))
