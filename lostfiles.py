# This was to handle the login, registration, and verification process
'''
# *NEW* Login form
class LoginForm(FlaskForm):
  username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
  password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
  remember = BooleanField('remember me')

# *NEW*
class RegisterForm(FlaskForm):
  email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
  username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
  password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

# *NEW*
@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()

  if form.validate_on_submit():
    return '<h1>' + form.username.data + ''+ form.password.data + '</h1>'

# *NEW*
@app.route('/signup', methods=['GET', 'POST'])
def signup():
  
  post_email = request.json['email']
  post_username = request.json['email']
  post_password = request.json['email']

  new_user = User(username=post_email, email=post_username, password=post_password)
  db.session.add(new_user)
  db.session.commit()

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(15), unique=True)
  email = db.Column(db.String(50), unique = True)
  password = db.Column(db.String(80))

  def __init__(self, username, email, password):
    self.username = username
    self.email = email
    self.password = password

class UserSchema(ma.Schema):
  class Meta:
    fields = ('id', 'username', 'email', 'password')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  
  post_email = request.json['email']
  post_username = request.json['email']
  post_password = request.json['email']

  new_user = User(username=post_email, email=post_username, password=post_password)
  db.session.add(new_user)
  db.session.commit()
'''



# Update a Post
  @app.route('/posts/<id>', methods=['PUT'])
  def updatepost(id): 
    post = BlogPost.query.get(id)

    
    content = request.json['content']
    
   
    post.content = content 
   

    db.session.commit()
          #return redirect('/posts')
    return blogpost_schema.jsonify(post)

  # Delete Post
  @app.route('/posts/<id>', methods=['DELETE'])
  def delete_post(id):
    post = BlogPost.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return blogpost_schema.jsonify(post)

'''
@app.route('/product', methods=['POST'])
def add_product():
  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  qty = request.json['qty']

  new_product = Product(name, description, price, qty)

  db.session.add(new_product)
  db.session.commit()

  return product_schema.jsonify(new_product)

# Get All Products
@app.route('/product', methods=['GET'])
def get_products():
  all_products = Product.query.all()
  result = products_schema.dump(all_products)
  return jsonify(result.data)

# Get Single Products
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
  product = Product.query.get(id)
  return product_schema.jsonify(product)

# Update a Product
@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
  product = Product.query.get(id)

  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  qty = request.json['qty']

  product.name = name
  product.description = description
  product.price = price
  product.qty = qty

  db.session.commit()

  return product_schema.jsonify(product)

# Delete Product
@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
  product = Product.query.get(id)
  db.session.delete(product)
  db.session.commit()

  return product_schema.jsonify(product)

'''