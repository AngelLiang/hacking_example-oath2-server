from website.app import create_app


app = create_app({
    'SECRET_KEY': 'secret',
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///db.sqlite',
})


@app.cli.command()
def initdb():
    """
    数据库初始化
    """
    from website.models import db
    db.create_all()
