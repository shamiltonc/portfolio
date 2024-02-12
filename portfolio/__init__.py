from flask import Flask, render_template, abort

def create_app():
    app = Flask(__name__)

    projects = [
        {
            "name": "CSS Resume",
            "thumb": "img/CSSresume-thumb.png",
            "hero": "img/CSSresume-hero.PNG",       
            "categories": ["css", "html"],
            "slug": "css-resume",
            "prod": "https://shamiltonc.github.io/cssResume/",
        },
        {
            "name": "OC Gallery",
            "thumb": "img/ocGallery-thumb.png",
            "hero": "img/ocGallery-hero.PNG",
            "categories": ["css", "html", "javascript"],
            "slug": "oc-gallery",
            "prod": "https://shamiltonc.github.io/ocGallery/",
        },
        {
            "name": "@methejax on Rufflr",
            "thumb": "img/methejax-thumb.png",
            "hero": "img/methejax-hero.PNG",
            "categories": ["css", "html"],
            "slug": "methejax",
            "prod": "https://shamiltonc.github.io/methejax/",
        },
        {
            "name": "Python To-Do",
            "thumb": "img/PythonToDo-thumb.png",
            "hero": "img/PythonToDo-hero.png",
            "categories": ["python"],
            "slug": "python-todo",
            "prod": "https://github.com/shamiltonc/python-todo",
        },
        {
            "name": "Echo Micro: Flask Microblog",
            "thumb": "img/echomicro-thumb.png",
            "hero": "img/echomicro_hero.PNG",
            "categories": ["python", "css", "html", "flask"],
            "slug": "echo-micro",
            "prod": "https://echo-micro.onrender.com",
        },
        {
            "name": "Flask Habit Tracker",
            "thumb": "img/habitTracker-thumb.png",
            "hero": "img/habitTracker-hero.PNG",        
            "categories": ["python", "css", "html", "flask"],
            "slug": "habit-tracker",
            "prod": "https://habittracker-z7k1.onrender.com/",
        },
    ]

    slug_to_project = {project["slug"]: project for project in projects}

    @app.route("/")
    def home():
        return render_template("home.html", projects=projects)

    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/contact")
    def contact():
        return render_template("/contact.html")

    @app.route("/project/<string:slug>")
    def project(slug):
        if slug not in slug_to_project:
            abort(404)
        return render_template(
            f"project_{slug}.html", 
            project=slug_to_project[slug]
        )

    return app