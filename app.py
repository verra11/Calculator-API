from flask import Flask, render_template, request

app = Flask(__name__)

def add(a, b):
	return float(a) + float(b)

def sub(a, b):
	return float(a) - float(b)

def mul(a, b):
	return float(a) * float(b)

def div(a, b):
	return float(a) / float(b)

def pow(a, b):
	return a ** b

def gcd(a, b):
	if a == 0:
		return b
	return gcd(b%a, a)

def lcm(a, b):
	return (a*b) / gcd(a,b)

def OR(a, b):
	return int(a) | int(b)

def AND(a, b):
	return int(a) & int(b)

def XOR(a, b):
	return int(a) ^ int(b)


@app.route("/", methods=["POST", "GET"])
def home():
	return render_template("index.html")

@app.route("/submit", methods=["POST", "GET"])
def submit():

	val = 0

	if request.method == "POST":

		num1 = float(request.form['num1'])
		num2 = float(request.form['num2'])
		op = request.form['operation']

		if op == 'add':
			val = add(num1, num2)
		elif op == 'sub':
			val = sub(num1, num2)
		elif op == 'mul':
			val = mul(num1, num2)
		elif op == 'div':
			val = div(num1, num2)
		elif op == 'pow':
			val = pow(num1, num2)
		elif op == 'gcd':
			val = gcd(num1, num2)
		elif op == 'lcm':
			val = lcm(num1, num2)
		elif op == 'or':
			val = OR(num1, num2)
		elif op == 'and':
			val = AND(num1, num2)
		elif op == 'xor':
			val = XOR(num1, num2)

	return render_template("index.html", num1=num1, num2=num2, op=op, val=val)	

if __name__ == "__main__":
	app.run(debug=True)