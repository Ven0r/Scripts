''' 
Finds all the : in a file and grabs 
 the words before and after the colon. 
'''

with open("scada_defaults.txt", "r") as f:
    data = f.read()
    lines = data.split("\n")
    users = []
    passwords = []
    for line in lines:
        try:
            substrings = line.split(':')
            if len(substrings) > 1:
                users.append(substrings[0].split()[-1])
                passwords.append(substrings[1].split()[0])
        except IndexError:
            pass
        with open("scada_default_users.txt", "w") as f:
            f.writelines(user + "\n" for user in users)
        with open("scada_default_pass.txt", "w") as f:
            f.writelines(password + "\n" for password in passwords)



