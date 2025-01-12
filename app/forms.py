from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    area = StringField("House Area", validators=[DataRequired()])
    bedrooms = StringField("Number of Bedrooms", validators=[DataRequired()])
    bathrooms = StringField("Number of Bathrooms", validators=[DataRequired()])
    stories = StringField("Number of Stories", validators=[DataRequired()])
    parking = StringField("Parking Spaces", validators=[DataRequired()])
    mainroad = BooleanField("Main Road Access")
    guestroom = BooleanField("Guestroom Available")
    basement = BooleanField("Basement Available")
    hotwaterheating = BooleanField("Hot Water Heating Available")
    airconditioning = BooleanField("Air Conditioning Available")
    prefarea = BooleanField("Preferred Area")
    furnishing_status = RadioField(
        "Furnishing Status",
        choices=[
            ("furnished", "Furnished"),
            ("semi-furnished", "Semi-Furnished"),
            ("unfurnished", "Unfurnished"),
        ],
        default="unfurnished",
        validators=[DataRequired()],
    )
    submit = SubmitField("Predict")

#     X.columns
# Index(['area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom',
#        'basement', 'hotwaterheating', 'airconditioning', 'parking', 'prefarea',
#        'furnishingstatus'],
#       dtype='object')
