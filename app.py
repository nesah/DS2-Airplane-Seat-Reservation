# Import libraries
from flask import Flask, request, render_template, redirect, flash, url_for, session
import webview
import jinja2
import sys
import os
import threading

#lifesaver line - delete == shit wont work
sys.stdout = sys.stderr = open(os.devnull, 'w')

# Setup jinja
jinja = jinja2.Environment(loader=jinja2.FileSystemLoader("template"))

# Make app
app = Flask(__name__)
debug = False

# Create secret key for flash messages
app.secret_key = "72882373811"

# Flights schedules for flights_layout.html
flights_schedules = [["12 - 15 - 2022", "06:00AM - 07:00AM", "MNL - DAV", "AIRCRAFT - 46284629", "1"], 
                    ["12 - 15 - 2022", "08:00AM - 09:00AM", "MNL - CEB", "AIRCRAFT - 16271989", "2"],
                    ["12 - 15 - 2022", "08:00AM - 09:00AM", "DAV - MNL", "AIRCRAFT - 47629438", "3"],
                    ["12 - 15 - 2022", "08:00AM - 09:00AM", "DAV - CEB", "AIRCRAFT - 84027492", "4"],
                    ["12 - 15 - 2022", "06:00AM - 07:00AM", "CEB - MNL", "AIRCRAFT - 03774662", "5"],
                    ["12 - 15 - 2022", "08:00AM - 09:00AM", "CEB - DAV", "AIRCRAFT - 46027839", "6"]]

# Seats id for flights_layout.html
seat_id =   [   "FIRST-CLASS-A-1", "FIRST-CLASS-A-2", "FIRST-CLASS-A-3", "ECONOMY-CLASS-A-4", "ECONOMY-CLASS-A-5", "ECONOMY-CLASS-A-6", "ECONOMY-CLASS-A-7", "ECONOMY-CLASS-A-8", "ECONOMY-CLASS-A-9", "ECONOMY-CLASS-A-10",
                "FIRST-CLASS-B-1", "FIRST-CLASS-B-2", "FIRST-CLASS-B-3", "ECONOMY-CLASS-B-4", "ECONOMY-CLASS-B-5", "ECONOMY-CLASS-B-6", "ECONOMY-CLASS-B-7", "ECONOMY-CLASS-B-8", "ECONOMY-CLASS-B-9", "ECONOMY-CLASS-B-10",
                "FIRST-CLASS-C-1", "FIRST-CLASS-C-2", "FIRST-CLASS-C-3", "ECONOMY-CLASS-C-4", "ECONOMY-CLASS-C-5", "ECONOMY-CLASS-C-6", "ECONOMY-CLASS-C-7", "ECONOMY-CLASS-C-8", "ECONOMY-CLASS-C-9", "ECONOMY-CLASS-C-10",
                "FIRST-CLASS-D-1", "FIRST-CLASS-D-2", "FIRST-CLASS-D-3", "ECONOMY-CLASS-D-4", "ECONOMY-CLASS-D-5", "ECONOMY-CLASS-D-6", "ECONOMY-CLASS-D-7", "ECONOMY-CLASS-D-8", "ECONOMY-CLASS-D-9", "ECONOMY-CLASS-D-10",
                "FIRST-CLASS-E-1", "FIRST-CLASS-E-2", "FIRST-CLASS-E-3", "ECONOMY-CLASS-E-4", "ECONOMY-CLASS-E-5", "ECONOMY-CLASS-E-6", "ECONOMY-CLASS-E-7", "ECONOMY-CLASS-E-8", "ECONOMY-CLASS-E-9", "ECONOMY-CLASS-E-10",
                "FIRST-CLASS-F-1", "FIRST-CLASS-F-2", "FIRST-CLASS-F-3", "ECONOMY-CLASS-F-4", "ECONOMY-CLASS-F-5", "ECONOMY-CLASS-F-6", "ECONOMY-CLASS-F-7", "ECONOMY-CLASS-F-8", "ECONOMY-CLASS-F-9", "ECONOMY-CLASS-F-10"
            ]

