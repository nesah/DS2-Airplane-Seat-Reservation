# Import libraries
from flask import Flask, request, render_template, redirect, flash, url_for, session
import jinja2

# Setup jinja
jinja = jinja2.Environment(loader=jinja2.FileSystemLoader("template"))

# Make app
app = Flask(__name__)

# Create secret key for flash messages
app.secret_key = "72882373811"

# Flights schedules for flights_layout.html
flights_schedules = [["12 - 15 - 2022", "06:00AM - 07:00AM", "MNL - DAV", "AIRCRAFT - 46284629", "1"], 
                    ["12 - 15 - 2022", "08:00AM - 09:00AM", "MNL - CEB", "AIRCRAFT - 16271989", "2"],
                    ["12 - 15 - 2022", "08:00AM - 09:00AM", "DAV - MNL", "AIRCRAFT - 47629438", "3"],
                    ["12 - 15 - 2022", "08:00AM - 09:00AM", "DAV - CEB", "AIRCRAFT - 84027492", "4"],
                    ["12 - 15 - 2022", "06:00AM - 07:00AM", "CEB - MNL", "AIRCRAFT - 03774662", "5"],
                    ["12 - 15 - 2022", "08:00AM - 09:00AM", "CEB - DAV", "AIRCRAFT - 46027839", "6"]]

# Seats list for seats_layout.html
a = [   "FIRST CLASS A 1", "FIRST CLASS A 2", "FIRST CLASS A 3", "FIRST CLASS B 1", "FIRST CLASS B 2", "FIRST CLASS B 3", "FIRST CLASS C 1", "FIRST CLASS C 2", "FIRST CLASS C 3",
        "FIRST CLASS D 1", "FIRST CLASS D 2", "FIRST CLASS D 3", "FIRST CLASS E 1", "FIRST CLASS E 2", "FIRST CLASS E 3", "FIRST CLASS F 1", "FIRST CLASS F 2", "FIRST CLASS F 3",         
        "ECONOMY CLASS A 4", "ECONOMY CLASS A 5", "ECONOMY CLASS A 6", "ECONOMY CLASS A 7", "ECONOMY CLASS A 8", "ECONOMY CLASS A 9", "ECONOMY CLASS A 10",
        "ECONOMY CLASS B 4", "ECONOMY CLASS B 5", "ECONOMY CLASS B 6", "ECONOMY CLASS B 7", "ECONOMY CLASS B 8", "ECONOMY CLASS B 9", "ECONOMY CLASS B 10",
        "ECONOMY CLASS C 4", "ECONOMY CLASS C 5", "ECONOMY CLASS C 6", "ECONOMY CLASS C 7", "ECONOMY CLASS C 8", "ECONOMY CLASS C 9", "ECONOMY CLASS C 10",
        "ECONOMY CLASS D 4", "ECONOMY CLASS D 5", "ECONOMY CLASS D 6", "ECONOMY CLASS D 7", "ECONOMY CLASS D 8", "ECONOMY CLASS D 9", "ECONOMY CLASS D 10",
        "ECONOMY CLASS E 4", "ECONOMY CLASS E 5", "ECONOMY CLASS E 6", "ECONOMY CLASS E 7", "ECONOMY CLASS E 8", "ECONOMY CLASS E 9", "ECONOMY CLASS E 10",
        "ECONOMY CLASS F 4", "ECONOMY CLASS F 5", "ECONOMY CLASS F 6", "ECONOMY CLASS F 7", "ECONOMY CLASS F 8", "ECONOMY CLASS F 9", "ECONOMY CLASS F 10",
    ]
