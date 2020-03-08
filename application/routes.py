from application import app, db, bcrypt
from flask import render_template, redirect, url_for, request, jsonify
from application.forms import PostForm, RegistrationForm, LoginForm, UpdateAccountForm, LeaguesForm
from application.models import *
from flask_login import login_user, current_user, logout_user, login_required



@app.route('/home',methods=['GET', 'POST'])
def home():
    form=LeaguesForm()
    User_Id = current_user.id
    PlayerFilter = UserTeam.query.filter(UserTeam.id == User_Id).first()
    teamDisp = UserTeam.query.filter(UserTeam.id == User_Id).all()
    
    if form.validate_on_submit():
        players = Players.query.filter_by(id=form.players.data).first()
        players1 = Players.query.filter_by(id=form.players1.data).first()
        players2 = Players.query.filter_by(id=form.players2.data).first()
        players3 = Players.query.filter_by(id=form.players3.data).first()            
        players4 = Players.query.filter_by(id=form.players4.data).first()
        club = Club.query.filter_by(id=form.club.data).first()
        
        User_Id = current_user.id
        NewTeam = UserTeam(
                id=User_Id,
                player_1= format(players.name),
                player_2= format(players1.name),
                player_3= format(players2.name),
                player_4= format(players3.name),
                player_5= format(players4.name))
        
        db.session.add(NewTeam)
        db.session.commit()
        db.session.delete(PlayerFilter)
        db.session.commit()

    
    return render_template('home.html', teamDisp=teamDisp, form=form)


@app.route('/')
@app.route('/about', methods=['GET', 'POST']) 
@login_required
def about():

    form = LeaguesForm()
    form.club.choices = [(club.id,club.club_name) for club in Players.query.filter_by(league_name='').all()]
    form.players.choices = [( players.id, players.name) for players in Players.query.filter_by(club_name='').all()]
    
    form.club1.choices = [(club1.id,club1.club_name) for club1 in Players.query.filter_by(league_name='England Premier League').all()]
    form.players1.choices = [( players1.id, players1.name) for players1 in Players.query.filter_by(club_name='Arsenal').all()]
    
    form.club2.choices = [(club2.id,club2.club_name) for club2 in Players.query.filter_by(league_name='England Premier League').all()]
    form.players2.choices = [( players2.id, players2.name) for players2 in Players.query.filter_by(club_name='Arsenal').all()]

    form.club3.choices = [(club3.id,club3.club_name) for club3 in Players.query.filter_by(league_name='England Premier League').all()]
    form.players3.choices = [( players3.id, players3.name) for players3 in Players.query.filter_by(club_name='Arsenal').all()]
    
    form.club4.choices = [(club4.id,club4.club_name) for club4 in Players.query.filter_by(league_name='England Premier League').all()]
    form.players4.choices = [( players4.id, players4.name) for players4 in Players.query.filter_by(club_name='Arsenal').all()]
    
    
    User_Id = current_user.id
    PlayerFilter = UserTeam.query.filter(UserTeam.id == User_Id).first()
    teamDisp = UserTeam.query.filter(UserTeam.id == User_Id).all()
    
    if request.method =="POST":
        
        players = Players.query.filter_by(id=form.players.data).first() 
        players1 = Players.query.filter_by(id=form.players1.data).first()
        players2 = Players.query.filter_by(id=form.players2.data).first()
        players3 = Players.query.filter_by(id=form.players3.data).first()
        players4 = Players.query.filter_by(id=form.players4.data).first()
        club = Club.query.filter_by(id=form.club.data).first()
        
        User_Id = current_user.id
        NewTeam = UserTeam(
                id=User_Id,
                player_1= format(players.name), 
                player_2= format(players1.name), 
                player_3= format(players2.name), 
                player_4= format(players3.name), 
                player_5= format(players4.name))
        
        db.session.add(NewTeam)
        db.session.commit()
        db.session.delete(PlayerFilter)
        db.session.commit()
        
        return redirect(url_for('home'))   
   


    return render_template('about.html', teamDisp=teamDisp, form=form)
    

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


