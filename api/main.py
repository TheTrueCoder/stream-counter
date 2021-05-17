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

def changeval(change_val):
    with open(value_path, "r+") as f:
        try:
            x = int(f.read())
        except:
            x = 0
        y = int(change_val)
        result = x+y

        if result < 0:
            result = 0

        f.seek(0)
        f.write(str(result))
        f.truncate()

        return (result)

@app.route("/increase")
def increase():
    return str(changeval(1))

@app.route("/decrease")
def decrease():
    return str(changeval(-1))

# print(changeval(1))