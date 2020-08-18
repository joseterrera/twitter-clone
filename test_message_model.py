"""Message model tests."""

# run these tests like:
#
#    python -m unittest test_message_model.py


import os
from unittest import TestCase
from sqlalchemy import exc

from models import db, User, Message, Follows, Likes

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"

# Now we can import app

from app import app


# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()

class UserModelTestCase(TestCase):
  """Test views for messages"""

  def setUp(self):
    """Create test client and sample data"""
    db.drop_all()
    db.create_all()

    self.uid = 94566
    u = User.signup('testing', 'testing@test.com', 'password', None)
    u.id = self.uid
    db.session.commit()

    self.u = User.query.get(self.uid)
    self.client = app.test_client()

  def teardown(self):
    res = super().teardown()
    db.session.rollback()
    return res
  
  def test_message_model(self):
    """Does basic model work?"""

    m = Message(
      text="a warble"
      user_id=self.uid
    )

    db.session.add(m)
    db.session.commit()

    self.assertEqual(len(self.u.messages), 1)
    self.assertEqual(self.u.messages[0].text, 'a warble')