b = [   "FIRST CLASS A 1", "FIRST CLASS A 2", "FIRST CLASS A 3", "FIRST CLASS B 1", "FIRST CLASS B 2", "FIRST CLASS B 3", "FIRST CLASS C 1", "FIRST CLASS C 2", "FIRST CLASS C 3",
        "FIRST CLASS D 1", "FIRST CLASS D 2", "FIRST CLASS D 3", "FIRST CLASS E 1", "FIRST CLASS E 2", "FIRST CLASS E 3", "FIRST CLASS F 1", "FIRST CLASS F 2", "FIRST CLASS F 3",         
        "ECONOMY CLASS A 4", "ECONOMY CLASS A 5", "ECONOMY CLASS A 6", "ECONOMY CLASS A 7", "ECONOMY CLASS A 8", "ECONOMY CLASS A 9", "ECONOMY CLASS A 10",
        "ECONOMY CLASS B 4", "ECONOMY CLASS B 5", "ECONOMY CLASS B 6", "ECONOMY CLASS B 7", "ECONOMY CLASS B 8", "ECONOMY CLASS B 9", "ECONOMY CLASS B 10",
        "ECONOMY CLASS C 4", "ECONOMY CLASS C 5", "ECONOMY CLASS C 6", "ECONOMY CLASS C 7", "ECONOMY CLASS C 8", "ECONOMY CLASS C 9", "ECONOMY CLASS C 10",
        "ECONOMY CLASS D 4", "ECONOMY CLASS D 5", "ECONOMY CLASS D 6", "ECONOMY CLASS D 7", "ECONOMY CLASS D 8", "ECONOMY CLASS D 9", "ECONOMY CLASS D 10",
        "ECONOMY CLASS E 4", "ECONOMY CLASS E 5", "ECONOMY CLASS E 6", "ECONOMY CLASS E 7", "ECONOMY CLASS E 8", "ECONOMY CLASS E 9", "ECONOMY CLASS E 10",
        "ECONOMY CLASS F 4", "ECONOMY CLASS F 5", "ECONOMY CLASS F 6", "ECONOMY CLASS F 7", "ECONOMY CLASS F 8", "ECONOMY CLASS F 9", "ECONOMY CLASS F 10",
    ]
c = [   "FIRST CLASS A 1", "FIRST CLASS A 2", "FIRST CLASS A 3", "FIRST CLASS B 1", "FIRST CLASS B 2", "FIRST CLASS B 3", "FIRST CLASS C 1", "FIRST CLASS C 2", "FIRST CLASS C 3",
        "FIRST CLASS D 1", "FIRST CLASS D 2", "FIRST CLASS D 3", "FIRST CLASS E 1", "FIRST CLASS E 2", "FIRST CLASS E 3", "FIRST CLASS F 1", "FIRST CLASS F 2", "FIRST CLASS F 3",         
        "ECONOMY CLASS A 4", "ECONOMY CLASS A 5", "ECONOMY CLASS A 6", "ECONOMY CLASS A 7", "ECONOMY CLASS A 8", "ECONOMY CLASS A 9", "ECONOMY CLASS A 10",
        "ECONOMY CLASS B 4", "ECONOMY CLASS B 5", "ECONOMY CLASS B 6", "ECONOMY CLASS B 7", "ECONOMY CLASS B 8", "ECONOMY CLASS B 9", "ECONOMY CLASS B 10",
        "ECONOMY CLASS C 4", "ECONOMY CLASS C 5", "ECONOMY CLASS C 6", "ECONOMY CLASS C 7", "ECONOMY CLASS C 8", "ECONOMY CLASS C 9", "ECONOMY CLASS C 10",
        "ECONOMY CLASS D 4", "ECONOMY CLASS D 5", "ECONOMY CLASS D 6", "ECONOMY CLASS D 7", "ECONOMY CLASS D 8", "ECONOMY CLASS D 9", "ECONOMY CLASS D 10",
        "ECONOMY CLASS E 4", "ECONOMY CLASS E 5", "ECONOMY CLASS E 6", "ECONOMY CLASS E 7", "ECONOMY CLASS E 8", "ECONOMY CLASS E 9", "ECONOMY CLASS E 10",
        "ECONOMY CLASS F 4", "ECONOMY CLASS F 5", "ECONOMY CLASS F 6", "ECONOMY CLASS F 7", "ECONOMY CLASS F 8", "ECONOMY CLASS F 9", "ECONOMY CLASS F 10",
    ]
