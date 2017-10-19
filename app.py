from flask import Flask, render_template, url_for, session, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired, ValidationError

from gallows import gallow_pic

from string import ascii_lowercase
from hangman import choose_word, wordlist, get_available_letters, is_word_guessed, get_guessed_word


app = Flask(__name__)
bootstrap = Bootstrap(app)

app.secret_key = 'Somehardtopredictstring'


# def alpha_check(form, field):
#     if not field.data.isalpha():
#         raise ValidationError('Guesses can only be letters')
#
#
# class Guess(FlaskForm):
#     guess = StringField('Please guess a letter', validators=[alpha_check, DataRequired(message='You have to guess a letter'), Length(max=1, message='Please only guess one letter')])
#     submit = SubmitField('Guess')


@app.route('/', methods=['GET', 'POST'])
def hangman():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)