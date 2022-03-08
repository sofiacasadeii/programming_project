from flask import Flask, render_template, request
from part1 import *
app = Flask(__name__, template_folder='template')


operations = registry.keys()


def myform():
    text = request.form.get('text')
    return text


@app.route('/')
def home_page():
    return render_template('home_page.html', title="Home Page", operations=operations)


@app.route('/Operation', methods=['GET', 'POST'])
def operation():
    my_operation = request.args.get('type')
    if str(my_operation) == 'SentenceGene':
        gene = str(myform())
        if gene != '':
            display = registry[my_operation].input_operation(gene)
            print(display)
            return render_template('operation.html', title=my_operation, operation=my_operation, display=display)
        


    elif operation == '':
        display = '3'
        return render_template('operation.html', title=my_operation, operation=my_operation, display=display)
    else:
        display = registry[str(my_operation)]
        return render_template('operation.html', title=my_operation, operation=my_operation, display=display)


if __name__ == '__main__':
    app.run(debug=True)