# Seats list for seats_layout.html
a = [   "FIRST-CLASS-A-1", "FIRST-CLASS-A-2", "FIRST-CLASS-A-3", "FIRST-CLASS-B-1", "FIRST-CLASS-B-2", "FIRST-CLASS-B-3", "FIRST-CLASS-C-1", "FIRST-CLASS-C-2", "FIRST-CLASS-C-3",
        "FIRST-CLASS-D-1", "FIRST-CLASS-D-2", "FIRST-CLASS-D-3", "FIRST-CLASS-E-1", "FIRST-CLASS-E-2", "FIRST-CLASS-E-3", "FIRST-CLASS-F-1", "FIRST-CLASS-F-2", "FIRST-CLASS-F-3",         
        "ECONOMY-CLASS-A-4", "ECONOMY-CLASS-A-5", "ECONOMY-CLASS-A-6", "ECONOMY-CLASS-A-7", "ECONOMY-CLASS-A-8", "ECONOMY-CLASS-A-9", "ECONOMY-CLASS-A-10",
        "ECONOMY-CLASS-B-4", "ECONOMY-CLASS-B-5", "ECONOMY-CLASS-B-6", "ECONOMY-CLASS-B-7", "ECONOMY-CLASS-B-8", "ECONOMY-CLASS-B-9", "ECONOMY-CLASS-B-10",
        "ECONOMY-CLASS-C-4", "ECONOMY-CLASS-C-5", "ECONOMY-CLASS-C-6", "ECONOMY-CLASS-C-7", "ECONOMY-CLASS-C-8", "ECONOMY-CLASS-C-9", "ECONOMY-CLASS-C-10",
        "ECONOMY-CLASS-D-4", "ECONOMY-CLASS-D-5", "ECONOMY-CLASS-D-6", "ECONOMY-CLASS-D-7", "ECONOMY-CLASS-D-8", "ECONOMY-CLASS-D-9", "ECONOMY-CLASS-D-10",
        "ECONOMY-CLASS-E-4", "ECONOMY-CLASS-E-5", "ECONOMY-CLASS-E-6", "ECONOMY-CLASS-E-7", "ECONOMY-CLASS-E-8", "ECONOMY-CLASS-E-9", "ECONOMY-CLASS-E-10",
        "ECONOMY-CLASS-F-4", "ECONOMY-CLASS-F-5", "ECONOMY-CLASS-F-6", "ECONOMY-CLASS-F-7", "ECONOMY-CLASS-F-8", "ECONOMY-CLASS-F-9", "ECONOMY-CLASS-F-10",
    ]
b = [   "FIRST-CLASS-A-1", "FIRST-CLASS-A-2", "FIRST-CLASS-A-3", "FIRST-CLASS-B-1", "FIRST-CLASS-B-2", "FIRST-CLASS-B-3", "FIRST-CLASS-C-1", "FIRST-CLASS-C-2", "FIRST-CLASS-C-3",
        "FIRST-CLASS-D-1", "FIRST-CLASS-D-2", "FIRST-CLASS-D-3", "FIRST-CLASS-E-1", "FIRST-CLASS-E-2", "FIRST-CLASS-E-3", "FIRST-CLASS-F-1", "FIRST-CLASS-F-2", "FIRST-CLASS-F-3",         
        "ECONOMY-CLASS-A-4", "ECONOMY-CLASS-A-5", "ECONOMY-CLASS-A-6", "ECONOMY-CLASS-A-7", "ECONOMY-CLASS-A-8", "ECONOMY-CLASS-A-9", "ECONOMY-CLASS-A-10",
        "ECONOMY-CLASS-B-4", "ECONOMY-CLASS-B-5", "ECONOMY-CLASS-B-6", "ECONOMY-CLASS-B-7", "ECONOMY-CLASS-B-8", "ECONOMY-CLASS-B-9", "ECONOMY-CLASS-B-10",
        "ECONOMY-CLASS-C-4", "ECONOMY-CLASS-C-5", "ECONOMY-CLASS-C-6", "ECONOMY-CLASS-C-7", "ECONOMY-CLASS-C-8", "ECONOMY-CLASS-C-9", "ECONOMY-CLASS-C-10",
        "ECONOMY-CLASS-D-4", "ECONOMY-CLASS-D-5", "ECONOMY-CLASS-D-6", "ECONOMY-CLASS-D-7", "ECONOMY-CLASS-D-8", "ECONOMY-CLASS-D-9", "ECONOMY-CLASS-D-10",
        "ECONOMY-CLASS-E-4", "ECONOMY-CLASS-E-5", "ECONOMY-CLASS-E-6", "ECONOMY-CLASS-E-7", "ECONOMY-CLASS-E-8", "ECONOMY-CLASS-E-9", "ECONOMY-CLASS-E-10",
        "ECONOMY-CLASS-F-4", "ECONOMY-CLASS-F-5", "ECONOMY-CLASS-F-6", "ECONOMY-CLASS-F-7", "ECONOMY-CLASS-F-8", "ECONOMY-CLASS-F-9", "ECONOMY-CLASS-F-10",
    ]
