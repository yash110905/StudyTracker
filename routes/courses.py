from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user
from database import db
from models.course import Course

#Initialize the Blueprint for course-related routes
courses = Blueprint("courses", __name__)


@courses.route("/courses")
@login_required
def view_courses():
    """Fetch and display all courses belonging to the logged-in user."""
    
    #Query the database for courses matching the current user's ID(one to many relation here)
    user_courses = Course.query.filter_by(
        user_id=current_user.id
    ).all()

    #Render the dashboard template and pass the user's courses to it
    return render_template(
        "courses.html",
        courses=user_courses
    )


@courses.route("/courses/add", methods=["POST"])
@login_required
def add_course():
    """Handle form submission to create and save a new course."""
    
    # Extract course details from the incoming POST request form data
    name = request.form["name"]
    code = request.form["code"]

    #Instantiate a new Course model linked to the current user
    course = Course(
        name=name,
        code=code,
        user_id=current_user.id
    )

    # Stage and save the new course instance to the database
    db.session.add(course)
    db.session.commit()

    #Redirect the user back to the main courses view
    return redirect("/courses")