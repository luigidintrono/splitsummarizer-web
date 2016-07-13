from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired

class SummarizorForm(Form):
    article_text = StringField(u'Text',
                            validators=[DataRequired()],
                            widget=TextArea())
