from flask import Flask

app = Flask(__name__)
value_name = "kmsrun.txt"

def changeval(change_val):
    with open(value_name, "r+") as f:
        try:
            x = int(f.read())
        except:
            x = 0
        y = int(change_val)
        result = x+y

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