d = [   "FIRST CLASS A 1", "FIRST CLASS A 2", "FIRST CLASS A 3", "FIRST CLASS B 1", "FIRST CLASS B 2", "FIRST CLASS B 3", "FIRST CLASS C 1", "FIRST CLASS C 2", "FIRST CLASS C 3",
        "FIRST CLASS D 1", "FIRST CLASS D 2", "FIRST CLASS D 3", "FIRST CLASS E 1", "FIRST CLASS E 2", "FIRST CLASS E 3", "FIRST CLASS F 1", "FIRST CLASS F 2", "FIRST CLASS F 3",         
        "ECONOMY CLASS A 4", "ECONOMY CLASS A 5", "ECONOMY CLASS A 6", "ECONOMY CLASS A 7", "ECONOMY CLASS A 8", "ECONOMY CLASS A 9", "ECONOMY CLASS A 10",
        "ECONOMY CLASS B 4", "ECONOMY CLASS B 5", "ECONOMY CLASS B 6", "ECONOMY CLASS B 7", "ECONOMY CLASS B 8", "ECONOMY CLASS B 9", "ECONOMY CLASS B 10",
        "ECONOMY CLASS C 4", "ECONOMY CLASS C 5", "ECONOMY CLASS C 6", "ECONOMY CLASS C 7", "ECONOMY CLASS C 8", "ECONOMY CLASS C 9", "ECONOMY CLASS C 10",
        "ECONOMY CLASS D 4", "ECONOMY CLASS D 5", "ECONOMY CLASS D 6", "ECONOMY CLASS D 7", "ECONOMY CLASS D 8", "ECONOMY CLASS D 9", "ECONOMY CLASS D 10",
        "ECONOMY CLASS E 4", "ECONOMY CLASS E 5", "ECONOMY CLASS E 6", "ECONOMY CLASS E 7", "ECONOMY CLASS E 8", "ECONOMY CLASS E 9", "ECONOMY CLASS E 10",
        "ECONOMY CLASS F 4", "ECONOMY CLASS F 5", "ECONOMY CLASS F 6", "ECONOMY CLASS F 7", "ECONOMY CLASS F 8", "ECONOMY CLASS F 9", "ECONOMY CLASS F 10",
    ]
e = [   "FIRST CLASS A 1", "FIRST CLASS A 2", "FIRST CLASS A 3", "FIRST CLASS B 1", "FIRST CLASS B 2", "FIRST CLASS B 3", "FIRST CLASS C 1", "FIRST CLASS C 2", "FIRST CLASS C 3",
        "FIRST CLASS D 1", "FIRST CLASS D 2", "FIRST CLASS D 3", "FIRST CLASS E 1", "FIRST CLASS E 2", "FIRST CLASS E 3", "FIRST CLASS F 1", "FIRST CLASS F 2", "FIRST CLASS F 3",         
        "ECONOMY CLASS A 4", "ECONOMY CLASS A 5", "ECONOMY CLASS A 6", "ECONOMY CLASS A 7", "ECONOMY CLASS A 8", "ECONOMY CLASS A 9", "ECONOMY CLASS A 10",
        "ECONOMY CLASS B 4", "ECONOMY CLASS B 5", "ECONOMY CLASS B 6", "ECONOMY CLASS B 7", "ECONOMY CLASS B 8", "ECONOMY CLASS B 9", "ECONOMY CLASS B 10",
        "ECONOMY CLASS C 4", "ECONOMY CLASS C 5", "ECONOMY CLASS C 6", "ECONOMY CLASS C 7", "ECONOMY CLASS C 8", "ECONOMY CLASS C 9", "ECONOMY CLASS C 10",
        "ECONOMY CLASS D 4", "ECONOMY CLASS D 5", "ECONOMY CLASS D 6", "ECONOMY CLASS D 7", "ECONOMY CLASS D 8", "ECONOMY CLASS D 9", "ECONOMY CLASS D 10",
        "ECONOMY CLASS E 4", "ECONOMY CLASS E 5", "ECONOMY CLASS E 6", "ECONOMY CLASS E 7", "ECONOMY CLASS E 8", "ECONOMY CLASS E 9", "ECONOMY CLASS E 10",
        "ECONOMY CLASS F 4", "ECONOMY CLASS F 5", "ECONOMY CLASS F 6", "ECONOMY CLASS F 7", "ECONOMY CLASS F 8", "ECONOMY CLASS F 9", "ECONOMY CLASS F 10",
    ]