c = [   "FIRST-CLASS-A-1", "FIRST-CLASS-A-2", "FIRST-CLASS-A-3", "FIRST-CLASS-B-1", "FIRST-CLASS-B-2", "FIRST-CLASS-B-3", "FIRST-CLASS-C-1", "FIRST-CLASS-C-2", "FIRST-CLASS-C-3",
        "FIRST-CLASS-D-1", "FIRST-CLASS-D-2", "FIRST-CLASS-D-3", "FIRST-CLASS-E-1", "FIRST-CLASS-E-2", "FIRST-CLASS-E-3", "FIRST-CLASS-F-1", "FIRST-CLASS-F-2", "FIRST-CLASS-F-3",         
        "ECONOMY-CLASS-A-4", "ECONOMY-CLASS-A-5", "ECONOMY-CLASS-A-6", "ECONOMY-CLASS-A-7", "ECONOMY-CLASS-A-8", "ECONOMY-CLASS-A-9", "ECONOMY-CLASS-A-10",
        "ECONOMY-CLASS-B-4", "ECONOMY-CLASS-B-5", "ECONOMY-CLASS-B-6", "ECONOMY-CLASS-B-7", "ECONOMY-CLASS-B-8", "ECONOMY-CLASS-B-9", "ECONOMY-CLASS-B-10",
        "ECONOMY-CLASS-C-4", "ECONOMY-CLASS-C-5", "ECONOMY-CLASS-C-6", "ECONOMY-CLASS-C-7", "ECONOMY-CLASS-C-8", "ECONOMY-CLASS-C-9", "ECONOMY-CLASS-C-10",
        "ECONOMY-CLASS-D-4", "ECONOMY-CLASS-D-5", "ECONOMY-CLASS-D-6", "ECONOMY-CLASS-D-7", "ECONOMY-CLASS-D-8", "ECONOMY-CLASS-D-9", "ECONOMY-CLASS-D-10",
        "ECONOMY-CLASS-E-4", "ECONOMY-CLASS-E-5", "ECONOMY-CLASS-E-6", "ECONOMY-CLASS-E-7", "ECONOMY-CLASS-E-8", "ECONOMY-CLASS-E-9", "ECONOMY-CLASS-E-10",
        "ECONOMY-CLASS-F-4", "ECONOMY-CLASS-F-5", "ECONOMY-CLASS-F-6", "ECONOMY-CLASS-F-7", "ECONOMY-CLASS-F-8", "ECONOMY-CLASS-F-9", "ECONOMY-CLASS-F-10",
    ]
d = [   "FIRST-CLASS-A-1", "FIRST-CLASS-A-2", "FIRST-CLASS-A-3", "FIRST-CLASS-B-1", "FIRST-CLASS-B-2", "FIRST-CLASS-B-3", "FIRST-CLASS-C-1", "FIRST-CLASS-C-2", "FIRST-CLASS-C-3",
        "FIRST-CLASS-D-1", "FIRST-CLASS-D-2", "FIRST-CLASS-D-3", "FIRST-CLASS-E-1", "FIRST-CLASS-E-2", "FIRST-CLASS-E-3", "FIRST-CLASS-F-1", "FIRST-CLASS-F-2", "FIRST-CLASS-F-3",         
        "ECONOMY-CLASS-A-4", "ECONOMY-CLASS-A-5", "ECONOMY-CLASS-A-6", "ECONOMY-CLASS-A-7", "ECONOMY-CLASS-A-8", "ECONOMY-CLASS-A-9", "ECONOMY-CLASS-A-10",
        "ECONOMY-CLASS-B-4", "ECONOMY-CLASS-B-5", "ECONOMY-CLASS-B-6", "ECONOMY-CLASS-B-7", "ECONOMY-CLASS-B-8", "ECONOMY-CLASS-B-9", "ECONOMY-CLASS-B-10",
        "ECONOMY-CLASS-C-4", "ECONOMY-CLASS-C-5", "ECONOMY-CLASS-C-6", "ECONOMY-CLASS-C-7", "ECONOMY-CLASS-C-8", "ECONOMY-CLASS-C-9", "ECONOMY-CLASS-C-10",
        "ECONOMY-CLASS-D-4", "ECONOMY-CLASS-D-5", "ECONOMY-CLASS-D-6", "ECONOMY-CLASS-D-7", "ECONOMY-CLASS-D-8", "ECONOMY-CLASS-D-9", "ECONOMY-CLASS-D-10",
        "ECONOMY-CLASS-E-4", "ECONOMY-CLASS-E-5", "ECONOMY-CLASS-E-6", "ECONOMY-CLASS-E-7", "ECONOMY-CLASS-E-8", "ECONOMY-CLASS-E-9", "ECONOMY-CLASS-E-10",
        "ECONOMY-CLASS-F-4", "ECONOMY-CLASS-F-5", "ECONOMY-CLASS-F-6", "ECONOMY-CLASS-F-7", "ECONOMY-CLASS-F-8", "ECONOMY-CLASS-F-9", "ECONOMY-CLASS-F-10",
    ]
