#from flask import Flask, make_response, session
#from requests import request
#from flask_login import LoginManager
#from data import db_session
#from data.users import User
#
#
#app = Flask(__name__)
#app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
#login_manager = LoginManager()
#login_manager.init_app(app)
#db_session.global_init('db/blogs.db')
#
#
#@login_manager.user_loader
#def load_user(user_id):
#    db_sess = db_session.create_session()
#    return db_sess.query(User).get(user_id)
#
#
#@app.route("/cookie_test")
#def cookie_test():
#    visits_count = int(request.cookies.get("visits_count", 0))
#    if visits_count:
#        res = make_response(
#            f"Вы пришли на эту страницу {visits_count + 1} раз")
#        res.set_cookie("visits_count", str(visits_count + 1),
#                       max_age=60 * 60 * 24 * 365 * 2)
#    else:
#        res = make_response(
#            "Вы пришли на эту страницу в первый раз за последние 2 года")
#        res.set_cookie("visits_count", '1',
#                       max_age=60 * 60 * 24 * 365 * 2)
#    return res
#
#
#@app.route("/session_test")
#def session_test():
#    visits_count = session.get('visits_count', 0)
#    session['visits_count'] = visits_count + 1
#    return make_response(
#        f"Вы пришли на эту страницу {visits_count + 1} раз")
#
#
#if __name__ == '__main__':
#    cookie_test()