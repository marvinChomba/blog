from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class AddPostForm(FlaskForm):
    title = StringField("Title", validators = [Required()])
    content = TextAreaField("Post", validators = [Required()])
    submit = SubmitField("Add Post")