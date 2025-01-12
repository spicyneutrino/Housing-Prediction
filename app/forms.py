from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    area = StringField("House Area")
    area = StringField("House Area")
    bedrooms = StringField("Number of Bedrooms")
    bathrooms = StringField("Number of Bathrooms")
    stories = StringField("Number of Stories")
    parking = StringField("Parking Spaces")
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
    )
    submit = SubmitField('Predict')

    # num__area', 'cat_ordinal__bedrooms', 'cat_ordinal__bathrooms',
    #    'cat_ordinal__stories', 'cat_ordinal__parking',
    #    'cat_onehot__mainroad_yes', 'cat_onehot__guestroom_yes',
    #    'cat_onehot__basement_yes', 'cat_onehot__hotwaterheating_yes',
    #    'cat_onehot__airconditioning_yes', 'cat_onehot__prefarea_yes',
    #    'cat_onehot__furnishingstatus_semi-furnished',
    #    'cat_onehot__furnishingstatus_unfurnished'],
