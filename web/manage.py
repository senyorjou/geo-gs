from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask_marshmallow import Marshmallow

from app import app, db


migrate = Migrate(app, db)
manager = Manager(app)
ma = Marshmallow(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
