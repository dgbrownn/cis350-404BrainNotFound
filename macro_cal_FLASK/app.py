from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'your-secret-key-123'  # Change this to a real secret key

# Admin credentials
ADMIN_EMAIL = "admin@macrocal.com"
ADMIN_PASSWORD = "pass"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials', 'error')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        exercise = int(request.form.get('exercise'))
        gender = request.form.get('gender')
        
        # Determine activity level
        if exercise >= 5:
            activity = 'active'
        elif exercise >= 3:
            activity = 'moderate'
        else:
            activity = 'sedentary'
        
        # Create Calories instance
        user = Calories(
            goal='maintain weight',  # Default goal
            ht=height,
            wt=weight,
            gender=gender,
            age=30,  # Default age
            activity_lvl=activity
        )
        
        # Store results in session
        session['user_data'] = {
            'maint_cals': user.maint_cals,
            'protein': user.ptn,
            'carbs': user.carbs,
            'fats': user.fts
        }
        
        return redirect(url_for('home'))
    
    return render_template('signUp.html')

@app.route('/home')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    # Get calculated data or use defaults
    user_data = session.get('user_data', {
        'maint_cals': 2000,
        'protein': 150,
        'carbs': 250,
        'fats': 65
    })
    
    return render_template('homePage.html', **user_data)
@app.route('/update_protein', methods=['POST'])
def update_protein():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    data = request.get_json()
    protein_ratio = float(data['protein_ratio'])
    maint_cals = float(data['current_cals'])
    
    if 'user_data' in session:
        # Update all macros
        session['user_data']['protein'] = round((maint_cals * protein_ratio / 4), 2)
        remaining_ratio = 1 - protein_ratio
        session['user_data']['carbs'] = round((maint_cals * remaining_ratio * 0.6 / 4), 2)
        session['user_data']['fats'] = round((maint_cals * remaining_ratio * 0.4 / 9), 2)
    
    return {'status': 'success'}
