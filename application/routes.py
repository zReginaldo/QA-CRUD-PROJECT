from application import app, db, bcrypt
from flask import render_template, redirect, url_for, request, jsonify
from application.forms import PostForm, RegistrationForm, LoginForm, UpdateAccountForm, LeaguesForm
from application.models import *
from flask_login import login_user, current_user, logout_user, login_required



@app.route('/home')
def home():
        postData = Posts.query.all()
        return render_template('home.html', title='Home', posts=postData)

@app.route('/')
@app.route('/about', methods=['GET', 'POST']) 
@login_required
def about():
    form = LeaguesForm()
    form.club.choices = [(club.id,club.club_name) for club in Players.query.filter_by(league_name='').all()]
    form.players.choices = [( players.id, players.name) for players in Players.query.filter_by(club_name='').all()]
    
    if request.method == "POST":
        players = Players.query.filter_by(id=form.players.data).first() 
        club = Club.query.filter_by(id=form.club.data).first()
        return '<h1>Your Choice: {}</h1>'.format(players.name)
    
    return render_template('about.html', form=form)
    

@app.route('/clubs/<league_name>')
def clubs(league_name):

    teams = Players.query.filter_by(league_name=league_name).all()
    
    
    clubArray = []

    for club in teams: 
        clubObj = {}
        clubObj['id'] = club.id
        clubObj['name'] = club.club_name
        clubArray.append(clubObj)
    
    return jsonify({'teams' : clubArray})

@app.route('/players/<id>')
def players(id):
    Player_nm = Players.query.filter_by(id=id).all()
    PlayArray = []
    
    for players in Player_nm:
        playObj = {}
        playObj['id'] = players.id
        playObj['name'] = players.name
        PlayArray.append(playObj)
        
    return jsonify({'Player_nm' : PlayArray})


@app.route('/register', methods=['GET', 'POST'])
def register():
        if current_user.is_authenticated:
                return redirect(url_for('home'))
        form = RegistrationForm()
        if form.validate_on_submit():
                hash_pw = bcrypt.generate_password_hash(form.password.data)
                user = Users(
                        first_name=form.first_name.data,
                        last_name=form.last_name.data,
                        email=form.email.data,
                        password=hash_pw
                        )

                db.session.add(user)
                db.session.commit()

                return redirect(url_for('post'))

        return render_template('register.html', title='Register', form=form)

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
        if current_user.is_authenticated:
                return redirect(url_for('home'))
        form = LoginForm()
        if form.validate_on_submit():
                user = Users.query.filter_by(email=form.email.data).first()
                if user and bcrypt.check_password_hash(user.password, form.password.data):
                        login_user(user, remember=form.remember.data)
                        next_page = request.args.get('next')
                        if next_page:
                                return redirect(next_page)
                        else:
                                return redirect('home')
        return render_template('login.html', title='Login', form=form)

@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
        form = PostForm()
        if form.validate_on_submit():
                postData = Posts(
                        title=form.title.data,
                        content=form.content.data,
                        author=current_user
                )
                db.session.add(postData)
                db.session.commit()
                return redirect(url_for('home'))

        else:
                print(form.errors)
        return render_template('post.html', title='Post', form=form)

@app.route('/logout')
@login_required
def logout():
        logout_user()
        return redirect(url_for('login'))

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)


@app.route("/account/delete", methods=["GET", "POST"])
@login_required
def account_delete():
    user = current_user.id
    deletePost = Posts.query.filter_by(user_id=user).all()
    account = Users.query.filter_by(id=user).first()
    logout_user()
    db.session.delete(account)
    for i in deletePost:
        db.session.delete(i)
    db.session.commit()
    return redirect(url_for('register'))
