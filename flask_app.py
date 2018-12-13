from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")
#They user input asks for name/ blizzard battlenet
#They then choose the roll they would like to play
#They then are asked for their favorite character
#They then enter their rank they currently are
#after all this is enterned functions determine what tips suit the user best
@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    name = request.form.get('input_name', '')
    role = request.form.get('input_role', '')
    select = request.form.get('input_select', '')
    freeform = request.form.get('input_freeform', '')
    if name is "":
        return render_template("main_page.html", input_data=role,
                           output="We would like to know your name%s." % name)
    return render_template("main_page.html",input_data=role,
                            name = name,
                            role = role)


