import subprocess
import time
import sys

proc = subprocess.Popen(
    ['C:\\Program Files\\LOVE\\love.exe', '.\\slave'],
    stdout=subprocess.PIPE,
    stdin=subprocess.PIPE,
    shell=True
    )

inp, err = proc.communicate(input='111'.encode("ASCII"))