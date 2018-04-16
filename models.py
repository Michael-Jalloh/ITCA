from peewee import *
import rsa
from werkzeug.security import generate_password_hash, check_password_hash

db = SqliteDatabase('auth.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(default="")
    first_name = CharField(default="")
    last_name = CharField(default="")
    password_hash = CharField()
    email = CharField()
    pub_key = CharField(default="")
    priv_key = CharField(default="")

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash, password)

    def details(self):
        return {
            'username': self.username,
            'id': self.id,
            'email':self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'pub_key':self.pub_key
        }

    def get_priv(self):
        return {
        'priv_key': self.priv_key
        }


    def generate_keys(self):
        print "[*] Generating rsa keys...."
        (pubkey, privkey) = rsa.newkeys(1024)
        self.pub_key = pubkey.save_pkcs1()
        self.priv_key = privkey.save_pkcs1()
        self.save()


class Agent(BaseModel):
    name = CharField(unique=True)
    password_hash = CharField()
    pub_key = CharField(default="")
    priv_key = CharField(default="")

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash, password)

    def details(self):
        return {
            'name': self.name,
            'id': self.id,
            'pub_key':self.pub_key
        }

    def get_priv(self):
        return {
        'priv_key': self.priv_key
        }


    def generate_keys(self):
        print "[*] Generating rsa keys...."
        (pubkey, privkey) = rsa.newkeys(1024)
        self.pub_key = pubkey.save_pkcs1()
        self.priv_key = privkey.save_pkcs1()
        self.save()



db.create_tables([Agent], safe=True)
db.create_tables([User], safe=True)
