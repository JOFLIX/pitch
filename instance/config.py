import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
WTF_CSRF_SECRET_KEY = SECRET_KEY