@app.route('/settings')
def settings():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    user_data = session.get('user_data', {
        'maint_cals': 2000,
        'protein': 150,
        'carbs': 250,
        'fats': 65
    })
    
    return render_template('settings.html', **user_data)
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
class Calories:
    def __init__(self, goal, ht, wt, gender, age, activity_lvl):
       '''
        Init for Calories class
        :param ht: User height (in inches)
        :param wt: User weight (in pounds)
        :param gender: User gender (Male or Female)
        :param activity_lvl: User's activity level (sedentary [1-2 30 mins exercise per week]
        moderate [3-4 30 mins exercise per week], active [5+ 30 mins exercise per week]).
        - maint_cals: User's calculated maintenance calories (daily
        calorie intake to maintain bodyweight) called from function set_maintenance_cals.
        '''
       self.goal = goal
       self.height = ht
       self.weight = wt
       self.activity_lvl = activity_lvl
       self.gender = gender
       self.age = age
       self.maint_cals = self.set_maintenance_cals()
       self.sed_def = self.sedentary_deficit()
       self.fts = self.fats()
       self.ptn = self.protein()
       self.carbs = self.carbohydrates()

    def set_goal(self, goal):
        '''
        Allows a user to set their goals
        If entry is in valid list, return self.goal
        Otherwise, raise ValueError if not in the list
        or TypeError if entry is not a string
        '''
        valid = ['lose weight', 'gain weight', 'waintain weight']
        for i in valid:
            if goal.lower() not in valid:
                raise ValueError(f'Invalid entry, must be from the following choices:\nLose Weight, Gain Weight, or Maintain Weight')
            elif not isinstance(goal, str):
                raise TypeError(f'Must be a string')
            else:
                return self.goal
    
    def get_goal(self):
        '''
        Returns a user's goal
        '''
        return self.goal

    def set_height(self, ht):
        '''
        Sets user's height
        :param ht: User's height. Must not be zero.
        :return: User's height if check passes, raises TypeError if input is not an integer.
        '''
        if not isinstance(ht, int):
            raise TypeError(f'Invalid, enter height in inches')
        if self.height != 0:
            self.height = ht
        return self.height

    def get_height(self):
        '''
        Gets user's height
        '''
        return self.height

    def set_weight(self, wt):
        '''
        Sets user's weight
        :param wt: User's weight. Must not be zero
        :return: User's weight if check passes, raises TypeError if input is not an integer.
        '''
        if not isinstance(wt, int):
            raise TypeError(f'Invalid, enter weight to the nearest pound')
        if self.weight != 0:
            self.weight = wt
        return self.weight

    def get_weight(self):
        '''
        Gets user's height
        '''
        return self.weight

    def set_gender(self, gender):
        '''
        :param gender: User's gender, must be a string and within the list 'valid'
        Sets a user's gender if the user's input is within the list of valid gender options (male or female)
        If user's input is not a valid option, raises ValueError
        '''
        valid = ['male', 'female']
        if not isinstance(gender, str):
            raise TypeError
        for i in valid:
            if gender.lower() != i:
                raise ValueError('Male or Female')
        else:
            self.gender = gender
        return self.gender

    def get_gender(self):
        '''
        Gets/returns user's gender
        '''
        return self.gender

    def set_age(self, age):
        '''
        :param age: User's age
        Sets user's age if value is not 0 and is an integer
        '''
        if not isinstance(age, int):
            raise TypeError('Must be a number')
        if age != 0:
            self.age = age
        return self.age

    def get_age(self):
        '''
        Gets/returns user's age
        '''
        return self.age

    def set_activity_level(self, activity_lvl):
        '''
        Sets a user's activity level if it is a valid option and of type string
        valid = list of valid options for activity level
        '''
        valid = ['sedentary', 'moderate', 'active']
        if not isinstance(activity_lvl, str):
            raise TypeError
        for i in valid:
            if activity_lvl.lower() != i:
                raise ValueError(f'Please select between sedentary, moderate, and active')
        return self.activity_lvl

    def get_activity_level(self):
        '''
        Returns a user's activity level
        '''
        return self.activity_lvl

    def basal_metabolic_rate(self):
        '''
        Uses Harris-Benedict Formula to calculate a user's basal metabolic ratee (bmr)
        Basal Metabolic Rate - Amount of energy (calories) a person needs to function while at rest
        '''
        if self.gender.lower() == 'female':
            bmr = 655 + (4.35 * self.weight) + (4.7 * self.height) - (4.7 * self.age)
        if self.gender.lower() == 'male':
            bmr = 66 + (6.23 * self.weight) + (12.7 * self.height) - (6.8 * self.age)
        bmr = round(bmr, 2)
        return bmr

    def set_maintenance_cals(self):
        '''
        Calculate's a user's maintenance calories based off their activity level and BMR
        '''
        if not isinstance(self.basal_metabolic_rate(), float):
            raise TypeError
        if self.activity_lvl.lower() == 'active':
            self.maint_cals = self.basal_metabolic_rate() * 1.725
        if self.activity_lvl.lower() == 'moderate':
            self.maint_cals = self.basal_metabolic_rate() * 1.55
        if self.activity_lvl.lower() == 'sedentary':
            self.maint_cals = self.basal_metabolic_rate() * 1.2
        return round(self.maint_cals, 2)
        
    def active_deficit(self):
        '''
        Deficit's based off of activity level. Gradually decreases for each step 'up' in activity
        I.E. Active activity level will require more calroies for a deficit than sedentary 
        '''
        if self.goal.lower() == 'lose weight':
            if self.activity_lvl.lower() == 'active':
                if self.maint_cals != 0:
                    self.active_def = self.maint_cals - 300
                return round(self.active_def, 2)

    def moderate_deficit(self):
        '''
        See active_deficit comment
        '''
        if self.goal.lower() == 'lose weight':
            if self.activity_lvl.lower() == 'moderate':
                if self.maint_cals != 0:
                    self.mod_def = self.maint_cals - 500
                return round(self.mod_def, 2)

    def sedentary_deficit(self):
        '''
        See active_deficit comment
        '''
        if self.goal.lower() == 'lose weight':
            if self.activity_lvl.lower() == 'sedentary':
                if self.maint_cals != 0:
                    self.sed_def = self.maint_cals - 800
                return round(self.sed_def, 2)

    def active_surplus(self):
         '''
        Surpluses based off of activity level. Gradually increases for each step 'up' in activity
        I.E. Active activity level will require more calories for a surplus than sedentary 
        '''
         if self.goal.lower() == 'gain weight':
            if self.activity_lvl.lower() == 'active':
                if self.maint_cals != 0:
                    self.act_surplus = self.maint_cals + 800
                return round(self.act_surplus, 2)

    def moderate_surplus(self):
        '''
        See active_surplus comment
        '''
        if self.goal.lower() == 'gain weight':
            if self.activity_lvl.lower() == 'moderate':
                if self.maint_cals != 0:
                    self.mod_surplus = self.maint_cals + 500
                return round(self.mod_surplus, 2)

    def sedentary_surplus(self):
        '''
        See active_surplus comment
        '''
        if self.goal.lower() == 'gain weight':
            if self.activity_lvl.lower() == 'sedentary':
                if self.maint_cals != 0:
                    self.sed_surplus = self.maint_cals + 300
                return round(self.sed_surplus, 2)

    def fats(self):
        '''
        Calculates fats based off suggested daily calorie intake percentages
        '''
        if self.maint_cals != 0:
            return round(self.maint_cals * .20 / 9, 2)
    
    def protein(self):
        '''
        Calculates protein based off suggested daily calorie intake percentages
        '''
        if self.maint_cals != 0:
            return round((self.maint_cals * .3 / 4), 2)
    
    def carbohydrates(self):
        '''
        Calculates carbohydrates based off suggested daily calorie intake percentages
        '''
        if self.maint_cals != 0:
            return round(self.maint_cals * .45 / 4, 2)
    def set_protein_goal(self, protein_ratio):
        """Set custom protein ratio (0.0 to 1.0)"""
        if not 0 <= protein_ratio <= 1:
            raise ValueError("Protein ratio must be between 0 and 1")
        self.protein_ratio = protein_ratio
        self.ptn = round((self.maint_cals * protein_ratio / 4), 2)
        # Recalculate other macros to maintain balance
        remaining_ratio = 0.7  # 70% for carbs/fats
        self.carbs = round((self.maint_cals * remaining_ratio * 0.6 / 4), 2)  # 60% of remaining
        self.fts = round((self.maint_cals * remaining_ratio * 0.4 / 9), 2)   # 40% of remaining

    def get_protein_goal(self):
        """Returns current protein ratio"""
        return self.protein_ratio        
    def __str__(self):
        '''
        Temporary str method for displaying output
        '''
        deficit = ''
        surplus = ''
        if self.goal.lower() == 'lose weight':
            if self.activity_lvl.lower() == 'active':
                deficit = self.active_deficit()
            if self.activity_lvl.lower() == 'moderate':
                deficit = self.moderate_deficit()
            if self.activity_lvl.lower() == 'sedentary':
                deficit = self.sedentary_deficit()
            return f'Maintenance calories: {self.maint_cals} kcal\nDeficit Calories: {deficit} kcal\nFats: {self.fts}g\nCarbs: {self.carbs}g\nProtein: {self.ptn}g'
        elif self.goal.lower() == 'gain weight':
            if self.activity_lvl.lower() == 'active':
                surplus = self.active_surplus()
            if self.activity_lvl.lower() == 'moderate':
                surplus = self.moderate_surplus()
            if self.activity_lvl.lower() == 'sedentary':
                surplus = self.sedentary_deficit()
            return f'Maintenance Calories: {self.maint_cals} kcal\nSurplus Calroies: {surplus} kcal\nFats: {self.fts}g\nCarbs: {self.carbs}g\nProtein: {self.ptn}g'
        elif self.goal.lower() == 'maintain weight':
            return f'Maintenance Calories: {self.maint_cals} kcal\nFats: {self.fts}g\nCarbs: {self.carbs}g\nProtein: {self.ptn}g'

if __name__ == '__main__':
    c = Calories('lose weight', 60, 200, 'male', 20, 'active')
    print(c.__str__())
if __name__ == '__main__':
    app.run(debug=True)