f = [   "FIRST CLASS A 1", "FIRST CLASS A 2", "FIRST CLASS A 3", "FIRST CLASS B 1", "FIRST CLASS B 2", "FIRST CLASS B 3", "FIRST CLASS C 1", "FIRST CLASS C 2", "FIRST CLASS C 3",
        "FIRST CLASS D 1", "FIRST CLASS D 2", "FIRST CLASS D 3", "FIRST CLASS E 1", "FIRST CLASS E 2", "FIRST CLASS E 3", "FIRST CLASS F 1", "FIRST CLASS F 2", "FIRST CLASS F 3",         
        "ECONOMY CLASS A 4", "ECONOMY CLASS A 5", "ECONOMY CLASS A 6", "ECONOMY CLASS A 7", "ECONOMY CLASS A 8", "ECONOMY CLASS A 9", "ECONOMY CLASS A 10",
        "ECONOMY CLASS B 4", "ECONOMY CLASS B 5", "ECONOMY CLASS B 6", "ECONOMY CLASS B 7", "ECONOMY CLASS B 8", "ECONOMY CLASS B 9", "ECONOMY CLASS B 10",
        "ECONOMY CLASS C 4", "ECONOMY CLASS C 5", "ECONOMY CLASS C 6", "ECONOMY CLASS C 7", "ECONOMY CLASS C 8", "ECONOMY CLASS C 9", "ECONOMY CLASS C 10",
        "ECONOMY CLASS D 4", "ECONOMY CLASS D 5", "ECONOMY CLASS D 6", "ECONOMY CLASS D 7", "ECONOMY CLASS D 8", "ECONOMY CLASS D 9", "ECONOMY CLASS D 10",
        "ECONOMY CLASS E 4", "ECONOMY CLASS E 5", "ECONOMY CLASS E 6", "ECONOMY CLASS E 7", "ECONOMY CLASS E 8", "ECONOMY CLASS E 9", "ECONOMY CLASS E 10",
        "ECONOMY CLASS F 4", "ECONOMY CLASS F 5", "ECONOMY CLASS F 6", "ECONOMY CLASS F 7", "ECONOMY CLASS F 8", "ECONOMY CLASS F 9", "ECONOMY CLASS F 10",
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

    # Render page and send flights schedules list
    return render_template("flights_layout.html", flights_schedules=flights_schedules)

# Route for seats_layout.html
@app.route("/seats", methods=["GET", "POST"])
def seats():

    # Get selected flight
    sel = int(request.args.get("sel", None))

    # If button is clicked
    if request.method == "POST":

        # Get selected seat
        choosen = str(request.form.get("seat_choosen"))

        # CODE HERE
        # GET ALL TYPED INPUT FROM seats_layout.html AND CHECK IF INPUT IS BLANK OR TOO SHORT
        # IF INPUT IS BLANK OR TOO SHORT (ADD MORE CONSTAINTS) DISPLAY FLASH
        # TO DISPLAY FLASH, INSERT THIS CODE flash("Details cannot be blank!") (CHANGE TEXT FOR OTHER ERRORS)
        # AS LONG AS THERE IS PROBLEM FROM INPUT PREVENT CODE FROM EXECUTING LINE 113 - 131

        last_name = str(request.form.get("lname_text"))
        first_name = str(request.form.get("fname_text"))
        middle_name = str(request.form.get("mname_text"))
        cont_num = str(request.form.get("contact_text"))
        email_add = str(request.form.get("email_text"))
        
        # Checking text fields
        #check = 1
        #while(check == 1):
        if bool(last_name) != False:

            if bool(first_name) != False:
                
                if bool(middle_name) != False:

                    if bool(cont_num) != False:

                        if cont_num.isnumeric() == True:

                            if bool(email_add) != False:

                                if "@" in email_add:

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

                                    return redirect("/")
                                
                                else:
                                    flash("Please enter the correct details")

                            else:
                                flash("Details cannot be blank!")

                        else:
                            flash("Please enter the correct details")

                    else:
                        flash("Details cannot be blank!")

                else:
                    flash("Details cannot be blank!")

            else:
                flash("Details cannot be blank!")

        else:
            flash("Details cannot be blank!")

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
    for f in flights_schedules[int(sel)-1]:
        flig_sche = flig_sche + " " + f

    # Remove last element in details
    flig_sche = flig_sche[0:-1]

    # Render page and send seat list
    return render_template("seats_layout.html", seats_list=seats_list, flig_sche=flig_sche)
