from flask import Flask, jsonify, request, render_template, redirect

app = Flask(__name__)
expenses = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/expense', methods=['POST'])
def add_expense():
    description = request.form['description']
    amount = request.form['amount']
    expenses.append({"description": description, "amount": amount})
    return redirect('/expenses')

@app.route('/expenses', methods=['GET'])
def get_all_expenses():
    sort_by = request.args.get("sort_by")
    if sort_by == "amount":
        expenses.sort(key=lambda x: x["amount"])
    return jsonify(expenses)

@app.route('/expense/<int:expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
    expenses.pop(expense_id)
    return jsonify({"message": "Wydatek został usunięty"})

if __name__ == '__main__':
    app.run(debug=True)
