from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class AddPostForm(FlaskForm):
    title = StringField("Title", validators = [Required(s)])
    content = TextAreaField("Post", validators = [Required(s)])
    submit = SubmitField("Add Post")