e = [   "FIRST-CLASS-A-1", "FIRST-CLASS-A-2", "FIRST-CLASS-A-3", "FIRST-CLASS-B-1", "FIRST-CLASS-B-2", "FIRST-CLASS-B-3", "FIRST-CLASS-C-1", "FIRST-CLASS-C-2", "FIRST-CLASS-C-3",
        "FIRST-CLASS-D-1", "FIRST-CLASS-D-2", "FIRST-CLASS-D-3", "FIRST-CLASS-E-1", "FIRST-CLASS-E-2", "FIRST-CLASS-E-3", "FIRST-CLASS-F-1", "FIRST-CLASS-F-2", "FIRST-CLASS-F-3",         
        "ECONOMY-CLASS-A-4", "ECONOMY-CLASS-A-5", "ECONOMY-CLASS-A-6", "ECONOMY-CLASS-A-7", "ECONOMY-CLASS-A-8", "ECONOMY-CLASS-A-9", "ECONOMY-CLASS-A-10",
        "ECONOMY-CLASS-B-4", "ECONOMY-CLASS-B-5", "ECONOMY-CLASS-B-6", "ECONOMY-CLASS-B-7", "ECONOMY-CLASS-B-8", "ECONOMY-CLASS-B-9", "ECONOMY-CLASS-B-10",
        "ECONOMY-CLASS-C-4", "ECONOMY-CLASS-C-5", "ECONOMY-CLASS-C-6", "ECONOMY-CLASS-C-7", "ECONOMY-CLASS-C-8", "ECONOMY-CLASS-C-9", "ECONOMY-CLASS-C-10",
        "ECONOMY-CLASS-D-4", "ECONOMY-CLASS-D-5", "ECONOMY-CLASS-D-6", "ECONOMY-CLASS-D-7", "ECONOMY-CLASS-D-8", "ECONOMY-CLASS-D-9", "ECONOMY-CLASS-D-10",
        "ECONOMY-CLASS-E-4", "ECONOMY-CLASS-E-5", "ECONOMY-CLASS-E-6", "ECONOMY-CLASS-E-7", "ECONOMY-CLASS-E-8", "ECONOMY-CLASS-E-9", "ECONOMY-CLASS-E-10",
        "ECONOMY-CLASS-F-4", "ECONOMY-CLASS-F-5", "ECONOMY-CLASS-F-6", "ECONOMY-CLASS-F-7", "ECONOMY-CLASS-F-8", "ECONOMY-CLASS-F-9", "ECONOMY-CLASS-F-10",
    ]
