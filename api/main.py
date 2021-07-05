from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

vals_folder = "values"
value_name = "kmsrun.txt"
value_path = f"{vals_folder}/{value_name}"

f = open(value_path, "w")
f.close()
del(f)

def writefile(path, val):
    with open(path, "w+") as f:
        f.seek(0)
        f.truncate()
        f.write(str(val))

def readfile(path):
    with open(path, "r") as f:
        return f.read

def changeval(change_val):
    og_val = readfile(value_path)
    try:
        x = int(og_val)
    except:
        x = 0
    
    y = int(change_val)
    result = x+y
    if result < 0:
        result = 0
    
    writefile(value_path, result)
    return result

@app.route("/increase")
def increase():
    return str(changeval(1))

@app.route("/decrease")
def decrease():
    return str(changeval(-1))
