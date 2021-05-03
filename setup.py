import json

def load_configs():
    
    filename = 'settings.json'

    try:
        with open(filename) as f_obj:
            settings = json.load(f_obj)
        
    except FileNotFoundError:
        settings = {}
        settings['username'] = input("Username : ")
        settings['password'] = input("Password : ")
        settings['driver'] = input("""Type in your browser from the list (lower case) : 
        -> firefox
        -> chrome
        -> edge
        -> opera
        -> safari
        """
        )
        settings['nbClasses'] = int(input("Enter your amount of classes this semester : "))

        with open(filename, 'w') as f_obj:
            json.dump(settings, f_obj)
            
    return settings