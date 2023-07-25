import subprocess
import json
try:
    userData = subprocess.getstatusoutput(f'gh api -H "Accept: application/vnd.github+json" /user')
    user=json.loads(userData[1])
    userName=user['name']
    userLogin=user['login']
    code="adn"

    try:
        subprocess.Popen(f"figlet Congratulations", shell=True)
        print(f'''\n

        {userName} (@{userLogin})

        You have just informed the wizarding world of the greatest
        threat that looms over them, that is, Voldemort. You did the right thing by informing about it to Dumbledore, 
        one of the greatest wizard of all times. He'll help you and the wizarding world in this battle against evil.
        This marks the end of the Terminal Wizard. 
        Keep up the good work!!!
        ''')
        
    except:
        print(f'''

        Congratulations {userName} (@{userLogin}). 

        You have just informed the wizarding world of the greatest
        threat that looms over them, that is, Voldemort. You did the right thing by informing about it to Dumbledore, 
        one of the greatest wizard of all times. He'll help you and the wizarding world in this battle against evil.
        This marks the end of the Terminal Wizard. 
        Keep up the good work!!!

          ____                            _         _       _   _                 
 / ___|___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_(_) ___  _ __  ___ 
| |   / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __|
| |__| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \
 \____\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___/
                  |___/                                                   

        ''')

except Exception as e:
    print("Unkown Error occured, please try again later")