f = [   "FIRST-CLASS-A-1", "FIRST-CLASS-A-2", "FIRST-CLASS-A-3", "FIRST-CLASS-B-1", "FIRST-CLASS-B-2", "FIRST-CLASS-B-3", "FIRST-CLASS-C-1", "FIRST-CLASS-C-2", "FIRST-CLASS-C-3",
        "FIRST-CLASS-D-1", "FIRST-CLASS-D-2", "FIRST-CLASS-D-3", "FIRST-CLASS-E-1", "FIRST-CLASS-E-2", "FIRST-CLASS-E-3", "FIRST-CLASS-F-1", "FIRST-CLASS-F-2", "FIRST-CLASS-F-3",         
        "ECONOMY-CLASS-A-4", "ECONOMY-CLASS-A-5", "ECONOMY-CLASS-A-6", "ECONOMY-CLASS-A-7", "ECONOMY-CLASS-A-8", "ECONOMY-CLASS-A-9", "ECONOMY-CLASS-A-10",
        "ECONOMY-CLASS-B-4", "ECONOMY-CLASS-B-5", "ECONOMY-CLASS-B-6", "ECONOMY-CLASS-B-7", "ECONOMY-CLASS-B-8", "ECONOMY-CLASS-B-9", "ECONOMY-CLASS-B-10",
        "ECONOMY-CLASS-C-4", "ECONOMY-CLASS-C-5", "ECONOMY-CLASS-C-6", "ECONOMY-CLASS-C-7", "ECONOMY-CLASS-C-8", "ECONOMY-CLASS-C-9", "ECONOMY-CLASS-C-10",
        "ECONOMY-CLASS-D-4", "ECONOMY-CLASS-D-5", "ECONOMY-CLASS-D-6", "ECONOMY-CLASS-D-7", "ECONOMY-CLASS-D-8", "ECONOMY-CLASS-D-9", "ECONOMY-CLASS-D-10",
        "ECONOMY-CLASS-E-4", "ECONOMY-CLASS-E-5", "ECONOMY-CLASS-E-6", "ECONOMY-CLASS-E-7", "ECONOMY-CLASS-E-8", "ECONOMY-CLASS-E-9", "ECONOMY-CLASS-E-10",
        "ECONOMY-CLASS-F-4", "ECONOMY-CLASS-F-5", "ECONOMY-CLASS-F-6", "ECONOMY-CLASS-F-7", "ECONOMY-CLASS-F-8", "ECONOMY-CLASS-F-9", "ECONOMY-CLASS-F-10",
    ]

# Route for flights_layout.html
@app.route("/", methods=["GET", "POST"])
def index():

    # If button is clicked
    if request.method == "POST":

        # Get selected flight
        sel = request.form.get("flight_list")

        # Redirect to seats page
        return redirect(url_for("seats", sel=sel))

    # Render page and send flights schedules list, seat ids, and seats per flight
    return render_template("flights_layout.html", flights_schedules=flights_schedules, seat_id=seat_id, a=a, b=b, c=c, d=d, e=e, f=f)

def start_server():
    app.run(host='0.0.0.0', port=80)

# Route for seats_layout.html
@app.route("/seats", methods=["GET", "POST"])
def seats():

    # Get selected flight
    sel = int(request.args.get("sel", None))

    # If button is clicked
    if request.method == "POST":

        # Get selected seat
        choosen = str(request.form.get("seat_choosen"))

        # Get typed input
        last_name = str(request.form.get("lname_text"))
        first_name = str(request.form.get("fname_text"))
        middle_name = str(request.form.get("mname_text"))
        cont_num = str(request.form.get("contact_text"))
        email_add = str(request.form.get("email_text"))

        # Remove white spaces
        last_name = last_name.strip(' ')
        first_name = first_name.strip(' ')
        middle_name = middle_name.strip(' ')
        cont_num = cont_num.strip(' ')
        email_add = email_add.strip(' ')

        # Check if input is correct
        if not last_name:
            flash("Last name cannot be blank!")
        elif not first_name:
            flash("First name cannot be blank!")
        elif not middle_name:
            flash("Middle name cannot be blank!")
        elif not cont_num:
            flash("Contact number cannot be blank!")
        elif not cont_num.isnumeric():
            flash("Contact number is not numeric!")
        elif not email_add:
            flash("Email address cannot be blank!")
        elif not '@' in email_add:
            flash("Invalid email!")
        
        # Input is correct
        else: 

            # Remove selected seat
            if sel == 1:
                a.remove(choosen)
            if sel == 2:
                b.remove(choosen)           
            if sel == 3:
                c.remove(choosen)           
            if sel == 4:
                d.remove(choosen)         
            if sel == 5:
                e.remove(choosen)
            if sel == 6:
                f.remove(choosen)

            # Redirect to flights_layout.html
            return redirect("/")

    # Send seat list depending on flight schedule selected
    if sel == 1:
        seats_list = a   
    if sel == 2:
        seats_list = b
    if sel == 3:
        seats_list = c  
    if sel == 4:
        seats_list = d
    if sel == 5:
        seats_list = e
    if sel == 6:
        seats_list = f

    # Get flight schedule details
    flig_sche = ""
    for fli in flights_schedules[int(sel)-1]:
        flig_sche = flig_sche + " " + fli

    # Remove last element in details
    flig_sche = flig_sche[0:-1]

    # Render page and send seat list and flight schedule details
    return render_template("seats_layout.html", seats_list=seats_list, flig_sche=flig_sche)


#makes the app run only in main even if run anywhere else
if __name__ == '__main__':

    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()

    webview.create_window("EVERECO", "http://localhost/")
    webview.start()
    sys.exit()
