from flask import Flask, render_template, request
app = Flask(__name__)

import repo

@app.route("/menu/delete", methods=['POST','GET'])
def menu_delete():
    if (request.method == 'POST'):
          repo.delete_menu(request.form.get('dishes'))
          return "Record deleted"
    return render_template("menuform.html")

@app.route("/menu/update", methods=['POST','GET'])
def menu_update():
    if (request.method == 'POST'):
          repo.update_menu(request.form.get('dishes'),request.form.get('ratings'))
          return "Record Updated"
    return render_template("menuform.html")
    
@app.route("/menu/create",methods=['POST','GET'])
def menu_create():
    if(request.method == 'POST'):
        repo.create_menu(request.form.get('dishes'), request.form.get('ratings'))
        return "New record created"
    return render_template("menuform.html")

@app.route("/menu/read")
def menu_read():
        return render_template("menu.html",menulist=repo.read_menu())

@app.route("/")
def default():
        return render_template("pageOne.html")

#The following functions not used yet
"""
@app.route("/dashboard")
def dashboard_view():
        return render_template("dashboard.html")

@app.route("/product/<id>")
def get_product(id):
        return "product ID = %s" % id

@app.route("/product")
def product_view():
        return "This is product page"
"""

       

if __name__ == "__main__":
    app.run()
