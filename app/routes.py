# Exemple complet dans app/routes.py

from flask import render_template, url_for, flash, redirect, request
from app import app, db
from app.models import Car
from app.forms import CarForm

@app.route('/car/<int:car_id>/edit', methods=['GET', 'POST'])
def edit_car(car_id):
    car = Car.query.get_or_404(car_id)
    form = CarForm()
    if form.validate_on_submit():
        car.make = form.make.data
        car.model = form.model.data
        car.year = form.year.data
        car.price = form.price.data
        car.description = form.description.data
        car.image = form.image.data
        db.session.commit()
        flash('Car has been updated!', 'success')
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.make.data = car.make
        form.model.data = car.model
        form.year.data = car.year
        form.price.data = car.price
        form.description.data = car.description
        form.image.data = car.image
    return render_template('edit_car.html', title='Edit Car', form=form)

@app.route('/car/<int:car_id>/delete', methods=['POST'])
def delete_car(car_id):
    car = Car.query.get_or_404(car_id)
    db.session.delete(car)
    db.session.commit()
    flash('Car has been deleted!', 'success')
    return redirect(url_for('index'))