@app.route('/clubs1/<league_name>')
def clubs1(league_name):

    teams1 = Players.query.filter_by(league_name=league_name).all()
    clubArray = []

    for club1 in teams1:
        clubObj = {}
        clubObj['id'] = club1.id
        clubObj['name'] = club1.club_name
        clubArray.append(clubObj)

    return jsonify({'teams1' : clubArray})



@app.route('/clubs2/<league_name>')
def clubs2(league_name):

    teams2 = Players.query.filter_by(league_name=league_name).all()
    clubArray = []

    for club2 in teams2:
        clubObj = {}
        clubObj['id'] = club2.id
        clubObj['name'] = club2.club_name
        clubArray.append(clubObj)

    return jsonify({'teams2' : clubArray})


@app.route('/clubs3/<league_name>')
def clubs3(league_name):
    
    teams3 = Players.query.filter_by(league_name=league_name).all()
    clubArray = []
    
    for club3 in teams3:
        clubObj = {}
        clubObj['id'] = club3.id
        clubObj['name'] = club3.club_name
        clubArray.append(clubObj)
    return jsonify({'teams3' : clubArray})

@app.route('/clubs4/<league_name>')
def clubs4(league_name):

    teams4 = Players.query.filter_by(league_name=league_name).all()
    clubArray = []

    for club4 in teams4:
        clubObj = {}
        clubObj['id'] = club4.id
        clubObj['name'] = club4.club_name
        clubArray.append(clubObj)
    return jsonify({'teams4' : clubArray})


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


@app.route('/players1/<id>')
def players1(id):
    Player_nm1 = Players.query.filter_by(id=id).all()
    PlayArray = []

    for players1 in Player_nm1:
        playObj = {}
        playObj['id'] = players1.id
        playObj['name'] = players1.name
        PlayArray.append(playObj)

    return jsonify({'Player_nm1' : PlayArray})



@app.route('/players2/<id>')
def players2(id):
    Player_nm2 = Players.query.filter_by(id=id).all()
    PlayArray = []

    for players2 in Player_nm2:
        playObj = {}
        playObj['id'] = players2.id
        playObj['name'] = players2.name
        PlayArray.append(playObj)
        
    return jsonify({'Player_nm2' : PlayArray})



@app.route('/players3/<id>')
def players3(id):
    Player_nm3 = Players.query.filter_by(id=id).all()
    PlayArray = []

    for players3 in Player_nm3:
        playObj = {}
        playObj['id'] = players3.id
        playObj['name'] = players3.name
        PlayArray.append(playObj)
        
    return jsonify({'Player_nm3' : PlayArray})



@app.route('/players4/<id>')
def players4(id):
    Player_nm4 = Players.query.filter_by(id=id).all()
    PlayArray = []
    
    for players4 in Player_nm4:
        playObj = {}
        playObj['id'] = players4.id
        playObj['name'] = players4.name
        PlayArray.append(playObj)
    
    return jsonify({'Player_nm4' : PlayArray})



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

                return redirect(url_for('about'))

        return render_template('register.html', title='Register', form=form)

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
        if current_user.is_authenticated:
            User_Id = current_user.id
            PlayerFilter = UserTeam.query.filter(UserTeam.id == User_Id).all()
            if PlayerFilter ==[]:
                Playeradd = UserTeam(id=User_Id, player_1 ="Select First player", player_2 ="Select Second player", player_3 ="Select Third player", player_4 ="Select Fourth player", player_5="Select Fith PLayer")
                db.session.add(Playeradd)
                db.session.commit()

        form = LoginForm()
        if form.validate_on_submit():
                user = Users.query.filter_by(email=form.email.data).first()
                if user and bcrypt.check_password_hash(user.password, form.password.data):
                        login_user(user, remember=form.remember.data)
                        User_Id = current_user.id
                        Playeradd = UserTeam(id=User_Id, player_1 ="Select First player", player_2 ="Select Second player", player_3 ="Select Third player", player_4 ="Select Fourth player", player_5="Select Fith PLayer")
                        db.session.add(Playeradd)
                        db.session.commit()
                        next_page = request.args.get('next')
                        
                        if next_page:
                                return redirect(next_page)
                        else:
                                return redirect('about')
        return render_template('login.html', title='Login', form=form)

@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
        form = LeaguesForm()
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
