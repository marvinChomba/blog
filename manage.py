from app import create_app,db
from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand
from app.models import User,Post,Comment

#create app with the desired cnfiguration
app = create_app("development")

manager = Manager(app)

migrate = Migrate(app,db)
manager.add_command("db", MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(db = db, app = app, Post = Post, Comment = Comment,User = User)

if __name__ == "__main__":
    manager.run()