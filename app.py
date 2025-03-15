from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/run", methods=["POST"])
def run_command():
    command = request.form.get("command")
    output = os.popen(command).read()  # ❌ Command Injection Vulnerability
    return f"<pre>{output}</pre>"

@app.route("/eval", methods=["POST"])
def eval_code():
    code = request.form.get("code")
    result = eval(code)  # ❌ Remote Code Execution (RCE)
    return str(result)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8000)
