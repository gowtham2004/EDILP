import subprocess

# First script
script1 = f"python vedio.py"
process1 = subprocess.Popen(script1, stdout=subprocess.PIPE)

# Second script
script2 = f"python EDILP.py"
process2 = subprocess.Popen(script2, stdout=subprocess.PIPE)
