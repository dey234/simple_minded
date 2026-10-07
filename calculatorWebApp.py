
from flask import Flask, request, render_template_string

# Create the Flask app that serves the calculator web page and handles form submissions.
app = Flask(__name__)

# This HTML template defines the calculator's layout, fields, button, and result display.
PAGE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#173b35">
  <title>Simple Minded Calculator</title>
  <style>
    :root {
      color-scheme: light;
      font-family: "Avenir Next", Avenir, "Segoe UI", sans-serif;
      color: #173b35;
      background: #f2f5f0;
    }
    * { box-sizing: border-box; }
    body {
      min-height: 100vh;
      margin: 0;
      padding: 32px 20px;
      display: grid;
      place-items: center;
      background: linear-gradient(135deg, #f2f5f0 0%, #e6efea 100%);
    }
    main {
      width: min(100%, 620px);
      padding: clamp(28px, 7vw, 56px);
      background: #fffefa;
      border: 1px solid #dce6df;
      border-radius: 12px;
      box-shadow: 0 18px 55px #173b3512;
    }
    .eyebrow {
      margin: 0 0 14px;
      color: #b54e36;
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 0.14em;
      text-transform: uppercase;
    }
    h1 {
      margin: 0;
      font-family: Georgia, "Times New Roman", serif;
      font-size: clamp(34px, 8vw, 52px);
      font-weight: 500;
      line-height: 1.05;
    }
    .intro { margin: 12px 0 32px; color: #5c7069; line-height: 1.5; }
    form { display: grid; grid-template-columns: minmax(0, 1fr) 76px minmax(0, 1fr); gap: 12px; }
    label { display: grid; gap: 8px; color: #50655e; font-size: 13px; font-weight: 700; }
    input, select, button {
      min-width: 0;
      min-height: 54px;
      border: 1px solid #cbd9d1;
      border-radius: 6px;
      font: inherit;
    }
    input, select { width: 100%; padding: 0 14px; background: #fff; color: #173b35; }
    input:focus, select:focus, button:focus-visible { outline: 3px solid #e8a07c; outline-offset: 2px; }
    .operator { align-self: end; }
    .operator select { text-align: center; font-size: 21px; font-weight: 700; }
    button {
      grid-column: 1 / -1;
      margin-top: 8px;
      border-color: #173b35;
      background: #173b35;
      color: white;
      font-size: 16px;
      font-weight: 750;
      cursor: pointer;
      transition: background 150ms ease, transform 150ms ease;
    }
    button:hover { background: #24564d; }
    button:active { transform: translateY(1px); }
    .result {
      margin-top: 26px;
      padding: 18px 20px;
      border-left: 4px solid #b54e36;
      background: #f5f1e8;
      overflow-wrap: anywhere;
    }
    .result-label { display: block; margin-bottom: 4px; color: #68746d; font-size: 12px; font-weight: 750; text-transform: uppercase; }
    .result-value { font-family: Georgia, "Times New Roman", serif; font-size: 26px; }
    @media (max-width: 460px) {
      body { padding: 16px; }
      form { grid-template-columns: minmax(0, 1fr) 62px minmax(0, 1fr); gap: 8px; }
      input { padding: 0 10px; }
    }
  </style>
</head>
<body>
  <main>
    <p class="eyebrow">Simple Minded · Everyday arithmetic</p>
    <h1>Simple Minded<br>Calculator</h1>
    <p class="intro">A little math, without the fuss.</p>
    <form method="post">
      <label>First number
        <input type="number" name="num1" value="{{ num1 }}" step="any" inputmode="decimal" placeholder="e.g. 12" required>
      </label>
      <label class="operator">Operation
        <select name="op" aria-label="Operation">
          {% for symbol in ["+", "-", "*", "/"] %}
            <option value="{{ symbol }}" {% if symbol == op %}selected{% endif %}>{{ symbol }}</option>
          {% endfor %}
        </select>
      </label>
      <label>Second number
        <input type="number" name="num2" value="{{ num2 }}" step="any" inputmode="decimal" placeholder="e.g. 3" required>
      </label>
      <button type="submit">Calculate</button>
    </form>
    {% if result != "" %}
      <div class="result" role="status" aria-live="polite">
        <span class="result-label">Result</span>
        <span class="result-value">{{ result }}</span>
      </div>
    {% endif %}
  </main>
</body>
</html>
"""

# Route for the home page: display the form and process the submitted calculation.
@app.route("/", methods=["GET", "POST"])
def index():
    # Keep track of the entered values and the current math symbol for the page display.
    num1 = num2 = result = ""
    op = "+"

    # When the form is submitted, read the values and perform the selected calculation.
    if request.method == "POST":
        num1 = request.form.get("num1", "")
        num2 = request.form.get("num2", "")
        op = request.form.get("op", "+")

        try:
            # Convert the text inputs into numbers so arithmetic can be done safely.
            a = float(num1)
            b = float(num2)

            # Apply the correct operator to the two numbers.
            if op == "+":
                result = a + b
            elif op == "-":
                result = a - b
            elif op == "*":
                result = a * b
            elif op == "/":
                # Prevent division by zero and show a helpful error instead.
                if b == 0:
                    result = "Error: cannot divide by zero"
                else:
                    result = a / b
            else:
                result = "Error: choose a valid operation"
        except ValueError:
            # Tell the user the values entered are not valid numbers.
            result = "Error: enter valid numbers"

    # Render the HTML page again with the entered values and computed result.
    return render_template_string(PAGE, num1=num1, num2=num2, op=op, result=result)

# Run the local web server when this file is executed directly.
if __name__ == "__main__":
    app.run(debug=True, port=5000)