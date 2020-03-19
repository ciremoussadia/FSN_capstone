
import unittest
from app import create_app
from models import *


class MovieAgencyTestCase(unittest.TestCase):
  def setUp(self):
    
    self.app = create_app()
    self.client = self.app.test_client
    self.database_path = os.environ['TEST_DATABASE_URL']
    setup_db(self.app, self.database_path)

    with self.app_context():
      self.db = SQLAlchemy()
      self.db.init_app(self.app)
      db.drop_all()
      db.create_all()

  def tearDown(self):
    pass


if __name__ == "__main__":
  unittest.main()
